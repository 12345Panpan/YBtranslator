import http.client
import hashlib
import urllib
import random
import json
import csv
import re
import time

appid = '20200803000532159'
secretKey = 'zeBDUeIDBi5p_p0Z68zW'
httpClient = None


def translateBaidu(content, toLang='en'):
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


def save_csv(title, data):
    file_name = title + '.csv'
    header = ['video_id', 'is_primary_language', 'language', 'title', 'description', 'keywords', 'caption_file',
              'audio_track_file', 'audio_content_type']
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)


def save_srt(title, srt_name, language):
    srt_after_name = title[0:5] + '_' + language + '.srt'
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
                        line_after = translateBaidu(line, toLang=language)
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


if __name__ == '__main__':

    # 获取输入内容
    video_id = input('请输入视频id*：')

    primary_lang = input('请选择是否指定此语言是否为视频元数据的主要语言：')
    if primary_lang is '': primary_lang = 'no'

    language = input('请选择翻译语言(默认英文)：')
    if language is '': language = 'en'

    title = input('请输入视频标题*：')
    title_result = translateBaidu(content=title, toLang=language)

    desc = input('请输入视频描述：')
    if desc is not '':
        desc_result = translateBaidu(content=desc, toLang=language)
    else:
        desc_result = ''

    keywords = input('请输入关键字：')
    keywords_result = translateBaidu(content=keywords, toLang=language)

    caption_file_before = input('请输入字幕文件名称：')
    caption_file_before += '.txt'
    caption_file = save_srt(title, caption_file_before, language)
    print('字幕文件导出完成！')

    audio_track_file = input('请输入音频文件的名称：')

    audio_content_type = input('请选择音频类型：')

    data = [video_id, primary_lang, language, title_result, desc_result, keywords_result, caption_file,
            audio_track_file, audio_content_type]
    date = time.strftime('%F')
    save_csv(date, data)
