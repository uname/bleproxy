# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main_window.ui'
#
# Created: Wed Nov 04 16:07:55 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(849, 516)
        MainWindow.setStyleSheet(_fromUtf8("font: 9pt \"宋体\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.connectBtn = QtGui.QPushButton(self.centralwidget)
        self.connectBtn.setMinimumSize(QtCore.QSize(85, 0))
        self.connectBtn.setMaximumSize(QtCore.QSize(85, 16777215))
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.gridLayout.addWidget(self.connectBtn, 0, 0, 1, 1)
        self.scanBtn = QtGui.QPushButton(self.centralwidget)
        self.scanBtn.setMinimumSize(QtCore.QSize(100, 23))
        self.scanBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scanBtn.setObjectName(_fromUtf8("scanBtn"))
        self.gridLayout.addWidget(self.scanBtn, 0, 1, 1, 1)
        self.sockTab = SockTab(self.centralwidget)
        self.sockTab.setIconSize(QtCore.QSize(256, 16))
        self.sockTab.setObjectName(_fromUtf8("sockTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 611, 81))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.archView = QtGui.QLabel(self.tab)
        self.archView.setGeometry(QtCore.QRect(10, 110, 459, 147))
        self.archView.setObjectName(_fromUtf8("archView"))
        self.sockTab.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.sockTab, 0, 2, 2, 1)
        self.bleListWgt = BleListWidget(self.centralwidget)
        self.bleListWgt.setMinimumSize(QtCore.QSize(191, 433))
        self.bleListWgt.setMaximumSize(QtCore.QSize(250, 16777215))
        self.bleListWgt.setObjectName(_fromUtf8("bleListWgt"))
        self.gridLayout.addWidget(self.bleListWgt, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sockTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BleProxyDesk", None, QtGui.QApplication.UnicodeUTF8))
        self.connectBtn.setText(QtGui.QApplication.translate("MainWindow", "连接", None, QtGui.QApplication.UnicodeUTF8))
        self.scanBtn.setText(QtGui.QApplication.translate("MainWindow", "扫描蓝牙", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BleProxy是用于桥接BLE蓝牙和WiFi通讯的代理</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">通过PC端BleProxyDesk连接到Android端的BleProxy服务，即可方便的进行BLE蓝牙通讯调试</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.archView.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTab.setTabText(self.sockTab.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))

from view.SockTab import SockTab
from view.BleListWidget import BleListWidget
