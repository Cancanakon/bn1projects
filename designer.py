# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/90531/Desktop/bn1projects/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(730, 533)
        frmMain.setMinimumSize(QtCore.QSize(600, 400))
        frmMain.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        frmMain.setFont(font)
        self.btnUpdate = QtWidgets.QPushButton(frmMain)
        self.btnUpdate.setGeometry(QtCore.QRect(270, 460, 111, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("updt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon)
        self.btnUpdate.setIconSize(QtCore.QSize(32, 32))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnAll = QtWidgets.QPushButton(frmMain)
        self.btnAll.setGeometry(QtCore.QRect(390, 460, 151, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("eq1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAll.setIcon(icon1)
        self.btnAll.setIconSize(QtCore.QSize(32, 32))
        self.btnAll.setObjectName("btnAll")
        self.btnExt = QtWidgets.QPushButton(frmMain)
        self.btnExt.setGeometry(QtCore.QRect(10, 480, 88, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnExt.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ext.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExt.setIcon(icon2)
        self.btnExt.setIconSize(QtCore.QSize(32, 32))
        self.btnExt.setObjectName("btnExt")
        self.btnDanger = QtWidgets.QPushButton(frmMain)
        self.btnDanger.setGeometry(QtCore.QRect(550, 460, 121, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("thunder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDanger.setIcon(icon3)
        self.btnDanger.setIconSize(QtCore.QSize(32, 32))
        self.btnDanger.setObjectName("btnDanger")
        self.lblBlck = QtWidgets.QLabel(frmMain)
        self.lblBlck.setGeometry(QtCore.QRect(220, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lblBlck.setFont(font)
        self.lblBlck.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBlck.setObjectName("lblBlck")
        self.lndtDeger = QtWidgets.QLineEdit(frmMain)
        self.lndtDeger.setGeometry(QtCore.QRect(120, 380, 113, 25))
        self.lndtDeger.setObjectName("lndtDeger")
        self.lndtSehir = QtWidgets.QLineEdit(frmMain)
        self.lndtSehir.setGeometry(QtCore.QRect(120, 410, 113, 25))
        self.lndtSehir.setObjectName("lndtSehir")
        self.label = QtWidgets.QLabel(frmMain)
        self.label.setGeometry(QtCore.QRect(30, 380, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmMain)
        self.label_2.setGeometry(QtCore.QRect(50, 410, 61, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtBrowser = QtWidgets.QTextBrowser(frmMain)
        self.txtBrowser.setGeometry(QtCore.QRect(20, 40, 701, 331))
        self.txtBrowser.setObjectName("txtBrowser")
        self.cbSehir = QtWidgets.QComboBox(frmMain)
        self.cbSehir.setGeometry(QtCore.QRect(350, 390, 241, 31))
        self.cbSehir.setObjectName("cbSehir")

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "Anasayfa"))
        self.btnUpdate.setText(_translate("frmMain", "Güncelle"))
        self.btnUpdate.setShortcut(_translate("frmMain", "Ctrl+U"))
        self.btnAll.setText(_translate("frmMain", "Bütün \n"
"Depremler"))
        self.btnAll.setShortcut(_translate("frmMain", "Ctrl+A"))
        self.btnExt.setText(_translate("frmMain", "Çıkış"))
        self.btnExt.setShortcut(_translate("frmMain", "Ctrl+Q"))
        self.btnDanger.setText(_translate("frmMain", "Yıkıcı \n"
"Boyut"))
        self.btnDanger.setShortcut(_translate("frmMain", "Ctrl+D"))
        self.lblBlck.setText(_translate("frmMain", "BLACKNIGHT"))
        self.label.setText(_translate("frmMain", "Büyüklük:"))
        self.label_2.setText(_translate("frmMain", "Vilayet:"))

