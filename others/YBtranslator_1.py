# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Works\YouBridge\YBtranslator\YBtranslator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 829)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video_id = QtWidgets.QLabel(self.centralwidget)
        self.video_id.setGeometry(QtCore.QRect(40, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.video_id.setFont(font)
        self.video_id.setObjectName("video_id")
        self.mainornot = QtWidgets.QCheckBox(self.centralwidget)
        self.mainornot.setGeometry(QtCore.QRect(450, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mainornot.setFont(font)
        self.mainornot.setObjectName("mainornot")
        self.lang_choice = QtWidgets.QComboBox(self.centralwidget)
        self.lang_choice.setGeometry(QtCore.QRect(150, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lang_choice.setFont(font)
        self.lang_choice.setObjectName("lang_choice")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title_con = QtWidgets.QTextEdit(self.centralwidget)
        self.title_con.setGeometry(QtCore.QRect(150, 160, 541, 41))
        self.title_con.setObjectName("title_con")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(40, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.video_id_con = QtWidgets.QLineEdit(self.centralwidget)
        self.video_id_con.setGeometry(QtCore.QRect(150, 20, 541, 41))
        self.video_id_con.setObjectName("video_id_con")
        self.desc_con = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.desc_con.setGeometry(QtCore.QRect(150, 230, 541, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.desc_con.setFont(font)
        self.desc_con.setBackgroundVisible(False)
        self.desc_con.setCenterOnScroll(False)
        self.desc_con.setObjectName("desc_con")
        self.keywords = QtWidgets.QLabel(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(30, 420, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.keywords.setFont(font)
        self.keywords.setObjectName("keywords")
        self.key_con = QtWidgets.QTextEdit(self.centralwidget)
        self.key_con.setGeometry(QtCore.QRect(150, 420, 541, 41))
        self.key_con.setObjectName("key_con")
        self.srt_file = QtWidgets.QLabel(self.centralwidget)
        self.srt_file.setGeometry(QtCore.QRect(20, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.srt_file.setFont(font)
        self.srt_file.setObjectName("srt_file")
        self.srt_file_con = QtWidgets.QTextEdit(self.centralwidget)
        self.srt_file_con.setGeometry(QtCore.QRect(150, 490, 361, 41))
        self.srt_file_con.setObjectName("srt_file_con")
        self.choicesrt_button = QtWidgets.QPushButton(self.centralwidget)
        self.choicesrt_button.setGeometry(QtCore.QRect(520, 490, 171, 41))
        self.choicesrt_button.setObjectName("choicesrt_button")
        self.audio_file_con = QtWidgets.QTextEdit(self.centralwidget)
        self.audio_file_con.setGeometry(QtCore.QRect(150, 560, 361, 41))
        self.audio_file_con.setObjectName("audio_file_con")
        self.choiceaudio_button_ = QtWidgets.QPushButton(self.centralwidget)
        self.choiceaudio_button_.setGeometry(QtCore.QRect(520, 560, 171, 41))
        self.choiceaudio_button_.setObjectName("choiceaudio_button_")
        self.audio_file = QtWidgets.QLabel(self.centralwidget)
        self.audio_file.setGeometry(QtCore.QRect(20, 560, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_file.setFont(font)
        self.audio_file.setObjectName("audio_file")
        self.language = QtWidgets.QLabel(self.centralwidget)
        self.language.setGeometry(QtCore.QRect(40, 90, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.language.setFont(font)
        self.language.setObjectName("language")
        self.audio_choice = QtWidgets.QComboBox(self.centralwidget)
        self.audio_choice.setGeometry(QtCore.QRect(150, 630, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_choice.setFont(font)
        self.audio_choice.setObjectName("audio_choice")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.audio_type = QtWidgets.QLabel(self.centralwidget)
        self.audio_type.setGeometry(QtCore.QRect(20, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_type.setFont(font)
        self.audio_type.setObjectName("audio_type")
        self.synthetise = QtWidgets.QPushButton(self.centralwidget)
        self.synthetise.setGeometry(QtCore.QRect(280, 710, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.synthetise.setFont(font)
        self.synthetise.setObjectName("synthetise")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.video_id.setText(_translate("MainWindow", "视频ID"))
        self.mainornot.setText(_translate("MainWindow", "指定为主要语言"))
        self.lang_choice.setItemText(0, _translate("MainWindow", "英语en (默认)"))
        self.lang_choice.setItemText(1, _translate("MainWindow", "韩语kor"))
        self.lang_choice.setItemText(2, _translate("MainWindow", "泰语th"))
        self.lang_choice.setItemText(3, _translate("MainWindow", "葡萄牙语pt"))
        self.lang_choice.setItemText(4, _translate("MainWindow", "希腊语el"))
        self.lang_choice.setItemText(5, _translate("MainWindow", "保加利亚语bul"))
        self.lang_choice.setItemText(6, _translate("MainWindow", "芬兰语fin"))
        self.lang_choice.setItemText(7, _translate("MainWindow", "斯洛文尼亚slo"))
        self.lang_choice.setItemText(8, _translate("MainWindow", "法语fra"))
        self.lang_choice.setItemText(9, _translate("MainWindow", "阿拉伯语ara"))
        self.lang_choice.setItemText(10, _translate("MainWindow", "德语de"))
        self.lang_choice.setItemText(11, _translate("MainWindow", "荷兰语nl"))
        self.lang_choice.setItemText(12, _translate("MainWindow", "爱沙尼亚语est"))
        self.lang_choice.setItemText(13, _translate("MainWindow", "捷克语cs"))
        self.lang_choice.setItemText(14, _translate("MainWindow", "瑞典语swe"))
        self.lang_choice.setItemText(15, _translate("MainWindow", "越南语vie"))
        self.lang_choice.setItemText(16, _translate("MainWindow", "日语jp"))
        self.lang_choice.setItemText(17, _translate("MainWindow", "西班牙语spa"))
        self.lang_choice.setItemText(18, _translate("MainWindow", "俄语ru"))
        self.lang_choice.setItemText(19, _translate("MainWindow", "意大利语it"))
        self.lang_choice.setItemText(20, _translate("MainWindow", "波兰语pl"))
        self.lang_choice.setItemText(21, _translate("MainWindow", "丹麦语dan"))
        self.lang_choice.setItemText(22, _translate("MainWindow", "罗马尼亚语rom"))
        self.lang_choice.setItemText(23, _translate("MainWindow", "匈牙利语hul"))
        self.title.setText(_translate("MainWindow", "标题"))
        self.description.setText(_translate("MainWindow", "描述"))
        self.keywords.setText(_translate("MainWindow", "关键字"))
        self.srt_file.setText(_translate("MainWindow", "字幕文件"))
        self.choicesrt_button.setText(_translate("MainWindow", "选择文件"))
        self.choiceaudio_button_.setText(_translate("MainWindow", "选择文件"))
        self.audio_file.setText(_translate("MainWindow", "音频文件"))
        self.language.setText(_translate("MainWindow", "语言"))
        self.audio_choice.setItemText(0, _translate("MainWindow", "选填"))
        self.audio_choice.setItemText(1, _translate("MainWindow", "localized_audio"))
        self.audio_choice.setItemText(2, _translate("MainWindow", "audio_description"))
        self.audio_choice.setItemText(3, _translate("MainWindow", "commentary"))
        self.audio_type.setText(_translate("MainWindow", "音频类型"))
        self.synthetise.setText(_translate("MainWindow", "翻译生成"))
