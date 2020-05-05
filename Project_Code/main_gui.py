# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import pyaudio
from PyQt5 import QtCore, QtGui, QtWidgets
from music_studio import *
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(630, 0, 184, 128))
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
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(340, 180, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.bk_music = QtWidgets.QPushButton(self.centralwidget)
        self.bk_music.setGeometry(QtCore.QRect(340, 260, 151, 51))
        self.bk_music.setObjectName("bk_music")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 210, 317, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(530, 210, 281, 61))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(270, 150, 300, 61))
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.openedTabs = 0
        self.filePath1='images/drum_4.jpg'
        self.filePath1_2='sound_tracks/output.wav'
        self.filePath2='images/drum_3.jpg'
        self.filePath2_2='sound_tracks/O-Hi-Hat.wav'
        self.filePath3='images/drum_2.jpg'
        self.filePath3_2='sound_tracks/hi_hat.wav'
        self.filePath4='images/drum_1.jpg'
        self.filePath4_2='sound_tracks/snare.wav'
        self.filePath_bk_music=None
        self.record_path="records/output.wav"

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
        self.start.setText(_translate("MainWindow", "start"))
        self.bk_music.setText(_translate("MainWindow", "Background Music"))
        self.label_5.setText(_translate("MainWindow", "Select Input Device:"))
        self.label_6.setText(_translate("MainWindow", "Enter Record Name:"))
        self.error.setText(_translate("MainWindow", "TextLabel"))
        for i, device in enumerate(self.input_devices):
            self.comboBox_5.setItemText(i, _translate("MainWindow", device['name']))
        self.item_img_1.clicked.connect(self.on_click1_img)
        self.item_sound_1.clicked.connect(self.on_click1_sound)
        self.item_img_2.clicked.connect(self.on_click2_img)
        self.item_sound_2.clicked.connect(self.on_click2_sound)
        self.item_img_3.clicked.connect(self.on_click3_img)
        self.item_sound_3.clicked.connect(self.on_click3_sound)
        self.item_img_4.clicked.connect(self.on_click4_img)
        self.item_sound_4.clicked.connect(self.on_click4_sound)
        self.bk_music.clicked.connect(self.on_click_bk_music)
        self.start.clicked.connect(self.on_click)

        self.error.hide()

    def on_click1_img(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Image (*.png *.jpg)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath1 = fileDialog.selectedFiles()[0]
            
    
    def on_click1_sound(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Sound (*.wav *.mp3)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath1_2 = fileDialog.selectedFiles()[0]
                  

    def on_click2_img(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Image (*.png *.jpg)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath2 = fileDialog.selectedFiles()[0]
                      

    def on_click2_sound(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Sound (*.wav *.mp3)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath2_2 = fileDialog.selectedFiles()[0]
                    

    def on_click3_img(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Image (*.png *.jpg)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath3 = fileDialog.selectedFiles()[0]
                   

    def on_click3_sound(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Sound (*.wav *.mp3)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath3_2 = fileDialog.selectedFiles()[0]
             

    def on_click4_img(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Image (*.png *.jpg)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath4 = fileDialog.selectedFiles()[0]
            

    def on_click4_sound(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Sound (*.wav *.mp3)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath4_2 = fileDialog.selectedFiles()[0]
    

    def on_click_bk_music(self):
       
       fileDialog = QtWidgets.QFileDialog()
       fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
       fileDialog.setNameFilters(["Sound (*.wav *.mp3)", "Image (*.png *.jpg)"])
       fileDialog.selectNameFilter("Sound (*.wav *.mp3)")
       if fileDialog.exec_():
            self.openedTabs += 1
            self.filePath_bk_music = fileDialog.selectedFiles()[0]
    def on_click(self):
        if (self.filePath1==None) or (self.filePath1_2==None) or (self.filePath2==None) or (self.filePath2_2==None) or (self.filePath3==None) or (self.filePath3_2==None) or (self.filePath4==None) or (self.filePath4_2==None):
            self.error.setText("please select images/sound paths")
            self.error.setStyleSheet("color: red")
            self.error.show()
        else:
            music_data = [[ self.filePath1_2,self.filePath1, int(self.comboBox_1.currentIndex())],
                  [self.filePath2_2,self.filePath2, int(self.comboBox_2.currentIndex())],
                  [self.filePath3_2,self.filePath3, int(self.comboBox_3.currentIndex())],
                  [self.filePath4_2,self.filePath4, int(self.comboBox_4.currentIndex())]]
            background_music=self.filePath_bk_music
            device_name = str(self.comboBox_5.currentText())
            filename = self.plainTextEdit.toPlainText()
            if filename:
                self.record_path = "records/"+filename+".wav"
            music_studio = studio_main(music_data, background_music, device_name, self.record_path)
        if os.path.isfile(self.record_path):
            if not music_studio:
                self.outui = MediaPlayer(self.record_path)
                self.outui.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
