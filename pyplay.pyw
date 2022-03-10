# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os

from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound

soundList = []
for i in os.listdir("pyPlay/sounds"):
    if i != "readme.txt" and (i.endswith(".mp3") or i.endswith(".wav")):
        soundList.append(i)

chosenSounds = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(130, 40, 301, 191))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(soundList)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 250, 186, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 280, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.playSound)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def playSound(self):
        playsound("pyPlay/sounds/"+soundList[self.listWidget.currentRow()])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyPlay"))
        self.label.setText(_translate("MainWindow", "Select a sound you want to play."))
        self.pushButton.setText(_translate("MainWindow", "Play selected sound"))


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
