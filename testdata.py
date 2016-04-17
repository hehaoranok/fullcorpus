import redis,codecs

r = redis.Redis(host='114.215.85.245',port=6379,db=0)

count = 6243
fod = open("./experiment/alphago.txt", "w")
while 1:
    print "================",count
    data = r.lindex('comments-alphago',count)
    fod.write(data+',0\n')
    count = count - 1
    if count == -1:
        break
fod.close()
