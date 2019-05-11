#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
from requests.cookies import cookiejar_from_dict

def update_Cookies_Authorization(user_agent):
    str = raw_input("Enter information of picture: ");
    print(str)
    myData = '{"username":"cfysxh01234","password":"yishang","captcha":"' + str + '","scope":"*","grant_type":"password","client_id":3,"client_secret":"CAMIGZh7K4wFCmGEYYzrPNneOR7pzTY2QUoADeYD"}'
    headers = {
        "Host": "member.91huoke.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "http://member.91huoke.com",
        "User-Agent": user_agent,
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "http://member.91huoke.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "91_session=eyJpdiI6IlZzMWJmeTRrdFVIbDNPdFNNMVJRZ3c9PSIsInZhbHVlIjoidWt5dytqUjRmd3g4a1NIcTVFOGVUMzRBN2Y2WVlOemJcL3JwblJqVFBxYXNURXZxbmlCbUY2NExaRGQxc0xoMW4iLCJtYWMiOiIzMzRjZWRlYjJiMjcyNjY0OTc2YWRlYTJjODlmMWYyNzk1MDc4ZTI5MzdhMjU2N2U0M2ZkMDcwM2Q4ZjUzNGE1In0%3D",
    }
    session = requests.Session()
    url = 'http://member.91huoke.com//oauth/token'
    #response = session.get(url, headers=headers).json()
    response=session.post(url,data=myData,headers=headers)
    print (response.headers)
    print (response.text)
    #captcha_url =  response.get('data').get('url')
    #captcha_response = session.get(captcha_url, headers=headers)
    #with open('captcha.png','wb') as captcha_image:
    #    captcha_image.write(captcha_response.content)

def get_captcha_code(user_agent):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "member.91huoke.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user_agent,
    }
    session = requests.Session()
    url = 'http://member.91huoke.com/member/code'
    #response = session.get(url, headers=headers).json()
    responsed = session.get(url, headers=headers)
    print (responsed.headers['Set-Cookie'])
    response = responsed.json()
    print (response)
    captcha_url =  response.get('data').get('url')
    captcha_response = session.get(captcha_url, headers=headers)
    with open('captcha.png','wb') as captcha_image:
        captcha_image.write(captcha_response.content)
if __name__ == '__main__':
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    get_captcha_code(user_agent)
    update_Cookies_Authorization(user_agent)
