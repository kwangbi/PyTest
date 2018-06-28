# -*- coding: utf-8 -*-

import os
import codecs
import sys


print (os.getcwd()) #현재 디렉토리의
print (os.path.realpath(__file__))#파일
print (os.path.dirname(os.path.realpath(__file__)) )#파일이 위치한 디렉토리



fileName = "sample.txt"
filePath = os.getcwd()
fileFullName = filePath + "\\" + fileName

with codecs.open('test.out', 'w') as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
        