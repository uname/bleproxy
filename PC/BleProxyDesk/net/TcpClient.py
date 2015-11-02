#-*- coding: utf-8 -*-
from log import logger
from SigObject import sigObject
import signals
import socket
import select
import threading

class TcpClient(threading.Thread):
    
    RECV_SIZE = 262144
    
    def __init__(self, ip=None, port=None):
        threading.Thread.__init__(self)
        self.stopflag = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(0)
        self.ip, self.port = ip, port
        
    def connect(self):
        try:
            if self.sock is None:
                self.createSockByType(self.sockType)
                
            self.sock.settimeout(0.3)
            self.sock.connect((self.ip, self.port))
            self.sock.setblocking(0)
            self.conFlag = True
            return True
            
        except Exception as e:
            logger.error("connect exp: %s" % e.message)
            return
        
    def sendall(self, data):
        if not isinstance(data, basestring):
            return False
        
        return self.sock.sendall(data) is None
        
    def close(self):
        logger.debug("------ CLOSE ------")
        if self.sock is None:
            return
        
        self.sock.close()
        self.sock = None
            
    def stop(self):
        self.stopflag = True
        
    def run(self):
        while not self.stopflag:
            rfds, _, efds = select.select([self.sock], [], [self.sock], 0.1)
            if len(efds) > 0:
                logger.error("remote client error")
                break
                
            if len(rfds) < 1:
                continue
                
            data = self.sock.recv(SockClient.RECV_SIZE)
            if data == "":
                logger.error("socket closed")
                break
            
            logger.debug("data from %s:%d -> %s" % (self.ip, self.port, data))
            sigObject.emit(signals.SIG_DATA_RECVED, self._id, data)
        
        self.close()
        logger.debug("tcp client stopped")
        