#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import sys
import codecs
import jieba
reload(sys) 
sys.setdefaultencoding("utf-8") 
print sys.getdefaultencoding() 
r = redis.Redis(host='114.215.85.245',port=6379,db=0)

fod = codecs.open("COAE2014_4_data.txt", "r", encoding='UTF-8')
fos = open("coae2014.txt", "w+")
count = 4999
flag = 1
val=''
index=0
findex=0
sent=0

while 1:
    line = fod.readline()
    if not line:
        break
    start = line.find('Doc')
    end = line.find('>')
    dindex = int(line[(start+3):end])
    print 'dindex:'+str(dindex)
    if flag == 1:
        if count == -1:
            break
        val = r.lindex('pingce-answer',count)
        index = val.find('=')
        findex = int(val[:index])
        print findex
        sent  = int(val[(index+1):])
        if sent == -1:
            sent = 0
        print sent
        count = count - 1
        flag = 0
    else:
        pass
    print 'dindex-findex'+str(dindex)+'---'+str(findex)
    if dindex == findex:
        flag = 1
        part = line[(end+1):]
        pend = part.find('<')
        vals = line[(end+1):pend]
        seg_list = jieba.cut(vals, cut_all=False)
        values = " ".join(seg_list)
        print values
        ends = "'"+values+"',"+str(sent)+'\n'
        fos.write(str(ends))    
    else:
        pass
fos.close()
fod.close()

