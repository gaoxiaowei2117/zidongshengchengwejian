# -*- coding:utf8 -*-
import json
import sys
import os
import re
import random
import codecs
sys.stdout=codecs.getwriter('utf8')(sys.stdout.detach())

BASE_DIR="/home/tools/Graphical/"

def CreateFile(phasesList, picturesList, number, fileName):
    fileWriter=open(fileName,'w',encoding='utf8')
    #for paraIndex in range(len(phasesList) - 1) :
        #print(paraIndex)
        #print(phasesList[paraIndex])
    phases_list = range(len(phasesList) - 1)
    phases_num = random.sample(phases_list, number)

    picture_list = range(len(picturesList) - 1)
    picture_num = random.sample(picture_list, 2)

    fileWriter.write('{"title":"title_test","keyword":["testKey1","testKey2"],"is_ys":"","published_on_time":"","w":"w","content":"<div>')

    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><span style=\\"color: rgb(51, 51, 51); font-size: 14px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;\\\\\\\\5FAE软雅黑&quot;, Arial, sans-serif;\\">')
    fileWriter.write(phasesList[0])
    fileWriter.write('</span></p>')
    totalLen = (len(phasesList[0]))
    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><img src=\\"')
    fileWriter.write(picturesList[picture_num[0]])
    fileWriter.write('\\" alt=\\"\\"><br></p>')
    #for num in phases_num :
    for i in range(0, number) :
        num=phases_num[i]
        #print(num)
        #print(phasesList[num])
        fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><span style=\\"color: rgb(51, 51, 51); font-size: 14px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;\\\\\\\\5FAE软雅黑&quot;, Arial, sans-serif;\\">')
        fileWriter.write(phasesList[num])
        fileWriter.write('</span></p>')
        totalLen = totalLen + (len(phasesList[num]))
        if totalLen>900:
            break
    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><img src=\\"')
    fileWriter.write(picturesList[picture_num[1]])
    fileWriter.write('\\" alt=\\"\\"><br></p></div>"}')
    fileWriter.close()
    #picture_list = range(len(phaseseList))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('python3 server.py {directory}')
        print('eg: python3 server.py ./')
        sys.exit()
    p=re.compile('{split}\n',re.S);
    f= open(sys.argv[1]+'/phases','r',encoding='utf8')
    fileContent = f.read()
    phasesList=p.split(fileContent)
    f.close()
    f= open(sys.argv[1]+'/pictures','r',encoding='utf8')
    fileContent = f.read()
    picturesList=p.split(fileContent)
    f.close()
    f= open(sys.argv[1]+'/product','r',encoding='utf8')
    fileContent = f.read()
    productList=p.split(fileContent)
    f.close()
    print("*"*10)

    fileName='files/0.txt'
    CreateFile(phasesList, picturesList, 7, fileName)

    f= open(fileName,'r',encoding='utf8')
    alllines=f.readlines()
    f.close()
    f= open(fileName,'w',encoding='utf8')
    for eachline in alllines:
        a=re.sub(productList[0],productList[1],eachline)
        print(a)
        f.writelines(a)
    f.close()
