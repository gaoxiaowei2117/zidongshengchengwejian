#/usr/bin/env python
#coding=utf8
 
import http.client
#import md5
import hashlib
import urllib
import random
import json

appid = '20190710000316607' #你的appid
secretKey = 'Z3j1AehLpDY_30cVoVHn' #你的密钥

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = '苹果'
fromLang = 'zh'
toLang = 'en'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
#m1 = md5.new()
m1 = hashlib.md5()
m1.update(sign.encode("utf8"))
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    json_direct=json.loads(response.read().decode("utf8"))
    print(json_direct)
    print(json_direct["trans_result"][0].get('src'))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
