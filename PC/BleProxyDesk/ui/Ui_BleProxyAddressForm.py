# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/bleproxy_address_form.ui'
#
# Created: Mon Nov 02 20:03:16 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BleProxyAddressForm(object):
    def setupUi(self, BleProxyAddressForm):
        BleProxyAddressForm.setObjectName(_fromUtf8("BleProxyAddressForm"))
        BleProxyAddressForm.resize(344, 147)
        self.gridLayout = QtGui.QGridLayout(BleProxyAddressForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(BleProxyAddressForm)
        self.label_2.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.ipCmbBox = QtGui.QComboBox(BleProxyAddressForm)
        self.ipCmbBox.setEditable(True)
        self.ipCmbBox.setObjectName(_fromUtf8("ipCmbBox"))
        self.ipCmbBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.ipCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(BleProxyAddressForm)
        self.label.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portCmbBox = QtGui.QComboBox(BleProxyAddressForm)
        self.portCmbBox.setEditable(True)
        self.portCmbBox.setObjectName(_fromUtf8("portCmbBox"))
        self.portCmbBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.portCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okBtn = QtGui.QPushButton(BleProxyAddressForm)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.cancelBtn = QtGui.QPushButton(BleProxyAddressForm)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.retranslateUi(BleProxyAddressForm)
        QtCore.QMetaObject.connectSlotsByName(BleProxyAddressForm)

    def retranslateUi(self, BleProxyAddressForm):
        BleProxyAddressForm.setWindowTitle(QtGui.QApplication.translate("BleProxyAddressForm", "连接BleProxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BleProxyAddressForm", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.ipCmbBox.setItemText(0, QtGui.QApplication.translate("BleProxyAddressForm", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BleProxyAddressForm", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.portCmbBox.setItemText(0, QtGui.QApplication.translate("BleProxyAddressForm", "8927", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setText(QtGui.QApplication.translate("BleProxyAddressForm", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("BleProxyAddressForm", "取消", None, QtGui.QApplication.UnicodeUTF8))

