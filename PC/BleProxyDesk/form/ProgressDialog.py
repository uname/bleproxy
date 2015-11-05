#-*- coding: utf-8 -*-
import text
import config
from PyQt4 import QtGui, QtCore

class ProgressDialog(QtGui.QProgressDialog):
    
    def __init__(self, parent, waitTime=config.BLE_CONNECT_TIMEOUT, title="Please wait", max=100):
        QtGui.QProgressDialog.__init__(self, title, "Hide", 0, max, parent)
        self.setWindowTitle(text.CONNECTING_BLE_DEVICE)
        
        self.step, self.max = 0, max
        self.interval = waitTime / max + 1
        self.canceled.connect(self.onCanceled)
        
    def show(self):
        self.open()
        self.step = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start(self.interval)
    
    def cancel(self):
        self.timer.stop()
        self.close()
        
    def onTimeout(self):
        self.setValue(self.step)
        if self.step >= self.max:
            self.onWaitTimeout()
            
        self.step += 1
        
    def onCanceled(self):
        self.timer.stop()
        
    def onWaitTimeout(self):
        self.onCanceled()