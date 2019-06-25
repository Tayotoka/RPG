# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionsMain(object):
    def setupUi(self, optionsMain):
        optionsMain.setObjectName("optionsMain")
        optionsMain.resize(400, 300)
        optionsMain.setStyleSheet("background: black;")
        self.gridLayout_2 = QtWidgets.QGridLayout(optionsMain)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSave = QtWidgets.QPushButton(optionsMain)
        self.btnSave.setStyleSheet("background: #a6c5ea;")
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.btnQuit = QtWidgets.QPushButton(optionsMain)
        self.btnQuit.setStyleSheet("background: #a6c5ea;")
        self.btnQuit.setObjectName("btnQuit")
        self.gridLayout.addWidget(self.btnQuit, 1, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(optionsMain)
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(optionsMain)
        self.textEdit_2.setStyleSheet("color: white;")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(optionsMain)
        QtCore.QMetaObject.connectSlotsByName(optionsMain)

    def retranslateUi(self, optionsMain):
        _translate = QtCore.QCoreApplication.translate
        optionsMain.setWindowTitle(_translate("optionsMain", "Options"))
        self.btnSave.setText(_translate("optionsMain", "Save"))
        self.btnQuit.setText(_translate("optionsMain", "Quit"))
        self.textEdit.setHtml(_translate("optionsMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Would you like to Save?</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("optionsMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Would you like to exit the game?</p></body></html>"))

