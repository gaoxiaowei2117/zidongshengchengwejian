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

def send_file_code_fromDB(taskRecord):
    # session代表某一次连接
    mySession = requests.session()
    # 因为原始的session.cookies
    # 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    #mySession.cookies = cookielib.LWPCookieJar(filename = path+"Cookie.txt")
    cookieArr = taskRecord[8].split('=')
    #print('cookie',cookieArr)
    cookies = {cookieArr[0]:cookieArr[1],}
    #cookies = {"TOKON_KEY":"Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhkMTA2OTg2NmFjZjMxMjg5ZWMwMzI3NzI4ZTJiY2NkMDUxZjI4MTM3YzU3ZDc2YjFlOWY2ODcwOWY2MTAyZjM4NDBhMTJmYTg1MWE3NDBmIn0.eyJhdWQiOiIzIiwianRpIjoiOGQxMDY5ODY2YWNmMzEyODllYzAzMjc3MjhlMmJjY2QwNTFmMjgxMzdjNTdkNzZiMWU5ZjY4NzA5ZjYxMDJmMzg0MGExMmZhODUxYTc0MGYiLCJpYXQiOjE1NTkyOTYxMTAsIm5iZiI6MTU1OTI5NjExMCwiZXhwIjoxNTkwOTE4NTEwLCJzdWIiOiIyNTc3NyIsInNjb3BlcyI6WyIqIl19.D2fuWFG0svps6n2ynTsUmq-ycDCpeG9KwRQ9USLavGBu4kS_TGuaxJevWy7U3j8_9d8qY769SucBjo-FtBRDFRmamxIsn3GrL0R5VyP2Us0sUXqQ_ICTtEVvBMYsq2_JruEIOMBQ-iXPXkv1h5LRFf9P-3FDjXU3wetS6_7WqPs2pTluZIkeTNzqULEBuIShRgoaRtDpK8lntFgsAZU3VADcY0MHamte4Enu0qw997_yQrD2dG24Sgy6DbXY9WiRpQtNTDiDBlUNiVrIa7FHh6qbyhxrX_zyIs_hZDTyh4SGlG2ojPNFeF6sZcLo2KO8AfR9i-nuGJf8AwQ9i9vU8BwbhFazU7KdZ9XaJty9yJIutzDBgzs3e82oq1qfHVJe1vrlKxhX0WFJzXTWkGED3JHZQxs0baZEr5Sgel7Cq1BltWU_CENoY2j3nb6FDob0jlwZ9FdoF6ZWAyBHavNcrhC58gL_E_gQn-dRl4zWeKGNFDfSt6ptt7ewA6cJ2obLrRSBMhMoiSWQvrD5n3ZjMQ8ciWSVgD6p5nY1JwYBcWzulWvyanHEokmSM5MrLT2skdMNZxfTvuuXZgIQz868bqbyZPsYNJUZhSJpvAyhnT8JO2iYjg3dQbSyytCnm-xiQyo1dvzbvsmUxZgLbqNxMWUir11ll94xZxaFD1wtuPs",}
    authorization = taskRecord[7]
    #print('Authorization', authorization)
    user_agent = taskRecord[9]
    #print('UA', user_agent)
    #print(type( cookies))
    #f= open('./0.txt','r')
    f= open('./files/0.txt','r',encoding='utf8')
    fileContent = f.read()
    #print(fileContent)
    f.close()
    #print(fileContent)
    #f= open(path+'/Authorization.txt','r')
    #authorization = (f.readline()).rstrip('\n')
    #f.close()
    #print(authorization)
    #f= open(path+'/User_Agent.txt','r')
    #user_agent = (f.readline()).rstrip('\n')
    #f.close()
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
    #response=mySession.post(url,data=fileContent.encode('utf-8'),headers=headers).json()
    response=mySession.post(url,data=fileContent.encode('utf-8'),headers=headers, cookies=cookies).json()
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

def send_file_code(path):
    # session代表某一次连接
    mySession = requests.session()
    # 因为原始的session.cookies
    # 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    mySession.cookies = cookielib.LWPCookieJar(filename = path+"Cookie.txt")
    #cookies = {"TOKON_KEY":"Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjhkMTA2OTg2NmFjZjMxMjg5ZWMwMzI3NzI4ZTJiY2NkMDUxZjI4MTM3YzU3ZDc2YjFlOWY2ODcwOWY2MTAyZjM4NDBhMTJmYTg1MWE3NDBmIn0.eyJhdWQiOiIzIiwianRpIjoiOGQxMDY5ODY2YWNmMzEyODllYzAzMjc3MjhlMmJjY2QwNTFmMjgxMzdjNTdkNzZiMWU5ZjY4NzA5ZjYxMDJmMzg0MGExMmZhODUxYTc0MGYiLCJpYXQiOjE1NTkyOTYxMTAsIm5iZiI6MTU1OTI5NjExMCwiZXhwIjoxNTkwOTE4NTEwLCJzdWIiOiIyNTc3NyIsInNjb3BlcyI6WyIqIl19.D2fuWFG0svps6n2ynTsUmq-ycDCpeG9KwRQ9USLavGBu4kS_TGuaxJevWy7U3j8_9d8qY769SucBjo-FtBRDFRmamxIsn3GrL0R5VyP2Us0sUXqQ_ICTtEVvBMYsq2_JruEIOMBQ-iXPXkv1h5LRFf9P-3FDjXU3wetS6_7WqPs2pTluZIkeTNzqULEBuIShRgoaRtDpK8lntFgsAZU3VADcY0MHamte4Enu0qw997_yQrD2dG24Sgy6DbXY9WiRpQtNTDiDBlUNiVrIa7FHh6qbyhxrX_zyIs_hZDTyh4SGlG2ojPNFeF6sZcLo2KO8AfR9i-nuGJf8AwQ9i9vU8BwbhFazU7KdZ9XaJty9yJIutzDBgzs3e82oq1qfHVJe1vrlKxhX0WFJzXTWkGED3JHZQxs0baZEr5Sgel7Cq1BltWU_CENoY2j3nb6FDob0jlwZ9FdoF6ZWAyBHavNcrhC58gL_E_gQn-dRl4zWeKGNFDfSt6ptt7ewA6cJ2obLrRSBMhMoiSWQvrD5n3ZjMQ8ciWSVgD6p5nY1JwYBcWzulWvyanHEokmSM5MrLT2skdMNZxfTvuuXZgIQz868bqbyZPsYNJUZhSJpvAyhnT8JO2iYjg3dQbSyytCnm-xiQyo1dvzbvsmUxZgLbqNxMWUir11ll94xZxaFD1wtuPs",}
    #print(type( cookies))
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
    #response=mySession.post(url,data=fileContent.encode('utf-8'),headers=headers, cookies=cookies).json()
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
