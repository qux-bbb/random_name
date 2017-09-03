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
import platform

xings = open("xing.txt",'r').read().split(" ")
mings = open("ming.txt",'r').read().split(" ")

xing = random.choice(xings)

ming = ""
for i in range(random.randint(1,2)):
	ming += random.choice(mings)

# 根据操作系统选择输出方式，支持linux和windows
now_plat = platform.system()
if now_plat == "Linux":
	print(xing + ":" + ming)
else:
	print(xing.decode("utf-8").encode("gbk") + ":" + ming.decode("utf-8").encode("gbk"))

