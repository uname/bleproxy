# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main_window.ui'
#
# Created: Tue Nov 03 18:48:15 2015
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
        MainWindow.resize(843, 516)
        MainWindow.setStyleSheet(_fromUtf8("font: 9pt \"宋体\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.connectBtn = QtGui.QPushButton(self.centralwidget)
        self.connectBtn.setMaximumSize(QtCore.QSize(85, 16777215))
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.gridLayout.addWidget(self.connectBtn, 0, 0, 1, 1)
        self.scanBtn = QtGui.QPushButton(self.centralwidget)
        self.scanBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scanBtn.setObjectName(_fromUtf8("scanBtn"))
        self.gridLayout.addWidget(self.scanBtn, 0, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 2, 2, 1)
        self.bleListWgt = BleListWidget(self.centralwidget)
        self.bleListWgt.setMinimumSize(QtCore.QSize(0, 351))
        self.bleListWgt.setMaximumSize(QtCore.QSize(250, 16777215))
        self.bleListWgt.setObjectName(_fromUtf8("bleListWgt"))
        self.gridLayout.addWidget(self.bleListWgt, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BleProxyDesk", None, QtGui.QApplication.UnicodeUTF8))
        self.connectBtn.setText(QtGui.QApplication.translate("MainWindow", "连接", None, QtGui.QApplication.UnicodeUTF8))
        self.scanBtn.setText(QtGui.QApplication.translate("MainWindow", "扫描蓝牙", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))

from view.BleListWidget import BleListWidget
