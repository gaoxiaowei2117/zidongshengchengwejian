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

    #for num in phases_num :
    for i in range(0, number) :
        num=phases_num[i]
        #print(num)
        #print(phasesList[num])
        fileWriter.write(phasesList[num])
        fileWriter.write('\r\n')
        if i == number//2 - 1:
            fileWriter.write(picturesList[picture_num[0]])
            fileWriter.write('\r\n')
    fileWriter.write(picturesList[picture_num[1]])
    fileWriter.write('\r\n')
    fileWriter.close()
    #picture_list = range(len(phaseseList))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('python3 server.py phases pictures product')
        sys.exit()
    p=re.compile('{split}\n',re.S);
    f= open(sys.argv[1],'r',encoding='utf8')
    fileContent = f.read()
    phasesList=p.split(fileContent)
    f.close()
    f= open(sys.argv[2],'r',encoding='utf8')
    fileContent = f.read()
    picturesList=p.split(fileContent)
    f.close()
    f= open(sys.argv[3],'r',encoding='utf8')
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
