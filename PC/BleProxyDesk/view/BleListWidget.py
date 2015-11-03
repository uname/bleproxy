#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from BleListItem import BleListItem

class BleListWidget(QtGui.QListWidget):
    
    def __init__(self, parent=None):
        QtGui.QListWidget.__init__(self, parent)
        self.bleItemDict = {}
        
    def addBleDevice(self, name, address, rssi):
        item = None
        if self.bleItemDict.has_key(address):
            item = self.bleItemDict.get(address)
            item.updateRssi(rssi)
        else:
            item = BleListItem(name, address, rssi)
            self.addItem(item)
            self.bleItemDict[address] = item
            
    def clear_(self):
        self.bleItemDict = {}
        self.clear()