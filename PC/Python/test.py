#-*- coding: utf-8 -*-
import BleProxyMsg_pb2 as pb
import struct

class BleProxyManager:
    
    def __init__(self, tcpClient):
        self.tcpClient = tcpClient
        self.msg = pb.BleProxyMsg()
    
    def sendMsg(self, pbMsg):
        pbBuff = pbMsg.SerializeToString()
        lenBuff = struct.pack('H', len(pbBuff))
        return self.tcpClient.sendall(lenBuff + pbBuff) is None
        
    def connect(self, address):
        if not isinstance(address, basestring):
            return
        
        self.msg.cmd = pb.CONNECT
        self.msg.connect.address = address
        
        return self.sendMsg(self.msg)
        
    def control(self, controlCmd):
        self.msg.cmd = pb.CONTROL
        self.msg.control.cmd = controlCmd
        
        return self.sendMsg(self.msg)
        
    def startScan(self):
        return self.control(pb.START_SCAN)
        
    def stopScan(self):
        return self.control(pb.STOP_SCAN)
   
    def sendData(self, data):
        self.msg.cmd = pb.PROXY_DATA
        self.msg.proxyData.data = data
        
        return self.sendMsg(self.msg)

import socket
import threading
import select

class TcpClient:

    RECV_SIZE = 262144
    
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.5)
        self.receiver = None
    
    def connectServer(self, ip, port):
        try:
            self.sock.connect((ip, port))
            self.sock.setblocking(0)
            return True
        except Exception as e:
            print e
            return
    
    def sendall(self, data):
        if not isinstance(data, basestring):
            return False
        
        return self.sock.sendall(data)
    
    def close(self):
        self.sock.close()
        
    def stop(self):
        self.receiver.stopflag = True
    
    def start(self):
        self.receiver = TcpClient.Receiver(self)
        self.receiver.start()
        
    class Receiver(threading.Thread):
        
        def __init__(self, parent):
            threading.Thread.__init__(self)
            self.parent = parent
            self.stopflag = False
            
        def run(self):
            while not self.stopflag:
                rfds, _, efds = select.select([self.parent.sock], [], [self.parent.sock], 0.1)
                if len(efds) > 0:
                    print "socket error"
                    break
                
                if len(rfds) < 1:
                    continue
                
                data = self.parent.sock.recv(TcpClient.RECV_SIZE)
                if data == "":
                    print "socket closed"
                    break
                    
                print data
            
            self.parent.close()

import sys
def main():
    tcpClient = TcpClient()
    if not tcpClient.connectServer("10.66.236.56", 8927):
        print "connect failed"
        sys.exit(1)
    
    print "connect success"
    tcpClient.start()
    bleProxyMgr = BleProxyManager(tcpClient)
    
    while 1:
        cmd = raw_input(">")
        if cmd == "quit":
            break
            
        print bleProxyMgr.connect("74:DA:EA:AE:9A:33")
    
    tcpClient.stop()
    
if __name__ == "__main__":
    main()