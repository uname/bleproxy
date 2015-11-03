#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from ui.AppIcons import *

class BleListItem(QtGui.QListWidgetItem):
    
    def __init__(self, name, address, rssi):
        QtGui.QListWidgetItem.__init__(self)
        self.name, self.address, self.rssi = name, address, rssi
        self.setBleInfo(rssi)
    
    def setBleInfo(self, rssi):
        iconPath = ":app/icons/app/sig_1.png"
        if rssi > -45:
            iconPath = ":app/icons/app/sig_4.png"
        elif rssi > -60:
            iconPath = ":app/icons/app/sig_3.png"
        elif rssi > -80:
            iconPath = ":app/icons/app/sig_2.png"
            
        self.setIcon(QtGui.QIcon(iconPath))
        self.setText("%s\n%s    %ddb\n" % (self.name, self.address, rssi))
        
    def updateRssi(self, rssi):
        self.setBleInfo(rssi)