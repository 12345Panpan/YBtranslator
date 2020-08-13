# from YBtranslator_widget import Ui_Form
from new_baidu import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
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
lang_dict = {'bul': 'bg', 'zh': 'zh-CN', 'est': 'et', 'swe': 'sv', 'jp': 'ja', 'spa': 'es'}


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.synthetise.clicked.connect(self.DataSyn)
        self.choicesrt_button.clicked.connect(self.Choice_srt)
        self.choiceaudio_button_.clicked.connect(self.Choice_audio)
        self.mainornot.stateChanged.connect(self.CheckBox)
        self.data = ['', 'no', 'en', '', '', '', '', '', '']
        self.srt_file_name = ''
        self.lang_baidu = ''
        self.filepath = ''
        self.title_orign = ''

    ####################--slog--#########################
    def Choice_srt(self):  # 选择字幕文件
        # filename要变为self.caption_file
        filename = QFileDialog.getOpenFileName(self, '.srt', 'd:')
        self.filepath = filename[0]
        filename = filename[0].split('/')[-1]
        self.srt_file_con.setText(filename)

    def Choice_audio(self):  # 选择音频文件
        # filename要变为self.audio_track_file
        filename = QFileDialog.getOpenFileName(self, 'd:')
        filename = filename[0].split('/')[-1]
        self.audio_file_con.setText(filename)

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
            for i in range(1, len(result["trans_result"])):
                dst += '\n'
                dst += result["trans_result"][i]["dst"]
            return dst
        except Exception as e:
            print(e)

    def save_csv(self, title, data):
        # print(time.strftime('%H'))
        if int(time.strftime('%H')) >= 14:

            file_name = title + 'pm' + '.csv'
        else:
            file_name = title + 'am' + '.csv'
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

    def save_srt(self, title, srt_name, language):
        srt_after_name = str(title) + '_' + language + '.srt'
        with open(srt_name, encoding='UTF-8') as file_obj:
            with open(srt_after_name, 'w', encoding='UTF-8') as srt_after:
                for line in file_obj:
                    line = line.strip()
                    if len(line) and not line.isdigit():
                        first_str = line[0:1]
                        if not first_str.isdigit():
                            line = re.sub("<[^>]*>", "", line)
                            line = re.sub("{[^}]*}", "", line)
                            # print(line)
                            line_after = self.translateBaidu(line, toLang=language)
                            # print(line_after)
                            srt_after.writelines(line_after)
                            srt_after.writelines('\n')
                        else:
                            srt_after.writelines(line)
                            srt_after.writelines('\n')
                    else:
                        srt_after.writelines(line)
                        srt_after.writelines('\n')
        return srt_after_name

    def key_trans(self, key_orign, language):
        key_list = re.split('[|]', key_orign)
        key_result = ''
        for item in key_list:
            key_result += self.translateBaidu(item, language)
            key_result += '|'
            # print(key_result)
        key_result = key_result.rstrip('|')
        return key_result

    def DataSyn(self):
        # video_id
        self.data[0] = self.video_id_con.text()

        # language
        lang_index = self.lang_choice.currentIndex()
        lang_baidu = re.sub(u"([^\u0041-\u007a])", "", self.lang_choice.itemText(lang_index))
        if lang_baidu in lang_dict:
            self.data[2] = lang_dict[lang_baidu]
        else:
            self.data[2] = lang_baidu[0:2]

        # title
        self.title_orign = self.title_con.text()
        self.data[3] = self.translateBaidu(self.title_con.text(), lang_baidu)

        # description 选填
        # print(self.desc_con.toPlainText())
        self.data[4] = self.translateBaidu(self.desc_con.toPlainText(), lang_baidu)

        # keywords 选填
        if self.key_con.text() == '':
            self.data[5] = ''
        else:
            # key_words = self.translateBaidu(self.key_con.text(), lang_baidu)
            self.data[5] = self.key_trans(self.key_con.text(), lang_baidu)

        # caption_file
        srt_file_original = self.srt_file_con.text()
        if srt_file_original == '':
            self.data[6] = ''
        else:
            self.data[6] = self.save_srt(self.title_orign, self.filepath, lang_baidu)

        # audio_track_file
        if self.audio_file_con == '':
            self.data[7] = ''
        else:
            self.data[7] = self.audio_file_con.text()

        # audio_content_type
        audio_index = self.audio_choice.currentIndex()
        self.data[8] = self.audio_choice.itemText(audio_index)
        if audio_index == 0:
            self.data[8] = ''
        self.save_csv(time.strftime('%F'), self.data)
        QMessageBox.information(self, "提示", "翻译文件已生成。")


##################################################

app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
