#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
r = redis.Redis(host='114.215.85.245',port=6379,db=0)

fod = open("COAE2014_4_data.txt", "r")
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
        val = r.lindex('pingce-answer',count)
        index = val.find('=')
        findex = int(val[:index])
        print findex
        sent  = int(val[(index+1):])
        print sent
        flag = 0
    else:
        pass
    print 'dindex-findex'+str(dindex)+'---'+str(findex)
    if dindex == findex:
        flag = 1
        part = line[(end+1):]
        pend = part.find('<')
        vals = line[(end+1):pend]+','+str(sent)+'\n'
        print vals
        fos.write(vals)    
    else:
        pass
fos.close()
fod.close()

