#-*- coding: utf-8 -*-
from net.TcpClient import TcpClient
from protocol.ProtocolPacker import protocolPacker
from protocol.ProtocolHandler import protocolHandler
from log import logger
import utils

class MainWindowPresenter:
    
    def __init__(self, view):
        self.view = view
        self.tcpClient = None
        self.scanning = False
    
    def getTcpClient(self):
        return self.tcpClient
        
    def isConnected(self):
        return self.tcpClient and self.tcpClient.isConnected()
        
    def setScanning(self, flag):
        self.scanning = flag
        
    def connectServer(self, ip, port):
        if not self.tcpClient:
            self.tcpClient = TcpClient(ip, port)
        ret = self.tcpClient.connect()
        if ret:
            self.tcpClient.start()
            
        return ret
        
    def connectBleDevice(self, address):
        buff = protocolPacker.getConnectBuff(address)
        return self.tcpClient.sendall(buff)
    
    def stopTcpClient(self):
        if self.tcpClient:
            self.tcpClient.stop()
            self.tcpClient = None
            self.scanning = False
        
    def scan(self):
        buff = self.scanning and protocolPacker.getStopScanBuff() or protocolPacker.getStartScanBuff()
        ret = self.tcpClient.sendall(buff)
        if ret:
            self.scanning = not self.scanning

        return ret, self.scanning
        
    def handleDataBuff(self, data):
        protocolHandler.handleDataBuff(data)
        