#!/usr/bin/python
# -*- coding: UTF-8 -*-
fos = open("negtive.txt", "r")
fod = open("rnegtive.txt", "w+")
while 1:
    line = fos.readline()
    if line:
        print line
        indexl = line.find('>')
        line2 = line[(1+indexl):]
        print line2
        indexr = line2.find('<')
        line3 = line2[0:indexr]
        print line3
        linev = line3 + ',0'+'\n'
        print linev
        fod.write(linev)
    else:
        break
fos.close()
fod.close()
