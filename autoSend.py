# -*- coding: utf-8 -*-

import json
import os
import re
import random
import codecs
import requests
import sys


# python2 和 python3的兼容代码
try:
    # python2 中
    import cookielib
    print("user cookielib in python2.")
except:
    # python3 中
    import http.cookiejar as cookielib
    print("user cookielib in python3.")

# session代表某一次连接
mySession = requests.session()
# 因为原始的session.cookies
# 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
mySession.cookies = cookielib.LWPCookieJar(filename = "Cookie.txt")

if __name__ == "__main__":
    #f= open('./0.txt','r')
    f= open('./files/0.txt','r')
    fileContent = f.read()
    f.close()
    #print(fileContent)
    f= open('./Authorization.txt','r')
    authorization = (f.readline()).rstrip('\n')
    f.close()
    #print(authorization)
    url='http://member.91huoke.com/api/member/article'
    headers={'Host': 'member.91huoke.com',
             'Connection': 'keep-alive',
             'Accept': 'application/json, text/plain, */*',
             'Origin': 'http://member.91huoke.com',
             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
             'Authorization': authorization,
             'Content-Type': 'application/json;charset=UTF-8',
             'Referer': 'http://member.91huoke.com/',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.8',
            }
    #d=requests.post(url,data=payload,headers=headers)
    d=mySession.post(url,data=fileContent,headers=headers)
    print(d)
    print(d.text)
