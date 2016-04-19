#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba,codecs
fow = codecs.open("../word/word.txt", "r", encoding='UTF-8')
fos = codecs.open("coae2014.txt", "r", encoding='UTF-8')
count = 4999
index = 1
dict = {}
list = []
fod = codecs.open("mlf.txt", "a+", encoding="UTF-8")
while 1:
    line = fow.readline()
    if line:
        line = line.strip()
  #      print line
        dict[line] = 0
        list.append(line)
        index = index + 1
    else:
        break
#for key in list:
 #   print key
print "++++++++++++++++++++++++++++++++++++++++++"
while 1:
    line = fos.readline()
    vector = ""
    if line:
        line = line.strip()
        tive =  line[-1]
        vector = vector + tive
        line3 = line[1:-3]
        seg_list = jieba.cut(line3, cut_all=True)
        for key in seg_list:
            key = key.replace("\n","")
            key = key.strip()
            if dict.has_key(key):
                #print key
                dict[key] = 1
                #vector = vector + " " + str(dict[key]) + ":1"
        for i in xrange(len(list)):
            if dict[list[i]] == 1:
                vector = vector + " " + str(i) + ":1"
                dict[list[i]] = 0
        print vector
        count = count + 1
    else:
        break
fos.close()
fod.close()
fow.close()

