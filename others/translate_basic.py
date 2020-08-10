import http.client
import hashlib
import urllib
import random
import json

appid = '20200803000532159'
secretKey = 'zeBDUeIDBi5p_p0Z68zW'
httpClient = None

def translateBaidu(content, fromLang='auto', toLang='en'):
    q = content
    salt = str(random.randint(32768, 65536))
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        # paramas = {
        #     'appid': appid,
        #     'q': content,
        #     'from': fromLang,
        #     'to': toLang,
        #     'salt': salt,
        #     'sign': sign
        # }
        # response = requests.get(apiurl, paramas)
        # jsonResponse = response.json()  # 获得返回的结果，结果为json格式
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode('utf-8')
        result = json.loads(result_all)
        dst = str(result["trans_result"][0]["dst"])
        # dst = str(jsonResponse["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst
    except Exception as e:
        print(e)


if __name__ == '__main__':
    content = input('请输入要翻译的内容：')
    result = translateBaidu(content=content)
    print(result)
    
