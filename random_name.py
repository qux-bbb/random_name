# !python3
# coding:utf8

'''
随机姓名
姓用的是百家姓
名用的是汉语常见3500字
这两个都放在不同的txt文件里，可以自己更换，格式照着改就行了，最后别有空格
由于编码的原因，所以最好在命令行下使用
'''

import random

xings = open("xing.txt",'r').read().split(" ")
mings = open("ming.txt",'r').read().split(" ")


xings_o = random.randint(0,len(xings)-1)
xing = xings[xings_o]

ming = ""
for i in range(random.randint(1,2)):
	mings_o = random.randint(0,len(mings)-1)
	ming += mings[mings_o]

print(xing.decode("utf-8").encode("gbk") + ":" + ming.decode("utf-8").encode("gbk"))
