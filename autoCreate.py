# -*- coding:utf8 -*-
import json
import sys
import os
import re
import random
import codecs
import linecache

sys.stdout=codecs.getwriter('utf8')(sys.stdout.detach())

BASE_DIR="/home/tools/Graphical/"

def CreateFile(phasesList, picturesList, number, fileName):
    fileWriter=open(fileName,'w',encoding='utf8')
    #for paraIndex in range(len(phasesList) - 1) :
        #print(paraIndex)
        #print(phasesList[paraIndex])
    phases_list = range(1,len(phasesList) - 1)
    phases_num = random.sample(phases_list, number)

    picture_list = range(len(picturesList) - 1)
    picture_num = random.sample(picture_list, 2)

    fileWriter.write('{"title":"{title_test}","keyword":["{testKey1}","{testKey2}","{testKey3}"],"is_ys":"","published_on_time":"","w":"w","content":"<div>')

    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><span style=\\"color: rgb(51, 51, 51); font-size: 14px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;\\\\\\\\5FAE软雅黑&quot;, Arial, sans-serif;\\">')
    fileWriter.write(phasesList[0])
    print(phasesList[0])
    fileWriter.write('</span></p>')
    totalLen = (len(phasesList[0]))
    fileWriter.write('<p style=\\"margin-bottom: 9px; color: rgb(115, 115, 115); font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, Arial, sans-serif; font-size: 13px;\\"><img src=\\"')
    fileWriter.write(picturesList[picture_num[0]])
    fileWriter.write('\\" alt=\\"\\"><br></p>')
    #for num in phases_num :
    for i in range(0, number) :
        num=phases_num[i]
        #print(num)
        print(phasesList[num])
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
    #picture_list = range(len(phaseseList))

def TitleAndKeys(path):
    if os.path.exists(path+'first'):
        count = len(open(path+'first',encoding='utf8').readlines())#获取行数
        firstnum=random.randrange(1,count+1, 1)#生成随机行数
        first=linecache.getline(path+'first',firstnum).rstrip('\n')#随机读取某行
    else:
        first=""
    print(first)
    count = len(open(path+'second',encoding='utf8').readlines())#获取行数
    secondnum=random.randrange(1,count+1, 1)#生成随机行数
    second=linecache.getline(path+'second',secondnum).rstrip('\n')#随机读取某行
    #print(second)
    count = len(open(path+'third',encoding='utf8').readlines())#获取行数
    thirdnum_1=random.randrange(1,count+1, 1)#生成随机行数
    third_1=linecache.getline(path+'third',thirdnum_1).rstrip('\n')#随机读取某行
    thirdnum_2=random.randrange(1,count+1, 1)#生成随机行数
    third_2=linecache.getline(path+'third',thirdnum_2).rstrip('\n')#随机读取某行
    #print(third)
    title = first+second+third_1
    key1 = first+second+third_1
    key2 = first+second
    key3 = first+second+third_2
    print(title,key1,key2,key3)
    return (title,key1,key2,key3)

if __name__ == "__main__": 
    if len(sys.argv) < 2:
        print('python3 server.py {directory}')
        print('eg: python3 server.py ./')
        sys.exit()
    #p=re.compile(\n',re.S);
    p=re.compile('\n',re.S);
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

    title,key1,key2,key3=TitleAndKeys(sys.argv[1])
    f= open(fileName,'r',encoding='utf8')
    alllines=f.readlines()
    f.close()
    f= open(fileName,'w',encoding='utf8')
    for eachline in alllines:
        a=re.sub(productList[0],productList[1],eachline)
        a=a.replace('{title_test}',title)
        a=a.replace('{testKey1}',key1)
        a=a.replace('{testKey2}',key2)
        a=a.replace('{testKey3}',key3)
        #print(a)
        f.writelines(a)
    f.close()
