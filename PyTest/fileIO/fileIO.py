# -*- coding: utf-8 -*-

import os

#파일명
fileName = "sample.txt"
#파일 경로
filePath = "C:\\Project\\git\\PyTest\\PyTest\\fileIO\\dir"

print (os.getcwd())
print (filePath)
#print(os.path.isdir(filePath))
print('=' *30)

if os.path.isdir(filePath) == False:
    # 디렉토리 생성
    os.mkdir(filePath)
    #print("디렉토리 생성 ")

if os.path.isfile(filePath + "\\" + fileName):
    # 파일이 존재 하면 appending 처리
    with open(filePath + "\\" + fileName, 'a') as f:
        for i in range(1, 11):
            data = "%d번째 줄입니다.\n" % i
            f.write(data)
else:
    # 파일이 존재하지 않으면 신규로 생성하여 쓰기.
    f = open(filePath + "/" + fileName,'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
        
# 파일 읽기
# 1.모든 라인을 읽기
with open(filePath + "/" + fileName, 'r') as f:
    for line in f.readlines():
        print(line)

print('=' *30)
    
# 2. 한 라인씩 읽기
with open(filePath + "/" + fileName, 'r') as f:
    print(f.readline())

print('=' *30)

# 3. 전체 내용을 읽기
with open(filePath + "/" + fileName, 'r') as f:
    content = f.read()
    print(content)
    
    
    
    