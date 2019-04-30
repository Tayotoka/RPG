import sys
import os
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
import xml.etree.ElementTree as etree
from gui.window import Ui_MainWindow
from gui.loginGui import Ui_loginWindow
from gui.signUpGui import Ui_SignUpWindow
from gui.gameWindow import Ui_gameWindow
from character import Player
from spawns import Mob, mobSpawn
from fight import battle


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Button functionality
        self.ui.btnNewGame.clicked.connect(self.newGame)
        self.ui.btnLoadGame.clicked.connect(self.loadGame)
        self.ui.btnOptions.clicked.connect(self.gameOptions)
        self.ui.btnExit.clicked.connect(lambda x: exit())

    def newGame(self):
        self.s = SignUpWindow()
        self.s.show()
        self.hide()

    def loadGame(self):
        self.l = LoginWindow()
        self.l.show()
        self.hide()

    def gameOptions(self):
        pass


class LoginWindow(Main):

    def __init__(self):
        super().__init__()
        self.loging = Ui_loginWindow()
        self.loging.setupUi(self)
        # button functionality:
        self.loging.btnLogin.clicked.connect(self.playerLogin)

    def playerLogin(self):
        users = 'Data/player/users.xml'
        # check if there are any current accounts
        if os.path.exists(users) is not True:
            msg = QMessageBox.warning(self, 'Error',
                                      'There are no current accounts',
                                      QMessageBox.Ok)
        else:
            # parse the existing accounts into memory
            xmlD = etree.parse(users)
            root = xmlD.getroot()
            # get login information
            playerUser = self.loging.yourUser.text()
            playerPass = self.loging.yourPass.text()
            # check if user/password match account
            for player in root.iter('User'):
                if player.attrib == {'userName': playerUser}:
                    if player[1].text == playerPass:
                        print('The login will work!')
                        self.g = gameWindow()
                        self.g.show()
                        self.hide()
                    else:
                        print('You entered a wrong username or password!')


class SignUpWindow(Main):

    def __init__(self):
        super().__init__()
        self.signing = Ui_SignUpWindow()
        self.signing.setupUi(self)
        # button functionality:
        self.signing.btnsignUp.clicked.connect(self.newAccount)

    def newAccount(self):
        # Check if xml database exists, or creates one
        users = 'Data/player/users.xml'
        if os.path.exists(users) is not True:
            tmp = open(users, 'a')
            tmp.write("<Player>\n</Player>")
            tmp.close()
        # Get data from XML file
        xmlD = etree.parse(users)
        root = xmlD.getroot()
        # write user data to xml file
        newUser = etree.SubElement(root, "User",
                                   attrib={"userName": self.signing.newUsername.text()})
        newUserName = etree.SubElement(newUser, "Username")
        newUserName.text = self.signing.newUsername.text()
        newUserPass = etree.SubElement(newUser, "Password")
        newUserPass.text = self.signing.newPassword.text()
        xmlD.write(users)
        self.l = LoginWindow()
        self.l.show()
        self.hide()


class gameWindow(Main):

    def __init__(self):
        super().__init__()
        self.gaming = Ui_gameWindow()
        self.gaming.setupUi(self)
        self.txtNumber = 0
        self.words = ['Welcome to the RPG game!', 'What would you like to do?',
                      'Please select from the following:']
        self.gaming.txtDisplay.setAlignment(QtCore.Qt.AlignVCenter)
        self.gaming.txtDisplay.append(self.words[self.txtNumber])
        # right button functionality
        self.gaming.btnRight.clicked.connect(self.newText)
        # left button functionality
        self.gaming.btnLeft.clicked.connect(self.removeText)

    def newText(self):
        if len(self.words) == self.txtNumber:
            pass
        else:
            text = self.gaming.txtDisplay
            text.clear()  # clears all current text
            text.append(self.words[self.txtNumber])
            self.txtNumber += 1
        # or use the text.append(words) without .toPlaintext()

    def removeText(self):
        if self.txtNumber - 1 < 0:
            pass
        else:
            self.txtNumber -= 1
            text = self.gaming.txtDisplay
            text.clear()
            text.append(self.words[self.txtNumber])
        # or use the text.append(words) without .toPlaintext()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
