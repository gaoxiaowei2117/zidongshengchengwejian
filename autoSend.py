# -*- coding: utf-8 -*-

import json
import os
import re
import random
from codecs import open
import requests
import sys
from get_verificatio_code import get_captcha_code
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

# python2 和 python3的兼容代码
try:
    # python2 中
    import cookielib
    print("user cookielib in python2.")
except:
    # python3 中
    import http.cookiejar as cookielib
    print("user cookielib in python3.")

def send_file_code(path):
    # session代表某一次连接
    mySession = requests.session()
    # 因为原始的session.cookies
    # 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    mySession.cookies = cookielib.LWPCookieJar(filename = path+"Cookie.txt")
    #f= open('./0.txt','r')
    f= open('./files/0.txt','r',encoding='utf8')
    fileContent = f.read()
    #print(fileContent)
    f.close()
    #print(fileContent)
    f= open(path+'/Authorization.txt','r')
    authorization = (f.readline()).rstrip('\n')
    f.close()
    #print(authorization)
    f= open(path+'/User_Agent.txt','r')
    user_agent = (f.readline()).rstrip('\n')
    f.close()
    #print(authorization)
    url='http://member.91huoke.com/api/member/article'
    headers={'Host': 'member.91huoke.com',
             'Connection': 'keep-alive',
             'Accept': 'application/json, text/plain, */*',
             'Origin': 'http://member.91huoke.com',
             'User-Agent': user_agent,
             'Authorization': authorization,
             'Content-Type': 'application/json;charset=UTF-8',
             'Referer': 'http://member.91huoke.com/',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.8',
            }
    #d=requests.post(url,data=payload,headers=headers)
    response=mySession.post(url,data=fileContent.encode('utf-8'),headers=headers).json()
    #print(json.dumps(response))
    #print(json.dumps(response).encode('utf-8').decode('unicode_escape'))
    print(json.dumps(response,ensure_ascii=False))
    #printond.text)
    '''
    status =  response.get('status')
    if status == 401:
        get_captcha_code(user_agent)
        print("haha")
    '''
    return response

if __name__ == "__main__":
    send_file_code(sys.argv[1])
