import redis,codecs,jieba

r = redis.Redis(host='114.215.85.245',port=6379,db=0)

count = 6243
fod = codecs.open("./experiment/alphago0.txt", "w",encoding="UTF-8")
while 1:
    print "================",count
    data = r.lindex('comments-alphago',count)
    seg_list = jieba.cut(data, cut_all=False)
    values = " ".join(seg_list)
    fod.write("'"+values+"',0\n")
    count = count - 1
    if count == -1:
        break
fod.close()
