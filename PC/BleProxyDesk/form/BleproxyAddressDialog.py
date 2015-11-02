#-*- coding: utf-8 -*-
import utils
import signals
from ui.Ui_BleProxyAddressForm import Ui_BleProxyAddressForm
from PyQt4 import QtGui

class BleproxyAddressDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_BleProxyAddressForm()
        self.ui.setupUi(self)
        self.initIpList()
        self.setModal(True)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
    
    def initIpList(self):
        pass
        
    def onOkBtnClicked(self):
        strPort = utils.qstr2str(self.ui.portCmbBox.currentText())
        if not strPort.isdigit():
            return
            
        port = int(strPort)
        if not utils.isPortOk(port):
            return
        
        self.emit(signals.SIG_CONNECT_SERVER, utils.qstr2str(self.ui.ipCmbBox.currentText()), port)
        self.close()
    
    def show_(self):
        self.ui.portCmbBox.setFocus()
        self.show()
