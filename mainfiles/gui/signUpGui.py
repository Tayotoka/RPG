# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(805, 683)
        SignUpWindow.setStyleSheet("background: white;\n"
"font: 24px;")
        self.centralwidget = QtWidgets.QWidget(SignUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.newUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.newUsername.setObjectName("newUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.newUsername)
        self.newPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.newPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword.setObjectName("newPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.newPassword)
        self.btnsignUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnsignUp.setStyleSheet("background: lightgrey")
        self.btnsignUp.setObjectName("btnsignUp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnsignUp)
        self.gridLayout.addLayout(self.formLayout, 4, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.btnBacktoMain = QtWidgets.QPushButton(self.centralwidget)
        self.btnBacktoMain.setMinimumSize(QtCore.QSize(100, 28))
        self.btnBacktoMain.setMaximumSize(QtCore.QSize(133, 30))
        self.btnBacktoMain.setStyleSheet("background: lightgrey;\n"
"")
        self.btnBacktoMain.setObjectName("btnBacktoMain")
        self.gridLayout.addWidget(self.btnBacktoMain, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        SignUpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SignUpWindow)
        self.statusbar.setObjectName("statusbar")
        SignUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "MainWindow"))
        self.label_2.setText(_translate("SignUpWindow", "Password"))
        self.label.setText(_translate("SignUpWindow", "UserName"))
        self.btnsignUp.setText(_translate("SignUpWindow", "SignUp"))
        self.textBrowser.setHtml(_translate("SignUpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:24;\">Please enter a username and password!</span></p></body></html>"))
        self.btnBacktoMain.setText(_translate("SignUpWindow", "Back"))

