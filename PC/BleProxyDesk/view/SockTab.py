#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from ui.AppIcons import *
from form.SocketForm import SocketForm

class SockTab(QtGui.QTabWidget):
    
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        
    def addSockForm(self, tcpClient, label="Proxy"):
        form = SocketForm(tcpClient, self)
        self.addTab(form, label)
        self.setCurrentIndex(self.count() - 1)
    
    def removeSockForm(self, index=1):
        assert index == 1    # TODO: only one sockform now
        if self.count() < index + 1:
            return
            
        self.removeTab(index)