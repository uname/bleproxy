#-*- coding: utf-8 -*-
import signals
import error
import text
from log import logger
from SigObject import sigObject
from form.TipPupup import TipPupup
from ui.Ui_MainWindow import Ui_MainWindow
from presenter.MainWindowPresenter import MainWindowPresenter
from form.BleproxyAddressDialog import BleproxyAddressDialog
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi_disconnected()
        self.tipPupup = TipPupup()
        self.presenter = MainWindowPresenter(self)
        self.bleproxyAddressDialog = BleproxyAddressDialog(self)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.connectBtn.clicked.connect(self.onConnectBtnClicked)
        self.ui.scanBtn.clicked.connect(self.onScanBtnClicked)
        self.connect(self.bleproxyAddressDialog, signals.SIG_CONNECT_SERVER, self.onConnectServer)
        
        self.connect(sigObject, signals.SIG_MSG_RECVED, self.presenter.handleDataBuff)
        self.connect(sigObject, signals.SIG_BLE_DEVICE, self.onBleDevice)
    
    def setupUi_disconnected(self):
        self.ui.scanBtn.setEnabled(False)
        self.ui.connectBtn.setText(text.CONNECT)
        self.ui.bleListWgt.clear_()
        
    def setupUi_connected(self):
        self.ui.scanBtn.setEnabled(True)
        self.ui.connectBtn.setText(text.DISCONNECT)
        
    def onConnectBtnClicked(self):
        if self.presenter.isConnected():
            self.presenter.stopTcpClient()
            self.setupUi_disconnected()
        else:
            self.bleproxyAddressDialog.show_()
    
    def onScanBtnClicked(self):
        ret, scanning = self.presenter.scan()
        if not ret:
            return
        
        self.ui.scanBtn.setText(scanning and text.TEXT_ON_SCANNING or text.TEXT_ON_NOT_SCANNING)
        
    def onConnectServer(self, ip, port):
        if self.presenter.connectServer(ip, port):
            logger.debug("connect success")
            self.setupUi_connected()
            self.tipPupup.makeInfoText(text.CONNECTED_TIPS)
        else:
            logger.error("connect error")
            self.tipPupup.makeErrorText(error.TCP_CLIENT_CONNECT_ERROR)
    
    def onBleDevice(self, name, address, rssi):
        #logger.debug("%s[%s]\t\t%d" % (name, address, rssi))
        self.ui.bleListWgt.addBleDevice(name, address, rssi)
        
    def closeEvent(self, e):
        self.presenter.stopTcpClient()
        e.accept()