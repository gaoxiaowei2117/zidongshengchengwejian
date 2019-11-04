# -*- coding:utf8 -*-
import json
import sys
import os
import re
import random
import codecs
import linecache
import time
#from scripts import operate_MySQL
from scripts.operate_MySQL import MyMysql
from trans_baidu import translate_baidu
from trans_baidu import translate
from trans_baidu import TransFile
from autoSend import send_file_code_fromDB

sys.stdout=codecs.getwriter('utf8')(sys.stdout.detach())

BASE_DIR="/home/tools/Graphical/"
YUANWEN="./files/yuanwen.txt"
WAIWEN="./files/waiwen.txt"
YUANCHUANG="./files/yuanchuang.txt"

db = MyMysql(myHost='localhost',myUser='root', myPasswd='Nc480s><ltyyz', myPort=3306, myDB="91Creater")

def SelectPhases(phasesList, number):
    fileWriter=open(YUANWEN,'w',encoding='utf8')

    totalLen = 0
    phases_list = range(1,len(phasesList) - 1)
    phases_num = random.sample(phases_list, number)
    #for num in phases_num :
    for i in range(0, number) :
        num=phases_num[i]
        fileWriter.write(phasesList[num])
        fileWriter.write('\n')
        totalLen = totalLen + (len(phasesList[num]))
        if totalLen>900:
            break
    fileWriter.close()

def CreateFile(phasesList, picturesList, fileName):
    #for paraIndex in range(len(phasesList) - 1) :
        #print(paraIndex)
        #print(phasesList[paraIndex])

    picture_list = range(len(picturesList) - 1)
    picture_num = random.sample(picture_list, 2)

    fileWriter=open(fileName,'w',encoding='utf8')
    fileWriter.write('{"title":"{title_test}","keyword":["{testKey1}","{testKey2}","{testKey3}"],"is_ys":"","published_on_time":"","w":"w","content":"<div>')

    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><span style=\\"color: rgb(51, 51, 51); font-size: 14px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;\\\\\\\\5FAE软雅黑&quot;, Arial, sans-serif;\\">')
    fileWriter.write(phasesList[0])
    #print(phasesList[0])
    fileWriter.write('</span></p>')
    totalLen = (len(phasesList[0]))
    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><img src=\\"')
    fileWriter.write(picturesList[picture_num[0]])
    fileWriter.write('\\" alt=\\"\\"><br></p>')
    #for num in phases_num :
    for i in range(1, len(phasesList)) :
        num=i
        #num=phases_num[i]
        #print(num)
        #print(phasesList[num])
        fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><span style=\\"color: rgb(51, 51, 51); font-size: 14px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;\\\\\\\\5FAE软雅黑&quot;, Arial, sans-serif;\\">')
        fileWriter.write(phasesList[num])
        fileWriter.write('</span></p>')
        totalLen = totalLen + (len(phasesList[num]))
        if totalLen>1000:
            break
    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><img src=\\"')
    fileWriter.write(picturesList[picture_num[1]])
    fileWriter.write('\\" alt=\\"\\"><br></p></div>"}')
    fileWriter.close()
    #picture_list = range(len(phasesList))

def TitleAndKeys(taskRecord):
    first = random.sample(taskRecord[4].split(","), 1)
    second = random.sample(taskRecord[5].split(","), 1)
    third_1 = random.sample(taskRecord[6].split(","), 1)
    third_2 = random.sample(taskRecord[6].split(","), 1)
    
    title = ''.join(first+second+third_1)
    key1 = ''.join(first+second+third_1)
    key2 = ''.join(first+second)
    key3 = ''.join(first+second+third_2)
    #print(title,key1,key2,key3)
    return (title,key1,key2,key3)

def AutoTransAndCreate(taskRecord):
    phasesList = list(db.SelectPassages(str(taskRecord[1]), str(taskRecord[2])))
    #print(type(phasesList))
    picturesList = db.SelectPicture(str(taskRecord[1]), str(taskRecord[2]))
    productList = db.SelectProduct(str(taskRecord[1]), str(taskRecord[2]))

    p=re.compile('\n',re.S);
    #f= open(argv_1+'/phases','r',encoding='utf8')
    #fileContent = f.read()
    #phasesList=p.split(fileContent)
    #f.close()
    #print(type(phasesList))
    #f= open(argv_1+'/pictures','r',encoding='utf8')
    #fileContent = f.read()
    #picturesList=p.split(fileContent)
    #f.close()
    #f= open(argv_1+'/product','r',encoding='utf8')
    #fileContent = f.read()
    #productList=p.split(fileContent)
    #f.close()
    
    #　选取随机段落
    SelectPhases(phasesList, 15)
    #　生产原创文章
    TransFile(YUANWEN, YUANCHUANG, phasesList[0])
    #　生产网络格式的文章
    f= open(YUANCHUANG,'r',encoding='utf8')
    fileContent = f.read()
    phasesYuanChuangList=p.split(fileContent)
    f.close()
    fileName='files/0.txt'
    CreateFile(phasesYuanChuangList, picturesList, fileName)

    #　替换关键词
    title,key1,key2,key3=TitleAndKeys(taskRecord)
    f= open(fileName,'r',encoding='utf8')
    alllines=f.readlines()
    f.close()
    randomKeyWord=''
    while(len(randomKeyWord)==0):
        randomKeyWord=random.choice(productList)
    #print(randomKeyWord, type(randomKeyWord))
    f= open(fileName,'w',encoding='utf8')
    for eachline in alllines:
        a=re.sub('12358436',randomKeyWord,eachline)
        #print('-------------------',taskRecord[10]);
        a=re.sub('12358437',taskRecord[10],eachline)
        a=a.replace('{title_test}',title)
        a=a.replace('{testKey1}',key1)
        a=a.replace('{testKey2}',key2)
        a=a.replace('{testKey3}',key3)
        #print(a)
        f.writelines(a)
    f.close()

if __name__ == "__main__": 
#    if len(sys.argv) < 2:
#        print('python3 server.py {directory}')
#        print('eg: python3 server.py ./')
#        sys.exit()
    taskList = db.SelectTasks()
    for taskRecord in taskList:
        for times in range(0,taskRecord[3]) :
            breakFlag = 0
            i = 0
            while i<20 :
                AutoTransAndCreate(taskRecord)
                ret=send_file_code_fromDB(taskRecord)
                if ret['status']==200 :
                    print('Send file succeed. status:%d'%ret['status'])
                    break
                if ret['status']==500 :
                    if '每日可发文上限为' in ret['msg']:
                        print('Exceeding the maximum number of transmissions. status:%d'%ret['status'])
                        breakFlag = 1
                        break
                i=i+1
            if i>=20 :
                print('Send alert email!')
            if breakFlag == 1 :
                break
