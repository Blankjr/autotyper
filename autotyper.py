# -*- coding: utf-8 -*-
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from RandomWordGenerator import RandomWord
import randomword
import keyboard
import windowsapps
import os
import subprocess
import pydirectinput


class Ui_MainWindow(object):
    stopped = False

    def __init__(self):
        self.timer_time = QtCore.QTime(0, 0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(666, 380)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono PL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(360, 230, 291, 111))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(self.typing)

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 651, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.timeEdit_setTimer = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_setTimer.setGeometry(QtCore.QRect(360, 120, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono PL SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit_setTimer.setFont(font)
        self.timeEdit_setTimer.setObjectName("timeEdit_setTimer")
        #self.timer_time = QtCore.QTime(0, 30)
        self.timeEdit_setTimer.setTime(self.timer_time)
        # print(timer_time.toString())

        self.label_title_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_title_2.setGeometry(QtCore.QRect(10, 110, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 90, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono PL SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono PL SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Productivity_Booster"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_title.setText(_translate("MainWindow", "AutoTyper"))
        self.label_title_2.setText(_translate("MainWindow", "Set Timer:"))
        self.label.setText(_translate("MainWindow", "Hours:Minutes"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p>Hold <span style=\" color:#ff0000;\">Q</span> Key to </p><p><span style=\" color:#ff0000;\">quit</span> typing early</p></body></html>"))

    def getTimerValues(self):
        # print(self.timeEdit_setStartDelay.time)
        time = QtCore.QTime()
        curent_t = time.currentTime()
        print(curent_t.toString())

    def stop_typing(self):
        stopped = True

    def typing(self):
        # os.system('notepad')
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
        counterTime = self.timeEdit_setTimer.time().toString()
        times = counterTime.split(':')
        print(times)
        counter = (int(times[0])*60 + int(times[1])) * 30  # 0.5 seconds
        print("Timer Set to :", counter/120, "minutes")
        keypressed = False
        while counter > 0 and not keypressed:
            counter -= 1
            print(counter)
            if keyboard.is_pressed('q'):
                keypressed = True
                print("quit typing")
            else:
                generated_word = randomword.get_random_word()
                for letter in generated_word:
                    pydirectinput.keyDown(letter)
                    pydirectinput.keyUp(letter)
                pydirectinput.keyDown('space')
                pydirectinput.keyUp('space')
                print(generated_word)
                time.sleep(0.4)
        subprocess.call(["taskkill", "/F", "/IM", "notepad.exe"])

        """needs multi threading to close typing process if stop is clicked and to not freeze ui
        """
        # rw = RandomWord(max_word_size=5)
        # print(rw.generate())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui.getTimerValues()

    # ui.typing()
    sys.exit(app.exec_())
