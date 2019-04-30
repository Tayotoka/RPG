# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 703)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("font: 24px;\n"
"background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnNewGame = QtWidgets.QPushButton(self.centralwidget)
        self.btnNewGame.setStyleSheet("background-color: #b8b9ba;\n"
"color: #bc090f;")
        self.btnNewGame.setObjectName("btnNewGame")
        self.gridLayout.addWidget(self.btnNewGame, 1, 1, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setStyleSheet("background-color: #b8b9ba;\n"
"color: #bc090f;")
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 4, 1, 1, 1)
        self.btnLoadGame = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadGame.setStyleSheet("background-color: #b8b9ba;\n"
"color: #bc090f;")
        self.btnLoadGame.setObjectName("btnLoadGame")
        self.gridLayout.addWidget(self.btnLoadGame, 2, 1, 1, 1)
        self.btnOptions = QtWidgets.QPushButton(self.centralwidget)
        self.btnOptions.setStyleSheet("background-color: #b8b9ba;\n"
"color: #bc090f;")
        self.btnOptions.setObjectName("btnOptions")
        self.gridLayout.addWidget(self.btnOptions, 3, 1, 1, 1)
        self.mainTxtWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.mainTxtWindow.setStyleSheet("border: none;")
        self.mainTxtWindow.setObjectName("mainTxtWindow")
        self.gridLayout.addWidget(self.mainTxtWindow, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnNewGame.setText(_translate("MainWindow", "New Game"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnLoadGame.setText(_translate("MainWindow", "Load Game"))
        self.btnOptions.setText(_translate("MainWindow", "Options"))
        self.mainTxtWindow.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:36pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Welcome to the RPG!</span></p></body></html>"))

