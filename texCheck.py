# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 21:18:24 2014

@author: vespa
"""
import os
import re

def GetFileType(rootPath,Filetype):
    for path,subdir,files in os.walk(rootPath,topdown=False):
    	if len(files) == 0 or path.find(".") > 0:
    		continue
    	for filename in files:
    		if len(re.findall(r".*%s$"%(Filetype),filename)) > 0 :
    			yield path+os.sep+filename

def FindLabel(filename,Pre):
	labelSet = [];
	for (linenum,line) in enumerate(open(filename)):
		result = re.findall("%s\{\s*([^\}]*)\s*\}"%(Pre),line)
		for item in result:
			labelSet.append([linenum+1,item]);
	return labelSet;


def GetLabelDict(rootPath,Pre):
	labelDict = {}
	for filename in GetFileType(rootPath,"tex"):
	    labelSet = FindLabel(filename,Pre)
	    for line,label in labelSet:
	    	for labelsub in label.split(","):
		    	if labelDict.has_key(labelsub):
		    		labelDict[labelsub].append([line,filename])
		    	else:
		    		labelDict[labelsub] = [[line,filename]]
	return labelDict

def GetBibDict(rootPath):
	at_Flag = False
	curlabel = ""
	bibDict = {}
	curLineNum = -1;
	for filename in os.listdir(rootPath):
	    if not filename.endswith("bib"):
	        continue
	    for (linenum,line) in enumerate(open(rootPath+os.sep+filename)):
	    	find = re.findall(r"@\w+\s*\{([^,]*),",line)
	    	if find:
	    		if at_Flag:
	    			print("Title Not Found:",curlabel)
	    		else:
	    			at_Flag = True
	    			curlabel = find[0]
	    			curLineNum = linenum+1
	    		continue
	    	find = re.findall(r"^\s*title\s*=\s*[\{|\"]([^\}\"]*)[\}|\"]",line)
	    	if find:
	    		if bibDict.has_key(curlabel):
	    			bibDict[curlabel].append([curLineNum,filename,find[0]])
	    		else:
	    			bibDict[curlabel] = [[curLineNum,filename,find[0]]]
	    		at_Flag = False
	return bibDict

############### Main
if __name__ == "__thesis__":
	rootPath = "./"

	# Check Label repeat
	labelDict = GetLabelDict(rootPath,"label")
	hasLabelRepeat = False
	for label in labelDict:
		if len(labelDict[label]) > 1:
			hasLabelRepeat = True
			print ("ERROR!!!    Label '%s' is Repeat in these files:"%label)
			for (line,filename) in labelDict[label]:
				print ("%s(Line %d)"%(filename,line))
			print ("\n")

	if not hasLabelRepeat:
		print ("[OK!]No Label Definition Repeat!!\n")

	# Check Lable Defined
	labelUsed = GetLabelDict(rootPath,"ref")
	hasLabelUndefined = False
	for label in labelUsed:
		if not labelDict.has_key(label):
			hasLabelUndefined = True
			print ("ERROR!!!    Label '%s' is used but not DEFINED!!:"%(label))
			for (line,filename) in labelUsed[label]:
				print ("%s(Line %d)"%(filename,line))
			print ("\n")

	if not hasLabelRepeat:
		print ("[OK!]All Label Used is Defined!!\n")

	# Check Bib Label Repeat
	bibDict = GetBibDict(rootPath)
	hasBibLabelRepeat = False
	for label in bibDict:
		if len(bibDict[label]) > 1:
			hasBibLabelRepeat = True
			print ("=======================================================")
			print ("Bib Label %s is Redefined in these lines:\n"%(label))
			for item in bibDict[label]:
				print ("<<%s>>\nLine:%d\nFile:%s\n"%(item[2],item[0],item[1]))


	if not hasBibLabelRepeat:
		print ("[OK!]No Label Definition Used in *bib is Repeat!!\n")

	bibLabelUsed = GetLabelDict(rootPath,"cite")
	hasBibLabelUndefined = False
	for label in bibLabelUsed:
		if not bibDict.has_key(label):
			hasBibLabelUndefined = True
			print ("=======================================================")
			print ("Bib Label %s is Used in These Lines BUT NOT BEEN DEFINED:"%(label))
			for item in bibLabelUsed[label]:
				print ("File:%s(Line:%d)"%(item[1],item[0]))

	if not hasBibLabelUndefined:
		print ("[OK!]All Label Used in *tex is Defined in *bib!!\n")
	print ("Finished!!")


