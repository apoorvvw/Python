# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ecegrid/a/ee364e10/ee364e10/Prelab10/calculator.ui'
#
# Created: Mon Mar 30 18:31:08 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 273)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 40, 92, 27))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(110, 40, 92, 27))
        self.btn8.setObjectName("btn8")
        self.btn5 = QtGui.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(110, 70, 92, 27))
        self.btn5.setObjectName("btn5")
        self.btn4 = QtGui.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 70, 92, 27))
        self.btn4.setObjectName("btn4")
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 100, 92, 27))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtGui.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(110, 100, 92, 27))
        self.btn2.setObjectName("btn2")
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(210, 40, 92, 27))
        self.btn9.setObjectName("btn9")
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(210, 70, 92, 27))
        self.btn6.setObjectName("btn6")
        self.btn3 = QtGui.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(210, 100, 92, 27))
        self.btn3.setObjectName("btn3")
        self.btnDiv = QtGui.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(310, 40, 92, 27))
        self.btnDiv.setObjectName("btnDiv")
        self.btnMul = QtGui.QPushButton(self.centralwidget)
        self.btnMul.setGeometry(QtCore.QRect(310, 70, 92, 27))
        self.btnMul.setObjectName("btnMul")
        self.btnMinus = QtGui.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(310, 100, 92, 27))
        self.btnMinus.setObjectName("btnMinus")
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(410, 40, 92, 51))
        self.btnClear.setObjectName("btnClear")
        self.btnDecimal = QtGui.QPushButton(self.centralwidget)
        self.btnDecimal.setGeometry(QtCore.QRect(210, 130, 92, 27))
        self.btnDecimal.setObjectName("btnDecimal")
        self.btn0 = QtGui.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(10, 130, 191, 27))
        self.btn0.setObjectName("btn0")
        self.btnPlus = QtGui.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(310, 130, 92, 27))
        self.btnPlus.setObjectName("btnPlus")
        self.btnResult = QtGui.QPushButton(self.centralwidget)
        self.btnResult.setGeometry(QtCore.QRect(410, 100, 92, 51))
        self.btnResult.setObjectName("btnResult")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 6, 491, 31))
        self.lineEdit.setMaxLength(200)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 481, 41))
        self.groupBox.setStyleSheet("border: 1px solid gray;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.label.setStyleSheet("border: none;")
        self.label.setObjectName("label")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(240, 10, 221, 22))
        self.checkBox.setStyleSheet("border: none;")
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(110, 10, 41, 16))
        self.spinBox.setStyleSheet("border:2pxSolid Grey")
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.btn8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.btn5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.btn4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btn9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.btn6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.btn3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDiv.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMul.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMinus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDecimal.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.btn0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btnResult.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "0.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Decimal Digits", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Display Thousand\'s Seperator", None, QtGui.QApplication.UnicodeUTF8))

