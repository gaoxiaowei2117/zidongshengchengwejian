# -*- coding:utf8 -*-
import json
import sys
import os
import re
import random
import codecs
import linecache

sys.stdout=codecs.getwriter('utf8')(sys.stdout.detach())


def CheckFile(phasesList, fileName):
    fileWriter=open(fileName,'w',encoding='utf8')
    for paraIndex in range(len(phasesList) - 1) :
        print(paraIndex)
        print(phasesList[paraIndex])
        if len(phasesList[paraIndex])<150:
            #fileWriter.write(paraIndex, len(phasesList[paraIndex]), phasesList[paraIndex]) 
            fileWriter.write(str(paraIndex+1)+',') 
            fileWriter.write(str(len(phasesList[paraIndex]))+',') 
            fileWriter.write(phasesList[paraIndex]) 
            fileWriter.write('\n') 
    fileWriter.close()

if __name__ == "__main__": 
    if len(sys.argv) < 2:
        print('python3 %s {directory}'%argv[0])
        print('eg: python3 %s ./test'%argv[0])
        sys.exit()
    #p=re.compile(\n',re.S);
    p=re.compile('\n',re.S);
    f= open(sys.argv[1],'r',encoding='utf8')
    fileContent = f.read()
    phasesList=p.split(fileContent)
    f.close()
    fileName='files/1.txt'
    CheckFile(phasesList, fileName)
