import requests
import json
from bs4 import BeautifulSoup
import execjs
from aip import AipNlp

import http.client
#import md5
import hashlib
import urllib
import random
import time

appid = '20190710000316607' #你的appid
secretKey = 'Z3j1AehLpDY_30cVoVHn' #你的密钥

""" 你的 APPID AK SK """
#APP_ID = '16748275'
#API_KEY = '53e5jBb3v5DFlZUNv3SDAUsl'
#SECRET_KEY = 'p4nBF0Ai9gGGitWqdHhzBe4Gmx8jVfyW'

#client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

class Py4Js():

    def __init__(self): 
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072;             
        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f";       
        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
                var m = a.charCodeAt(g); 
                128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
                e[f++] = m >> 18 | 240, 
                e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
                e[f++] = m >> 6 & 63 | 128), 
                e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    };          
    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
                var d = b.charAt(c + 2), 
                d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
                d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
                a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
 """)
    def getTk(self,text):
        return self.ctx.call("TL",text)

def buildUrl(text,tk,language):

    baseUrl='https://translate.google.cn/translate_a/single'
    baseUrl+='?client=t&'

    if language == 'en-zh':
        baseUrl+='s1=en&'
        baseUrl+='t1=zh-CN&'
        baseUrl+='h1=zh-CN&'
    elif language == 'zh-en':
        baseUrl+='sl=zh-CN&'
        baseUrl+='tl=en&'
        baseUrl+='hl=zh-CN&'

    baseUrl+='dt=at&'
    baseUrl+='dt=bd&'
    baseUrl+='dt=ex&'
    baseUrl+='dt=ld&'
    baseUrl+='dt=md&'
    baseUrl+='dt=qca&'
    baseUrl+='dt=rw&'
    baseUrl+='dt=rm&'
    baseUrl+='dt=ss&'
    baseUrl+='dt=t&'
    baseUrl+='ie=UTF-8&'
    baseUrl+='oe=UTF-8&'
    baseUrl+='otf=1&'
    baseUrl+='pc=1&'
    baseUrl+='ssel=0&'
    baseUrl+='tsel=0&'
    baseUrl+='kc=2&'
    baseUrl+='tk='+str(tk)+'&'
    baseUrl+='q='+text
    return baseUrl


def translate(language,text):
    header={
        'authority':'translate.google.cn',
        'method':'GET',
        'path':'',
        'scheme':'https',
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'cookie':'',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'x-client-data':'CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE='
    }
    url=buildUrl(text,js.getTk(text),language)
    res=''
    try:
        r=requests.get(url)
        result=json.loads(r.text)
        #print (result)
        if result[7]!=None:
            # 如果我们文本输错，提示你是不是要找xxx的话，那么重新把xxx正确的翻译之后返回
            try:
                correctText=result[7][0].replace('<b><i>',' ').replace('</i></b>','')
                print(correctText)
                correctUrl=buildUrl(correctText,js.getTk(correctText),language)
                correctR=requests.get(correctUrl)
                newResult=json.loads(correctR.text)
                res=newResult[0][0][0]

            except Exception as e:
                print(e)
                for r in result[0]: 
                    if r[0] is not None: 
                        res += r[0]

        else:
            for r in result[0]: 
                if r[0] is not None: 
                    res += r[0]
    except Exception as e:
        res=''
        print(url)
        print("翻译"+text+"失败")
        print("错误信息:")
        print(e)
    finally:
        return res

def dnnlm(text):
    dnn = client.dnnlm(text)
    return dnn["ppl"]

def translate_baidu(fromLang, toLang, q):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    #q = '苹果'
    #fromLang = 'zh'
    #toLang = 'en'
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
        res=(json_direct["trans_result"][0].get('dst'))
        return res
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    

text = "快速排名可以说是利用搜索引擎漏洞以及一些辅助工具使特定关键词快速快速排名在搜索引擎顶端的一个过程或技术。 正所谓“马无夜草不肥，人无横财不富”，搜索引擎优化是一个及其漫长的过程，平均排名时间大于6个月以上，但有时候我们经常在网上看到一些网站数天，数周就能获得大量的关键词排名，那么这是怎么做到的 鉴于博主本人并不擅长快排或者黑帽方面的知识，所以本文只是结合个人使用快排的一些心得和经历给大家做一个简单的科普，本博客也不会提供快排业务。"

if __name__ == '__main__':
    js=Py4Js()
    #yw = translate('zh-en',text)
    #res_enzh = translate('en-zh',yw)
    #print ("原文:",text)
    #print ("英文:",yw)
    #print ("伪原创:",res_enzh)
    yw=translate_baidu('zh', 'en', text)
    res_enzh = translate('en-zh',yw)
    #time.sleep(1)
    #res_enzh = translate_baidu('en', 'zh', yw)
    print ("原文:",text)
    print ("英文:",yw)
    print ("伪原创:",res_enzh)
    #print (dnnlm(text),dnnlm(res_enzh))
