#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import sys
import codecs
reload(sys) 
sys.setdefaultencoding("utf-8") 
print sys.getdefaultencoding() 
r = redis.Redis(host='114.215.85.245',port=6379,db=0)

fod = codecs.open("alphago.txt", "a+", encoding='UTF-8')
count = 6243

while 1:
    val = r.lindex('comments-alphago',count)
    if val:
        print val
        fod.write(str(val)+"\n")
    count = count - 1
    if count == -1:
        break
fod.close()
