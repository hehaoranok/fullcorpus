#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import sys
import codecs
import jieba
reload(sys) 
sys.setdefaultencoding("utf-8") 
print sys.getdefaultencoding() 
fod = codecs.open("COAE2014_4_data.txt", "r", encoding='UTF-8')
val=''
index=0
findex=0
sent=0
fos = open("countword.txt", "w+")
while 1:
    line = fod.readline()
    if not line:
        break
    start = line.find('>')
    line = line[(start+1):]
    end = line.find('<')
    vals = line[:end]
    seg_list = jieba.cut(vals, cut_all=True)
    for k in seg_list:
        print k
        fos.write(str(k)+"\n")    
fos.close()
fod.close()
