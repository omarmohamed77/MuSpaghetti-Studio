# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MediaPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QBasicTimer

class MediaPlayer(QtWidgets.QWidget):

    def __init__(self, filename):
        super().__init__()
        self.setObjectName("MediaPlayer")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(520, 140)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(520, 140))
        self.setMaximumSize(QtCore.QSize(520, 140))
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 15, 480, 120))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.play_button = QtWidgets.QPushButton(self.layoutWidget)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_3.addWidget(self.play_button)
        self.pause_button = QtWidgets.QPushButton(self.layoutWidget)
        self.pause_button.setObjectName("pause_button")
        self.horizontalLayout_3.addWidget(self.pause_button)
        self.stop_button = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_3.addWidget(self.stop_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.delete_button = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mute_button = QtWidgets.QPushButton(self.layoutWidget)
        self.mute_button.setObjectName("mute_button")
        self.horizontalLayout_2.addWidget(self.mute_button)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.volume_level = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.volume_level.setFont(font)
        self.volume_level.setObjectName("volume_level")
        self.horizontalLayout_2.addWidget(self.volume_level)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        
        self.recordPath = filename
        url = QtCore.QUrl.fromLocalFile(self.recordPath)
        content = QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(50)
        
        self.timer = QBasicTimer()
        self.step = 0
        
        self.setWindowTitle("MediaPlayer")
        self.play_button.setText("Play")
        self.pause_button.setText("Pause")
        self.stop_button.setText("Stop")
        self.delete_button.setText("Delete")
        self.mute_button.setText("Mute")
        self.volume_level.setText("50 %")
        self.play_button.clicked.connect(self.media_play)
        self.pause_button.clicked.connect(self.media_pause)
        self.stop_button.clicked.connect(self.media_stop)
        self.mute_button.clicked.connect(self.media_setMuted)
        self.horizontalSlider.valueChanged.connect(self.media_setVolume)
        self.delete_button.clicked.connect(self.media_delete)
        
        
    def media_play(self):
        if self.player.state() != 1:
            self.player.play()
            if not self.timer.isActive():
                self.timer.start(round(self.player.duration()/100), self)
        
    def media_pause(self):
        if self.player.state() != 2:
            self.player.pause()
            if self.timer.isActive():
                self.timer.stop()
                self.play_button.setText("Resume")
            
    def media_stop(self):
        if self.player.state() != 0:
            self.player.stop()
            if self.timer.isActive():
                self.timer.stop()
            self.step = 0
            self.progressBar.setValue(0)
            self.play_button.setText("Play")
        
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.step = 0
            if self.play_button.text() != "Play":
                self.play_button.setText("Play")
            return
        
        self.step +=1
        self.progressBar.setValue(self.step)
        
    def media_setMuted(self):
        if self.mute_button.text() == "Mute":
            self.player.setMuted(True)
            self.mute_button.setText("Unmute")
        elif self.mute_button.text() == "Unmute":
            self.player.setMuted(False)
            self.mute_button.setText("Mute")
            
    def media_setVolume(self):
        self.player.setVolume(self.horizontalSlider.value())
        self.volume_level.setText(str(self.horizontalSlider.value())+" %")

    def media_delete(self):
        if os.path.isfile(self.recordPath):
            os.remove(self.recordPath)
            self.close()
            
    def closeEvent(self, event):
        if self.player.state() != 0:
            self.player.stop()
        if self.timer.isActive():
            self.timer.stop()
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    filename="./records/output.wav"
    ui = MediaPlayer(filename)
    ui.show()
    sys.exit(app.exec_())
