#-*- coding: utf-8 -*-
from net.TcpClient import TcpClient

class MainWindowPresenter:
    
    def __init__(self, view):
        self.view = view
        self.tcpClient = None
        
    def connectServer(self, ip, port):
        if not self.tcpClient:
            self.tcpClient = TcpClient(ip, port)
        ret = self.tcpClient.connect()
        if ret:
            self.tcpClient.start()
            
        return True
    
    def stopTcpClient(self):
        if self.tcpClient:
            self.tcpClient.stop()
        