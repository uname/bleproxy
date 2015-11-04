#-*- coding: utf-8 -*-
import signals
import text
import config
from log import logger
from SigObject import sigObject
from form.TipPupup import TipPupup
from ui.AppIcons import *
from ui.Ui_MainWindow import Ui_MainWindow
from presenter.MainWindowPresenter import MainWindowPresenter
from form.BleproxyAddressDialog import BleproxyAddressDialog
from form.ProgressDialog import ProgressDialog
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(config.LOGO_PNG))
        self.ui.archView.setPixmap(QtGui.QPixmap(config.ARCH_PNG))
        self.setupUi_disconnected()
        self.tipPupup = TipPupup()
        self.presenter = MainWindowPresenter(self)
        self.bleproxyAddressDialog = BleproxyAddressDialog(self)
        self.progressDialog = ProgressDialog(self)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.connectBtn.clicked.connect(self.onConnectBtnClicked)
        self.ui.scanBtn.clicked.connect(self.onScanBtnClicked)
        self.ui.bleListWgt.itemDoubleClicked.connect(self.onBleItemDoubleClicked)
        self.connect(self.bleproxyAddressDialog, signals.SIG_CONNECT_SERVER, self.onConnectServer)
        
        self.connect(sigObject, signals.SIG_MSG_RECVED, self.presenter.handleDataBuff)
        self.connect(sigObject, signals.SIG_BLE_DEVICE, self.onBleDevice)
        self.connect(sigObject, signals.SIG_CONNECT_RESULT, self.onConnectResult)
        self.connect(sigObject, signals.SIG_DISCONNECT_BLE, self.onDisconnectBle)
        self.connect(sigObject, signals.SIG_SERVER_CLOSED, self.onServerClosed)
        self.connect(sigObject, signals.SIG_BLE_DISCONNECTED, self.onBleDisconnected)
    
    def setupUi_disconnected(self):
        self.ui.scanBtn.setEnabled(False)
        self.ui.scanBtn.setText(text.TEXT_ON_NOT_SCANNING)
        self.ui.connectBtn.setText(text.CONNECT)
        self.ui.bleListWgt.clear_()
        
    def setupUi_connected(self):
        self.ui.bleListWgt.setEnabled(True)
        self.ui.scanBtn.setEnabled(True)
        self.ui.connectBtn.setText(text.DISCONNECT)
        
    def onConnectBtnClicked(self):
        if self.presenter.isConnected():
            self.presenter.stopTcpClient()
            self.setupUi_disconnected()
            self.ui.sockTab.removeSockForm()
            self.ui.bleListWgt.setCurAddress(None)
        else:
            self.bleproxyAddressDialog.show_()
    
    def onDisconnectBle(self):
        self.ui.sockTab.removeSockForm()
        self.ui.bleListWgt.setEnabled(True)
        self.ui.bleListWgt.setCurAddress(None)
        self.ui.scanBtn.setEnabled(True)
        self.presenter.setScanning(False)
    
    def onServerClosed(self):
        logger.debug("server closed")
        self.tipPupup.makeErrorText(text.SERVER_CLOSED, 4000)
        self.onDisconnectBle()
        self.presenter.stopTcpClient()
        self.setupUi_disconnected()
    
    def onBleDisconnected(self):
        self.tipPupup.makeErrorText(text.BLE_DISCONNECTED, 4000)
        self.onDisconnectBle()
        
    def onBleItemDoubleClicked(self, item):
        if item.isConnected():
            logger.debug("already connected")
            return
            
        logger.debug("connect to ble device: %s" % item.getAddress())
        ret = self.presenter.connectBleDevice(item.getAddress())
        if ret:
            self.progressDialog.show()
        else:
            self.tipPupup.makeErrorText(text.SEND_PKG_ERROR)
        
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
            self.tipPupup.makeErrorText(text.TCP_CLIENT_CONNECT_ERROR)
    
    def onConnectResult(self, result, address, errorString):
        if self.progressDialog.isActiveWindow():
            self.progressDialog.cancel()
            
        if not result:
            logger.debug("Connect ble device error: %s" % errorString)
            self.tipPupup.makeErrorText(text.CONNECT_BLE_ERROR)
            return
            
        logger.debug("Connect ble device %s OK" % address)
        #self.tipPupup.makeInfoText(text.CONNECT_BLE_OK)
        self.ui.scanBtn.setEnabled(False)
        self.ui.scanBtn.setText(text.TEXT_ON_NOT_SCANNING)
        self.ui.bleListWgt.setEnabled(False)
        self.ui.bleListWgt.setCurAddress(address)
        self.ui.sockTab.addSockForm(self.presenter.getTcpClient())
        
    def onBleDevice(self, name, address, rssi):
        #logger.debug("%s[%s]\t\t%d" % (name, address, rssi))
        self.ui.bleListWgt.addBleDevice(name, address, rssi)
        
    def closeEvent(self, e):
        self.presenter.stopTcpClient()
        e.accept()