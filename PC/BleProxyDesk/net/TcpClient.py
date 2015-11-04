#-*- coding: utf-8 -*-
from log import logger
from SigObject import sigObject
import struct
import signals
import socket
import select
import threading

class TcpClient(threading.Thread):
    
    def __init__(self, ip=None, port=None):
        threading.Thread.__init__(self)
        self.stopflag = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip, self.port = ip, port
        self.connected = False
    
    def isConnected(self):
        return self.connected
        
    def connect(self):
        try:
            if self.sock is None:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
            self.sock.settimeout(0.5)
            self.sock.connect((self.ip, self.port))
            self.sock.setblocking(0)
            self.connected = True
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
        self.connected = False
            
    def stop(self):
        self.stopflag = True
        
    def run(self):
        data = ""
        while not self.stopflag:
            rfds, _, efds = select.select([self.sock], [], [self.sock], 0.1)
            if len(efds) > 0:
                logger.error("remote client error")
                break
                
            if len(rfds) < 1:
                continue
                
            try:
                data = self.sock.recv(2)
            except Exception as e:
                logger.error("sock exp. %s" % e.message)
                break
            if not data:
                break
                
            size = struct.unpack("H", data)[0]
            try:
                data = self.sock.recv(size)
            except Exception as e:
                logger.error("sock exp. %s" % e.message)
                break
            if not data:
                break
                
            sigObject.emit(signals.SIG_MSG_RECVED, data)
        
        self.close()
        logger.debug("tcp client stopped")
        