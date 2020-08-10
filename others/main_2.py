# from YBtranslator_widget import Ui_Form
from YBtranslator_ui import  Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QInputDialog
import sys
import re
import time
import csv
import random
import http.client
import json
import urllib
import hashlib
import os


appid = '20200803000532159'
secretKey = 'zeBDUeIDBi5p_p0Z68zW'
httpClient = None

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.synthetise_2.clicked.connect(self.DataSyn)
        self.choicesrt_button_2.clicked.connect(self.Choice_srt)
        self.choiceaudio_button_1.clicked.connect(self.Choice_audio)
        self.mainornot_2.stateChanged.connect(self.CheckBox)
        self.data = ['', 'no', 'en', '', '', '', '', '', '']
        # self.is_primary_language = 'no'

    #################--slog--#########################
    def Choice_srt(self):  # 选择字幕文件
        # filename要变为self.caption_file
        filename = QFileDialog.getOpenFileName(self, '.srt', 'd:')
        filename = filename[0].split('/')[-1]
        self.srt_file_con_2.setText(filename)

    def Choice_audio(self):  # 选择音频文件
        # filename要变为self.audio_track_file
        filename = QFileDialog.getOpenFileName(self, 'd:')
        filename = filename[0].split('/')[-1]
        self.audio_file_con_2.setText(filename)

    def CheckBox(self):
        if self.data[1] == 'no':
            self.data[1] = 'yes'
        else:
            self.data[1] = 'no'
        print(self.data[1])

    def translateBaidu(self, content, toLang):
        fromLang = 'auto'
        q = content
        salt = str(random.randint(32768, 65536))
        sign = appid + content + salt + secretKey
        sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
        myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            response = httpClient.getresponse()
            result_all = response.read().decode('utf-8')
            result = json.loads(result_all)
            dst = str(result["trans_result"][0]["dst"])
            return dst
        except Exception as e:
            print(e)

    def save_csv(self, title, data):
        file_name = title + '.csv'
        if os.path.exists(file_name) is False:
            header = ['video_id', 'is_primary_language', 'language', 'title', 'description', 'keywords', 'caption_file',
                  'audio_track_file', 'audio_content_type']
            with open(file_name, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
        else:
            with open(file_name, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)

    def DataSyn(self):
        # video_id
        self.data[0] = self.video_id_con_2.text()
        # language
        lang_index = self.lang_choice_2.currentIndex()
        self.data[2] = re.sub(u"([^\u0041-\u007a])", "", self.lang_choice_2.itemText(lang_index))
        # title
        self.data[3] = self.translateBaidu(self.title_con_2.toPlainText(), self.data[2])
        # description
        self.data[4] = self.translateBaidu(self.desc_con_2.toPlainText(), self.data[2])
        # keywords
        self.data[5] = self.translateBaidu(self.key_con_2.toPlainText(), self.data[2])
        # caption_file
        self.data[6] = self.srt_file_con_2.toPlainText()
        # audio_track_file
        self.data[7] = self.audio_file_con_2.toPlainText()
        # audio_content_type
        audio_index = self.audio_choice_2.currentIndex()
        self.data[8] = self.audio_choice_2.itemText(audio_index)
        if audio_index == 0:
            self.data[8] = ''
        print(self.data)
        self.save_csv(time.strftime('%F'), self.data)


##################################################
app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())

#今天的天儿可真热啊，我都热死了呢，然后今天7点55起床的，8点58到公司，卡得刚刚好！我真不错哈哈哈哈