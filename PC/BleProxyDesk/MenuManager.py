#-*- coding: utf-8 -*-
import text
from PyQt4 import QtGui

class MenuManager:
    
    def __init__(self, winobj):
        self.winobj = winobj
        self.initBleListWgtPopmenu()
    
    def initBleListWgtPopmenu(self):
        self.winobj.ui.bleListWgt.popMenu = QtGui.QMenu(self.winobj)
        actionCpMacAddress = QtGui.QAction(text.CP_MAC, self.winobj, priority=QtGui.QAction.LowPriority, triggered=self.winobj.onCpMacAddress)
        self.winobj.ui.bleListWgt.popMenu.addAction(actionCpMacAddress)
        