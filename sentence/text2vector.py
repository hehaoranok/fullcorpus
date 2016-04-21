#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba,codecs,redis
r = redis.Redis(host='114.215.85.245',port=6379,db=0)
fow = codecs.open("../word/seg.txt", "r", encoding='UTF-8')
#fos = codecs.open("alphago.txt", "r", encoding='UTF-8')
count = 6244
index = 1
dict = {}
list = []
fod1 = codecs.open("alphago_vector1.txt", "a+", encoding="UTF-8")
fod0 = codecs.open("alphago_vector0.txt", "a+", encoding="UTF-8")
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
    flag = 0
    line = r.lindex('comments-alphago',count)
    print line
    vector = ""
    if line:
        line3 = line.strip()
        seg_list = jieba.cut(line3, cut_all=True)
        for key in seg_list:
            key = key.replace("\n","")
            key = key.strip()
            if dict.has_key(key):
                #print key
                dict[key] = 1
                #vector = vector + str(dict[key]) + ":1" + " "
        for i in xrange(len(list)):
            if dict[list[i]] == 1:
                vector = vector + str(i )+":1" + " "
                dict[list[i]] = 0
                flag = 1
        print vector
        if flag == 1:
            fod1.write("+1 " + vector+"\n")
            fod0.write("-1 " + vector+"\n")
    count = count - 1
    if count == -1:
        break
#fos.close()
fod1.close()
fod0.close()
fow.close()


