# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Works\YouBridge\YBtranslator\new_google.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import importlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QListWidget, QCheckBox, QListWidgetItem


class ComboCheckBox(QtWidgets.QComboBox):
    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = items
        self.items.insert(0, '全部')
        self.row_num = len(self.items)
        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        # self.lang_list = []
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)

    def addQCheckBox(self, i):
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.items[i])
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])
        # print('add', i)

    def Selectlist(self):
        Outputlist = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        self.Selectedrow_num = len(Outputlist)
        return Outputlist

    def show(self):
        show = ''
        Outputlist = self.Selectlist()
        # self.lang_list = Outputlist
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show += i + ';'
        if self.Selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(0)
        elif self.Selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(2)
        else:
            self.qCheckBox[0].setCheckState(1)
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)

    def All(self, zhuangtai):
        if zhuangtai == 2:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif zhuangtai == 1:
            if self.Selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(2)
        elif zhuangtai == 0:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.audio_choice = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_choice.setFont(font)
        self.audio_choice.setObjectName("audio_choice")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.audio_choice.addItem("")
        self.gridLayout.addWidget(self.audio_choice, 14, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)
        self.audio_file_con = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_file_con.setFont(font)
        self.audio_file_con.setObjectName("audio_file_con")
        self.gridLayout.addWidget(self.audio_file_con, 11, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.choicesrt_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choicesrt_button.setFont(font)
        self.choicesrt_button.setObjectName("choicesrt_button")
        self.gridLayout.addWidget(self.choicesrt_button, 8, 3, 1, 3)
        self.key_con = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.key_con.setFont(font)
        self.key_con.setObjectName("key_con")
        self.gridLayout.addWidget(self.key_con, 7, 2, 1, 4)

        itemList = ['英语en', '繁体zh-tw', '葡萄牙语pt', '希腊语el', '保加利亚语bg', '芬兰语fi', '斯洛文尼亚sl',
                    '法语fr', '阿拉伯语ar', '德语de', '荷兰语nl', '爱沙尼亚语et', '捷克语cs',
                    '瑞典语sv', '越南语vi', '日语ja', '西班牙语es', '俄语ru', '意大利语it',
                    '波兰语pl', '丹麦语da', '罗马尼亚语ro', '匈牙利语hu', '南非荷兰语af',
                    '阿尔巴尼亚语sq', '阿姆哈拉语am', '亚美尼亚语hy', '阿塞拜疆az', '巴斯克eu',
                    '白俄罗斯语be', '孟加拉bn', '波斯尼亚语bs', '加泰罗尼亚语ca', '塞布亚诺ceb',
                    '齐佩瓦语ny', '科西嘉语co', '克罗地亚语hr', '世界语eo', '菲律宾语tl',
                    '弗里斯语fy', '加利西亚语gl', '乔治亚语ka', '古吉拉特语gu', '海地克里奥尔语ht',
                    '豪萨语ha', '夏威夷语haw', '希伯来语iw', '印地语hi', '苗语hmn', '冰岛语is',
                    '伊博ig', '印度尼西亚语ud', '爱尔兰语ga', '爪哇语jw', '卡纳达语kn',
                    '哈萨克语kk', '高棉语km', '库尔德语ku', '吉尔吉斯语ky', '老挝lo', '拉丁la',
                    '拉脱维亚lv', '立陶宛语lt', '卢森堡lb', '马其顿语mk', '马达加斯加mg',
                    '马来语ms', '马拉雅拉姆语ml', '马耳他语mt', '毛利语mi', '马拉地语mr',
                    '蒙古语mn', '缅甸my', '尼泊尔ne', '挪威语no', '普什图语ps', '波斯fa',
                    '旁遮普语pa', '萨摩亚语sm', '苏格兰盖尔语gd', '塞尔维亚语sr', '塞索托st',
                    '肖纳sn', '信德sd', '僧伽罗语si', '斯洛伐克sk', '索马里so', '巽他语su',
                    '斯瓦希里语sw', '塔吉克tg', '泰米尔语ta', '泰卢固语te', '土耳其语tr',
                    '乌克兰语uk', '乌尔都语ur', '乌兹别克uz', '威尔士语cy', '科萨xh', '意第绪语yi',
                    '约鲁巴yo', '祖鲁zu', '菲律宾fil', '希伯来语he']
        self.comboBox = ComboCheckBox(itemList)
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)

        # for i in range(10):
        #     self.comboBox.addItem("")
        #     item = self.comboBox.model().item(i, 0)
        #     item.setCheckState(QtCore.Qt.Unchecked)

        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 1)
        self.synthetise = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.synthetise.setFont(font)
        self.synthetise.setObjectName("synthetise")
        self.gridLayout.addWidget(self.synthetise, 15, 5, 2, 1)
        self.desc_con = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_con.setFont(font)
        self.desc_con.setObjectName("desc_con")
        self.gridLayout.addWidget(self.desc_con, 6, 2, 1, 4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 14, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.srt_file_con = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.srt_file_con.setFont(font)
        self.srt_file_con.setText("")
        self.srt_file_con.setObjectName("srt_file_con")
        self.gridLayout.addWidget(self.srt_file_con, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.choiceaudio_button_ = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choiceaudio_button_.setFont(font)
        self.choiceaudio_button_.setObjectName("choiceaudio_button_")
        self.gridLayout.addWidget(self.choiceaudio_button_, 11, 3, 1, 3)
        self.video_id_con = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.video_id_con.setFont(font)
        self.video_id_con.setText("")
        self.video_id_con.setObjectName("video_id_con")
        self.gridLayout.addWidget(self.video_id_con, 0, 2, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.mainornot = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainornot.setFont(font)
        self.mainornot.setObjectName("mainornot")
        self.mainornot.addItem("")
        # self.mainornot = QtWidgets.QCheckBox(self.centralwidget)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.mainornot.setFont(font)
        # self.mainornot.setObjectName("mainornot")
        self.gridLayout.addWidget(self.mainornot, 3, 3, 1, 2)

        self.save_preset = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_preset.setFont(font)
        self.gridLayout.addWidget(self.save_preset, 3, 5, 1, 1)

        self.choice_preset = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choice_preset.setFont(font)
        self.choice_preset.addItem("")
        self.gridLayout.addWidget(self.choice_preset, 4, 2, 1, 1)

        self.preset_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.preset_label.setFont(font)
        self.preset_label.setObjectName("preset_label")
        self.gridLayout.addWidget(self.preset_label, 4, 0, 1, 1)


        self.title_con = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_con.setFont(font)
        self.title_con.setObjectName("title_con")
        self.gridLayout.addWidget(self.title_con, 5, 2, 1, 4)
        self.lang_choice = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lang_choice.setFont(font)
        self.lang_choice.setObjectName("lang_choice")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.lang_choice.addItem("")
        self.gridLayout.addWidget(self.lang_choice, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YBtrans_Google"))
        self.label_2.setText(_translate("MainWindow", "语言"))
        self.audio_choice.setItemText(0, _translate("MainWindow", "选填"))
        self.audio_choice.setItemText(1, _translate("MainWindow", "localized_audio"))
        self.audio_choice.setItemText(2, _translate("MainWindow", "audio_description"))
        self.audio_choice.setItemText(3, _translate("MainWindow", "commentary"))
        self.label_7.setText(_translate("MainWindow", "音频文件"))
        self.label_5.setText(_translate("MainWindow", "关键字"))
        self.label_9.setText(_translate("MainWindow", "原始语言"))
        self.choicesrt_button.setText(_translate("MainWindow", "选择文件"))

        self.synthetise.setText(_translate("MainWindow", "翻译生成"))
        self.label_8.setText(_translate("MainWindow", "音频类型"))
        self.label_4.setText(_translate("MainWindow", "描述"))
        self.label.setText(_translate("MainWindow", "视频ID"))
        self.label_6.setText(_translate("MainWindow", "字幕文件"))
        self.choiceaudio_button_.setText(_translate("MainWindow", "选择文件"))
        self.label_3.setText(_translate("MainWindow", "标题"))
        # self.mainornot.setText(_translate("MainWindow", "指定为主要语言"))
        self.mainornot.setItemText(0, _translate("MainWindow", "指定主要语言"))
        self.save_preset.setText(_translate("MainWindow", "保存"))
        self.preset_label.setText(_translate("MainWindow", "预设选择"))
        # self.choice_preset.setText
        self.lang_choice.setItemText(0, _translate("MainWindow", "自动auto"))
        self.lang_choice.setItemText(1, _translate("MainWindow", "汉语zh-cn"))
        self.lang_choice.setItemText(2, _translate("MainWindow", "英语en"))
        self.choice_preset.setItemText(0, _translate("MainWindow", "请选择预设"))
