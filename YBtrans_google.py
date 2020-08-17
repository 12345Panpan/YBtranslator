from new_google import Ui_MainWindow
from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
import sys
import re
import time
import csv
import os


translator = Translator()

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
        self.lang_temp = ''
        self.filepath = ''
        self.check_status = 'no'

    #################--slog--#########################
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
        if self.check_status == 'no':
            self.check_status = 'yes'
        else:
            self.check_status = 'no'
        print(self.check_status)

    def translateGoogle(self, content, toLang, fromLang):
        # fromLang = fromLang
        q = content
        result = translator.translate(q, dest=toLang, src=fromLang).text
        return result

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
                for i in range(len(data)):
                    writer.writerow(data[i])
        else:
            with open(file_name, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for i in range(len(data)):
                    writer.writerow(data[i])

    def save_srt(self, title, srt_name, language, lang_org):
        srt_after_name = title + '_' + language + '.srt'
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
                            line_after = self.translateGoogle(line, toLang=language, fromLang=lang_org)
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

    def key_trans(self, key_orign, language, lang_org):
        key_list = re.split('[,]', key_orign)
        if len(key_list) == 1:
            key_list = re.split(re.compile(r'\，'), key_orign)
        key_result = ''
        key_trans = ''
        for item in key_list:
            key_result += item
            key_result += '|'
            key_trans += self.translateGoogle(item, language, lang_org)
            key_trans += '|'
        key_result += key_trans
        key_result = key_result.rstrip('|')
        # print(key_result)
        return key_result

    def DataSyn(self):
        lang_list = self.comboBox.Selectlist()
        lang_num = len(lang_list)
        self.data = [[0 for col in range(9)] for row in range(lang_num)] #大小为n*m列表
        for i in range(lang_num):
            lang_list[i] = re.sub(u"([^\u0041-\u007a])", "", lang_list[i])
            self.data[i][2] = lang_list[i]

        lang_index = self.lang_choice.currentIndex()
        lang_org = self.lang_choice.itemText(lang_index)[2:]

        # video_id
        video_id_temp = self.video_id_con.text()

        # title
        title_orign = self.title_con.text()
        for i in range(lang_num):
            self.data[i][3] = self.translateGoogle(self.title_con.text(), lang_list[i], lang_org)

        # description 选填
        if self.desc_con.toPlainText() == '':
            for i in range(lang_num): self.data[i][4] = ''
        else:
            for i in range(lang_num):
                self.data[i][4] = self.translateGoogle(self.desc_con.toPlainText(), lang_list[i], lang_org)

        # keywords 选填
        if self.key_con.text() == '':
            for i in range(lang_num): self.data[i][5] = ''
        else:
            for i in range(lang_num):
                self.data[i][5] = self.key_trans(self.key_con.text(), lang_list[i], lang_org)

        # caption_file
        srt_file_original = self.srt_file_con.text()
        if srt_file_original == '':
            for i in range(lang_num): self.data[i][6] = ''
        else:
            for i in range(lang_num):
                self.data[i][6] = self.save_srt(title_orign, self.filepath, lang_list[i], lang_org)

        # audio_track_file
        if self.audio_file_con == '':
            audio_file_con_temp = ''
        else:
            audio_file_con_temp = self.audio_file_con.text()

        # audio_content_type
        audio_index = self.audio_choice.currentIndex()
        audio_content_type_temp = self.audio_choice.itemText(audio_index)
        if audio_index == 0:
            audio_content_type_temp = ''
        for i in range(lang_num):
            self.data[i][0] = video_id_temp
            self.data[i][7] = audio_file_con_temp
            self.data[i][8] = audio_content_type_temp
            self.data[i][1] = self.check_status


        self.save_csv(time.strftime('%F'), self.data)
        QMessageBox.information(self, "提示", "翻译文件已生成。")


##################################################

app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
