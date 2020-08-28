from new_google import Ui_MainWindow
from googletrans import Translator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox, QProgressDialog, QProgressBar, QLineEdit, \
    QListWidget
import sys
import re
import time
import csv
import os

_translate = QtCore.QCoreApplication.translate


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.lang_list = []
        self.synthetise.clicked.connect(self.DataSyn)
        self.choicesrt_button.clicked.connect(self.Choice_srt)
        self.choiceaudio_button_.clicked.connect(self.Choice_audio)
        self.Preset_show()
        # self._translate = QtCore.QCoreApplication.translate

        for i in range(1, self.comboBox.row_num):
            self.comboBox.qCheckBox[i].stateChanged.connect(self.Main_lang)
        self.choice_preset.currentIndexChanged.connect(self.Lang_set)

        self.save_preset.clicked.connect(self.Save_preset)
        self.data = ['', 'no', 'en', '', '', '', '', '', '']
        # self.srt_file_name = ''
        # self.lang_temp = ''
        self.filepath = ''
        # self.check_status = 'no'
        self.line_index = 0
        self.line_count = 0
        self.progressDialog = QProgressDialog(self)
        self.progressDialog.reset()
        self.trans = Translator(service_urls=['translate.google.cn'])
        self.main_lang = ''
        self.lang_select = ''
        self.preset_num = 0

    #################--slog--#########################

    def Lang_set(self):
        preset_index = self.choice_preset.currentIndex()
        preset_content = self.choice_preset.itemText(preset_index)
        if preset_content != "请选择预设":
            self.comboBox.clear()
            if os.path.exists('preset.csv') is True:
                with open('preset.csv', 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row == []: break
                        if row[0] == preset_content:
                            self.main_lang = row[1]
                            self.lang_list = row[2:]
            for i in range(1, self.comboBox.row_num):
                for j in self.lang_list:
                    if self.comboBox.qCheckBox[i].text() == j:
                        self.comboBox.qCheckBox[i].setCheckState(1)

    def Save_preset(self):
        self.lang_select = self.comboBox.Selectlist()
        self.main_lang = self.mainornot.itemText(self.mainornot.currentIndex())
        value, ok = QInputDialog.getText(self, "预设", '请输入此预设的标题', QLineEdit.Normal)
        save_list = [value, self.main_lang]
        save_list += self.lang_select
        file_name = 'preset.csv'
        if os.path.exists(file_name) is False:
            with open(file_name, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(save_list)
        else:
            with open(file_name, 'r', encoding='utf-8') as old_file:
                lines = old_file.readlines()
                if len(lines) > 1:
                    lines.remove('\n')
            with open(file_name, 'w', encoding='utf-8') as new_file:
                for line in lines:
                    # print('line:', line)
                    # if line != '':
                    if line[0:line.find(',')] != value:
                        new_file.write(line)
                writer = csv.writer(new_file)
                writer.writerow(save_list)
            # with open(file_name, 'r', encoding='utf-8') as this_file:
            #     thislines = this_file.readlines()
            #     for line in thislines:
            #         print('this line is：', line)
            #     print('lines num is:', len(thislines))
            self.Preset_show()
            # self.choice_preset.removeItem(self.choice_preset.count())

    def Main_lang(self):
        Outputlist = []
        for i in range(1, self.comboBox.row_num):
            if self.comboBox.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.comboBox.qCheckBox[i].text())
        self.comboBox.Selectedrow_num = len(Outputlist)
        self.mainornot.clear()
        self.mainornot.addItem("")
        self.mainornot.setItemText(0, _translate("MainWindow", '指定主要语言'))
        for i in range(len(Outputlist)):
            self.mainornot.addItem("")
            self.mainornot.setItemText(i + 1, _translate("MainWindow", Outputlist[i]))
        # self.Preset_show()
        self.mainornot.setCurrentIndex(self.mainornot.findText(self.main_lang))

    def Preset_show(self):
        for i in range(1, self.choice_preset.count()+1):
            self.choice_preset.removeItem(i)
            # print('remove', i)
        if os.path.exists('preset.csv') is True:
            with open('preset.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                i = 1
                for row in reader:
                    if row == []:
                        # print('reach the end')
                        break
                    # print('preset name is:', row[0])
                    self.choice_preset.addItem("")
                    # print('add', i)
                    self.choice_preset.setItemText(i, _translate("MainWindow", row[0]))
                    i += 1
                self.preset_num = i
            # print(self.choice_preset.count())

            for j in range(i, self.choice_preset.count()+1):
                self.choice_preset.removeItem(j)
                # print('resub', j)
            # print(self.choice_preset.count())

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

    def translateGoogle(self, content, toLang, fromLang):
        # fromLang = fromLang
        q = content
        result = self.trans.translate(q, dest=toLang, src=fromLang).text
        return result

    def save_csv(self, title, date, data):
        file_name = date + '-' + title + '.csv'
        #
        # if int(time.strftime('%H')) >= 14:
        #
        #     file_name = date + 'pm' + '.csv'
        # else:
        #     file_name = date + 'am' + '.csv'
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
        self.trans = Translator(service_urls=['translate.google.cn'])
        with open(srt_name, encoding='utf-8') as file_obj:
            self.line_count = len(file_obj.readlines())
        with open(srt_name, encoding='utf-8') as file_obj:
            with open(srt_after_name, 'w', encoding='utf-8-sig') as srt_after:
                self.line_index = 0
                interval = 4
                for line in file_obj:
                    line = line.strip()
                    if self.line_index == 0:
                        if line[-1] != '1':
                            print('no number line!')
                            interval = 3
                        self.line_count = (self.line_count + 1) / interval

                        self.progressDialog.setWindowTitle("进度提示")
                        self.progressDialog.setLabelText(srt_after_name + ' 生成中...')
                        # self.progressDialog.setCancelButtonText('取消')
                        self.progressDialog.setMaximum(self.line_count)
                        self.progressDialog.open(lambda: print('对话框被取消'))

                    if self.line_index % 200 == 0:
                        self.trans = Translator(service_urls=['translate.google.cn'])

                    if self.line_index % interval == 2:
                        line = re.sub("<[^>]*>", "", line)
                        line = re.sub("{[^}]*}", "", line)
                        if line == '':
                            line_after = '\n'
                            # print('line %d is empty' %(self.line_index))
                        else:
                            line_after = self.translateGoogle(line, toLang=language, fromLang=lang_org) + '\n'
                        srt_after.writelines(line_after)
                    else:
                        srt_after.writelines(line + '\n')
                    self.line_index += 1
                    self.progressDialog.setValue(int(self.line_index / 4) + self.line_index % 4)
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
            key_trans += self.translateGoogle(item, 'en', lang_org)
            key_trans += '|'
        key_result += key_trans
        key_result = key_result.rstrip('|')
        # print(key_result)
        return key_result

    def ProgressBar(self, file_name):
        self.progressDialog.setWindowTitle("进度提示")
        self.progressDialog.setLabelText(file_name + ' 生成中...')
        # self.progressDialog.setCancelButtonText('取消')
        self.progressDialog.setMaximum(int(self.line_count))
        self.progressDialog.setAutoClose(True)
        self.progressDialog.setAutoReset(True)

    def DataSyn(self):

        lang_select_after = self.comboBox.Selectlist()
        lang_num = len(lang_select_after)
        # print('lang_num is:', lang_num)

        self.data = [[0 for col in range(9)] for row in range(lang_num)]  # 大小为n*m列表
        for i in range(lang_num):
            lang_select_after[i] = re.sub(u"([^\u0041-\u007a])", "", lang_select_after[i])
            if lang_select_after[i] == 'zhtw':
                lang_select_after[i] = 'zh-tw'
            self.data[i][2] = lang_select_after[i]

        # print('select lang are:', lang_select_after)

        lang_index = self.lang_choice.currentIndex()
        lang_org = self.lang_choice.itemText(lang_index)[2:]

        # video_id
        video_id_temp = self.video_id_con.text()

        # is_primary_language
        main_lang_index = self.mainornot.currentIndex()
        self.main_lang = self.mainornot.itemText(main_lang_index)
        main_lang = re.sub(u"([^\u0041-\u007a])", "", self.main_lang)
        if main_lang_index == 0:
            main_lang = ''
        # print(main_lang)
        for i in range(lang_num):
            # print(lang_select_after[i])
            if lang_select_after[i] == main_lang:
                self.data[i][1] = 'yes'
            else:
                self.data[i][1] = 'no'

        # title
        title_orign = self.title_con.text()
        for i in range(lang_num):
            self.data[i][3] = self.translateGoogle(self.title_con.text(), lang_select_after[i], lang_org)

        # description 选填
        if self.desc_con.toPlainText() == '':
            for i in range(lang_num): self.data[i][4] = ''
        else:
            for i in range(lang_num):
                self.data[i][4] = self.translateGoogle(self.desc_con.toPlainText(), lang_select_after[i], lang_org)

        # keywords 选填
        if self.key_con.text() == '':
            for i in range(lang_num): self.data[i][5] = ''
        else:
            for i in range(lang_num):
                self.data[i][5] = self.key_trans(self.key_con.text(), lang_select_after[i], lang_org)

        # caption_file
        srt_file_original = self.srt_file_con.text()
        if srt_file_original == '':
            for i in range(lang_num): self.data[i][6] = ''
        else:
            for i in range(lang_num):
                # self.trans = Translator(service_urls=['translate.google.cn'])
                self.data[i][6] = self.save_srt(title_orign, self.filepath, lang_select_after[i], lang_org)
                if i == lang_num - 1:
                    self.progressDialog.reset()

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

        # self.Preset_show()
        # self.choice_preset.removeItem(self.choice_preset.count())
        for j in range(self.preset_num, self.choice_preset.count() + 1):
            self.choice_preset.removeItem(j)

        self.save_csv(title_orign, time.strftime('%F'), self.data)
        QMessageBox.information(self, "提示", "翻译文件已生成。")


##################################################


app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
