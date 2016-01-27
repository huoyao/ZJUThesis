
#coding=utf-8
import os
import re
from re import split #for  english word counting
# import chardet
## https://pypi.python.org/pypi/chardet

def GetFileType(rootPath,Filetype):
    for path,subdir,files in os.walk(rootPath,topdown=False):
        if len(files) == 0 or path.find(".") > 0:
            continue
        for filename in files:
            if len(re.findall(r".*%s$"%(Filetype),filename)) > 0 :
                yield path+os.sep+filename

def IsChinese(c):
    if c >= u'\u4e00' and c<=u'\u9fa5':
        return True
    else:
        return False

def CountLineNum(line):
    num = 0
    #line=line.decode('gbk')
    for ch in line:
        if IsChinese(ch):
            num+=1
    return num

def CountTexNumCN(filename):
    print (filename)
    letterNum = 0
    with open(filename, "rU",encoding="utf-8") as f:
        for line in f.readlines():
            letterNum += CountLineNum(line)
    return letterNum

def CountTexNumEN(filename):
    counter = 0
    letterNum=0
    with open(filename, "rU",encoding="utf-8") as f:
        for word in f.read().split():
            #print(word) #for debuging
            if word[0]<='z' and word[0]>='a' or word[0]<='Z' and word[0]>='a':
                counter+=1
    return counter

def CountTexNum(filename):
    cnNum=CountTexNumCN(filename)
    enNum=CountTexNumEN(filename)
    print ("CN:",cnNum,",","EN:",enNum)
    return (cnNum,enNum)

def Run():
    rootpath = "./Chapters"
    chineseNum = 0
    englishNum=0
    for filename in GetFileType(rootpath,"tex"):
        cnNum,enNum=CountTexNum(filename)
        chineseNum+=cnNum
        englishNum+=enNum
    cnNum,enNum=CountTexNum("./thesisbib.bib")
    chineseNum+=cnNum
    englishNum+=enNum
    print ("\nChinese:",chineseNum,",English:",englishNum)
    print ("Total:",chineseNum+englishNum)

Run()