# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(812, 738)
        loginWindow.setStyleSheet("background: white;\n"
"font: 24px;")
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setStyleSheet("text-align: center;")
        self.userLabel.setObjectName("userLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userLabel)
        self.yourUser = QtWidgets.QLineEdit(self.centralwidget)
        self.yourUser.setObjectName("yourUser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yourUser)
        self.PassLabel = QtWidgets.QLabel(self.centralwidget)
        self.PassLabel.setObjectName("PassLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PassLabel)
        self.yourPass = QtWidgets.QLineEdit(self.centralwidget)
        self.yourPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yourPass.setObjectName("yourPass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yourPass)
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setStyleSheet("background: lightgrey;\n"
"")
        self.btnLogin.setObjectName("btnLogin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.btnLogin)
        self.gridLayout.addLayout(self.formLayout, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 4)
        self.btnBacktoMain = QtWidgets.QPushButton(self.centralwidget)
        self.btnBacktoMain.setMinimumSize(QtCore.QSize(100, 28))
        self.btnBacktoMain.setMaximumSize(QtCore.QSize(133, 38))
        self.btnBacktoMain.setStyleSheet("background: lightgrey;")
        self.btnBacktoMain.setObjectName("btnBacktoMain")
        self.gridLayout.addWidget(self.btnBacktoMain, 0, 0, 1, 1)
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.userLabel.setText(_translate("loginWindow", "Username"))
        self.PassLabel.setText(_translate("loginWindow", "Password"))
        self.btnLogin.setText(_translate("loginWindow", "Login"))
        self.textBrowser.setHtml(_translate("loginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Please enter  your username</span></p></body></html>"))
        self.btnBacktoMain.setText(_translate("loginWindow", "Back"))

