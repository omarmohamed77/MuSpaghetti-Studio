# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import pyaudio
import timeit
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QMessageBox
from music_studio import studio_main
from MediaPlayer import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(820, 514)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(820, 514))
        MainWindow.setMaximumSize(QtCore.QSize(820, 514))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 184, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.item1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.item1.setContentsMargins(0, 0, 0, 0)
        self.item1.setObjectName("item1")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.item1.addWidget(self.label)
        self.item_img_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.item_img_1.setObjectName("item_img_1")
        self.item1.addWidget(self.item_img_1)
        self.item_sound_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.item_sound_1.setObjectName("item_sound_1")
        self.item1.addWidget(self.item_sound_1)
        self.comboBox_1 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.item1.addWidget(self.comboBox_1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(630, 10, 184, 128))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.item1_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.item1_2.setContentsMargins(0, 0, 0, 0)
        self.item1_2.setObjectName("item1_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.item1_2.addWidget(self.label_2)
        self.item_img_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.item_img_2.setObjectName("item_img_2")
        self.item1_2.addWidget(self.item_img_2)
        self.item_sound_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.item_sound_2.setObjectName("item_sound_2")
        self.item1_2.addWidget(self.item_sound_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.item1_2.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 350, 184, 128))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.item1_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.item1_3.setContentsMargins(0, 0, 0, 0)
        self.item1_3.setObjectName("item1_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.item1_3.addWidget(self.label_3)
        self.item_img_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.item_img_3.setObjectName("item_img_3")
        self.item1_3.addWidget(self.item_img_3)
        self.item_sound_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.item_sound_3.setObjectName("item_sound_3")
        self.item1_3.addWidget(self.item_sound_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.item1_3.addWidget(self.comboBox_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(630, 350, 184, 128))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.item1_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.item1_4.setContentsMargins(0, 0, 0, 0)
        self.item1_4.setObjectName("item1_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.item1_4.addWidget(self.label_4)
        self.item_img_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.item_img_4.setObjectName("item_img_4")
        self.item1_4.addWidget(self.item_img_4)
        self.item_sound_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.item_sound_4.setObjectName("item_sound_4")
        self.item1_4.addWidget(self.item_sound_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.item1_4.addWidget(self.comboBox_4)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(235, 50, 351, 51))
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setText("")
        self.error.setObjectName("error")
        self.error.setStyleSheet("color: red")
        self.record_name = QtWidgets.QTextEdit(self.centralwidget)
        self.record_name.setGeometry(QtCore.QRect(285, 160, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.record_name.setFont(font)
        self.record_name.setOverwriteMode(True)
        self.record_name.setObjectName("record_name")
        self.record_name.setAlignment(QtCore.Qt.AlignCenter)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(285, 200, 250, 140))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(250, 140))
        self.splitter.setMaximumSize(QtCore.QSize(250, 140))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.comboBox_5 = QtWidgets.QComboBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(250, 31))
        self.comboBox_5.setMaximumSize(QtCore.QSize(250, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.start = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMinimumSize(QtCore.QSize(250, 62))
        self.start.setMaximumSize(QtCore.QSize(250, 62))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.playback_button = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playback_button.sizePolicy().hasHeightForWidth())
        self.playback_button.setSizePolicy(sizePolicy)
        self.playback_button.setMinimumSize(QtCore.QSize(250, 35))
        self.playback_button.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playback_button.setFont(font)
        self.playback_button.setObjectName("playback_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        pyaudio_instance = pyaudio.PyAudio()
        self.input_devices = []
        for i in range(pyaudio_instance.get_device_count()):
            dev = pyaudio_instance.get_device_info_by_index(i)
            if (dev['hostApi'] == 0 and dev['maxOutputChannels'] == 0):
                self.input_devices.append(dev)
                self.comboBox_5.addItem("")
        
        self.messageBox = QMessageBox()
        self.messageBox.setIcon(QMessageBox.Question)
        self.messageBox.setWindowTitle('MusicWindow')
        self.messageBox.setText('Add Background Music?')
        self.messageBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        self.skipButton = self.messageBox.addButton('Skip', QMessageBox.NoRole)
        self.closeButton = self.messageBox.addButton(QMessageBox.Close)
        self.messageBox.setDefaultButton(self.skipButton)
        self.closeButton.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.soundPaths = [None for i in range(4)]
        self.imagePaths = [None for i in range(4)]
        
        if os.path.isdir("images"):
            for i, filename in enumerate(os.listdir("images")[:4]):
                if filename.endswith(".png") or filename.endswith(".jpg"): 
                    self.imagePaths[i]='images/'+filename
        
        if os.path.isdir("sound_tracks"):
            for j, filename in enumerate(os.listdir("sound_tracks")[:4]):
                if filename.endswith(".wav"): 
                    self.soundPaths[j]='sound_tracks/'+filename
                    
        if not os.path.isdir("records"):
            os.mkdir("records")
        
        self.comboBoxes = [self.comboBox_1, self.comboBox_2,
                           self.comboBox_3, self.comboBox_4]
        self.filePath_bk_music=None
        self.record_path=None
        self.playback_button.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "          intrument 1"))
        self.item_img_1.setText(_translate("MainWindow", " image"))
        self.item_sound_1.setText(_translate("MainWindow", "sound"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "on hit"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "pause/resume"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "on/off"))
        self.label_2.setText(_translate("MainWindow", "          intrument 2"))
        self.item_img_2.setText(_translate("MainWindow", " image"))
        self.item_sound_2.setText(_translate("MainWindow", "sound"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "on hit"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "pause/resume"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "on/off"))
        self.label_3.setText(_translate("MainWindow", "          intrument 3"))
        self.item_img_3.setText(_translate("MainWindow", " image"))
        self.item_sound_3.setText(_translate("MainWindow", "sound"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "on hit"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "pause/resume"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "on/off"))
        self.label_4.setText(_translate("MainWindow", "          intrument 4"))
        self.item_img_4.setText(_translate("MainWindow", " image"))
        self.item_sound_4.setText(_translate("MainWindow", "sound"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "on hit"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "pause/resume"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "on/off"))
        self.record_name.setPlaceholderText(_translate("MainWindow", "               record name"))
        self.comboBox_5.setToolTip(_translate("MainWindow", "Select Input Device"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.playback_button.setText(_translate("MainWindow", "PlayBack"))
        for i, device in enumerate(self.input_devices):
            self.comboBox_5.setItemText(i, _translate("MainWindow", device['name']))
        self.record_name.textChanged.connect(self.palyback_setEnabled)
        self.item_img_1.clicked.connect(self.on_click1_img)
        self.item_sound_1.clicked.connect(self.on_click1_sound)
        self.item_img_2.clicked.connect(self.on_click2_img)
        self.item_sound_2.clicked.connect(self.on_click2_sound)
        self.item_img_3.clicked.connect(self.on_click3_img)
        self.item_sound_3.clicked.connect(self.on_click3_sound)
        self.item_img_4.clicked.connect(self.on_click4_img)
        self.item_sound_4.clicked.connect(self.on_click4_sound)
        self.start.clicked.connect(self.on_click)
        self.playback_button.clicked.connect(self.run_playback)
        
    def palyback_setEnabled(self):
        self.record_path = "records/"+self.record_name.toPlainText()+".wav"
        if os.path.isfile(self.record_path):
            self.playback_button.setEnabled(True)
        else:
            self.playback_button.setEnabled(False)
            
    def run_playback(self):
        if os.path.isfile(self.record_path):
            self.outui = MediaPlayer(self.record_path)
            self.outui.show()
        else:
            self.playback_button.setEnabled(False)
        
    def on_click1_img(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Image (*.png *.jpg)"])
        if fileDialog.exec_():
            self.imagePaths[0] = fileDialog.selectedFiles()[0]
            
    def on_click1_sound(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Sound (*.wav)"])
        if fileDialog.exec_():
            self.soundPaths[0] = fileDialog.selectedFiles()[0]
            
    def on_click2_img(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Image (*.png *.jpg)"])
        if fileDialog.exec_():
            self.imagePaths[1] = fileDialog.selectedFiles()[0]
            
    def on_click2_sound(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Sound (*.wav)"])
        if fileDialog.exec_():
            self.soundPaths[1] = fileDialog.selectedFiles()[0]
            
    def on_click3_img(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Image (*.png *.jpg)"])
        if fileDialog.exec_():
            self.imagePaths[2] = fileDialog.selectedFiles()[0]
            
    def on_click3_sound(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Sound (*.wav)"])
        if fileDialog.exec_():
            self.soundPaths[2] = fileDialog.selectedFiles()[0]
            
    def on_click4_img(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Image (*.png *.jpg)"])
        if fileDialog.exec_():
            self.imagePaths[3] = fileDialog.selectedFiles()[0]
            
    def on_click4_sound(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Sound (*.wav)"])
        if fileDialog.exec_():
            self.soundPaths[3] = fileDialog.selectedFiles()[0]
            
    def setFade(self, widget, flag):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(3000)
        self.animation.setStartValue(flag)
        self.animation.setEndValue(not flag)
        self.animation.start()
    
    def on_click_bk_music(self):
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        fileDialog.setNameFilters(["Sound (*.wav *.mp3)"])
        if fileDialog.exec_():
            self.filePath_bk_music = fileDialog.selectedFiles()[0]
            
    def display_error(self, error_message):
        self.error.setText(error_message)
        self.setFade(self.error, 0)
        self.setFade(self.error, 1)
            
    def on_click(self):
        if (None in self.imagePaths or None in self.soundPaths):
            self.display_error("Please select images/sound paths")
        elif not self.record_name.toPlainText():
            self.display_error("Please enter record name")
        else:
            reply = self.messageBox.exec_()
            if reply == QMessageBox.Yes:
                self.on_click_bk_music()
            elif reply == QMessageBox.No:
                self.filePath_bk_music=None
            if reply != QMessageBox.Close:
                music_data = []
                for i in range(4):
                    music_data.append([self.soundPaths[i], self.imagePaths[i], int(self.comboBoxes[i].currentIndex())])
                background_music=self.filePath_bk_music
                device_name = None
                if self.comboBox_5.count() > 0:
                    device_name = str(self.comboBox_5.currentText())
                filename = self.record_name.toPlainText()
                self.record_path = "records/"+filename+".wav"
                music_studio = studio_main(music_data, background_music, device_name, self.record_path)
                if os.path.isfile(self.record_path):
                    if music_studio:
                        self.outui = MediaPlayer(self.record_path)
                        self.outui.show()
                        if not self.playback_button.isEnabled():
                            self.playback_button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
