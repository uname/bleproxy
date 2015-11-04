#-*- coding: utf-8 -*-
from log import logger
from BleListItem import BleListItem
from PyQt4 import QtGui

class BleListWidget(QtGui.QListWidget):
    
    def __init__(self, parent=None):
        QtGui.QListWidget.__init__(self, parent)
        self.bleItemDict = {}
        self.curAddress = ""
        
    def addBleDevice(self, name, address, rssi):
        item = None
        if self.bleItemDict.has_key(address):
            item = self.bleItemDict.get(address)
            item.updateRssi(rssi)
        else:
            item = BleListItem(name, address, rssi)
            self.addItem(item)
            self.bleItemDict[address] = item
    
    def setCurAddress(self, address):
        item = None
        if not address:
            item = self.bleItemDict.get(self.curAddress)
            if not item:
                return
        else:
            item = self.bleItemDict.get(address)
        
        if not item:
            logger.error("NO SUCH DEVICE")
            return
        
        self.curAddress = address
        item.setConnected(address)
    
    def getCurAddress(self):
        return self.curAddress
        
    def clear_(self):
        self.bleItemDict = {}
        self.clear()