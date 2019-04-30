# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gameWindow(object):
    def setupUi(self, gameWindow):
        gameWindow.setObjectName("gameWindow")
        gameWindow.resize(800, 600)
        gameWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(gameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnBackpack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackpack.setStyleSheet("background: #a6c5ea;")
        self.btnBackpack.setObjectName("btnBackpack")
        self.gridLayout.addWidget(self.btnBackpack, 5, 5, 1, 1)
        self.btnYes = QtWidgets.QPushButton(self.centralwidget)
        self.btnYes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnYes.setStyleSheet("background: #a6c5ea;")
        self.btnYes.setObjectName("btnYes")
        self.gridLayout.addWidget(self.btnYes, 2, 0, 1, 1)
        self.btnNo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnNo.setStyleSheet("background: #a6c5ea")
        self.btnNo.setObjectName("btnNo")
        self.gridLayout.addWidget(self.btnNo, 5, 0, 1, 1)
        self.btnUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnUp.setStyleSheet("background: lightgrey;")
        self.btnUp.setObjectName("btnUp")
        self.gridLayout.addWidget(self.btnUp, 2, 2, 1, 2)
        self.btnDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnDown.setStyleSheet("background: lightgrey;")
        self.btnDown.setObjectName("btnDown")
        self.gridLayout.addWidget(self.btnDown, 6, 2, 1, 2)
        self.btnRight = QtWidgets.QPushButton(self.centralwidget)
        self.btnRight.setStyleSheet("background: lightgrey;")
        self.btnRight.setObjectName("btnRight")
        self.gridLayout.addWidget(self.btnRight, 5, 3, 1, 2)
        self.btnLeft = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeft.setStyleSheet("background: lightgrey;")
        self.btnLeft.setObjectName("btnLeft")
        self.gridLayout.addWidget(self.btnLeft, 5, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.btnCharacter = QtWidgets.QPushButton(self.centralwidget)
        self.btnCharacter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCharacter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCharacter.setStyleSheet("background: #a6c5ea;")
        self.btnCharacter.setObjectName("btnCharacter")
        self.gridLayout.addWidget(self.btnCharacter, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 5, 1, 1)
        self.txtDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDisplay.setStyleSheet("color: white;")
        self.txtDisplay.setReadOnly(True)
        self.txtDisplay.setObjectName("txtDisplay")
        self.gridLayout.addWidget(self.txtDisplay, 1, 0, 1, 6)
        self.btnGameOptions = QtWidgets.QPushButton(self.centralwidget)
        self.btnGameOptions.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnGameOptions.setStyleSheet("background:  #a6c5ea;")
        self.btnGameOptions.setObjectName("btnGameOptions")
        self.gridLayout.addWidget(self.btnGameOptions, 0, 0, 1, 1)
        gameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        gameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(gameWindow)
        self.statusbar.setObjectName("statusbar")
        gameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(gameWindow)
        QtCore.QMetaObject.connectSlotsByName(gameWindow)

    def retranslateUi(self, gameWindow):
        _translate = QtCore.QCoreApplication.translate
        gameWindow.setWindowTitle(_translate("gameWindow", "MainWindow"))
        self.btnBackpack.setText(_translate("gameWindow", "Backpack"))
        self.btnYes.setText(_translate("gameWindow", "Yes"))
        self.btnNo.setText(_translate("gameWindow", "No"))
        self.btnUp.setText(_translate("gameWindow", "Up"))
        self.btnDown.setText(_translate("gameWindow", "Down"))
        self.btnRight.setText(_translate("gameWindow", "Right"))
        self.btnLeft.setText(_translate("gameWindow", "Left"))
        self.btnCharacter.setText(_translate("gameWindow", "Character"))
        self.txtDisplay.setHtml(_translate("gameWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnGameOptions.setText(_translate("gameWindow", "Options"))

