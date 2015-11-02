#-*- coding: utf-8 -*-
import signals
import error
import text
from log import logger
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
        self.connect(self.bleproxyAddressDialog, signals.SIG_CONNECT_SERVER, self.onConnectServer)
    
    def setupUi_disconnected(self):
        self.ui.scanBtn.setEnabled(False)
        self.ui.connectBtn.setText(text.CONNECT)
        
    def setupUi_connected(self):
        self.ui.scanBtn.setEnabled(True)
        self.ui.connectBtn.setText(text.DISCONNECT)
        
    def onConnectBtnClicked(self):
        self.bleproxyAddressDialog.show_()
    
    def onConnectServer(self, ip, port):
        if self.presenter.connectServer(ip, port):
            logger.debug("connect success")
            self.tipPupup.makeInfoText(text.CONNECTED_TIPS)
            self.setupUi_connected()
        else:
            logger.error("connect error")
            self.tipPupup.makeErrorText(error.TCP_CLIENT_CONNECT_ERROR)
            
    def closeEvent(self, e):
        self.presenter.stopTcpClient()
        e.accept()