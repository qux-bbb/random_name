#!/usr/bin/env python3
# coding:utf8

'''
随机姓名生成器
姓用的是百家姓（xing.txt）
名用的是汉语常见3500字（ming.txt）
这两个txt文件可以自己更换，格式照着改就行，最后别有空格
'''

import os
import random

# 获取脚本所在目录，保证从任何路径运行都能找到数据文件
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_words(filename):
    """从txt文件加载词库，按空格分割"""
    path = os.path.join(SCRIPT_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip().split(' ')

def generate_name(xings, mings):
    """随机生成一个中文姓名"""
    xing = random.choice(xings)
    # 名字1~2个字
    ming_len = random.randint(1, 2)
    ming = ''.join(random.choice(mings) for _ in range(ming_len))
    return xing + ':' + ming

def main():
    xings = load_words('xing.txt')
    mings = load_words('ming.txt')
    name = generate_name(xings, mings)
    print(name)

if __name__ == '__main__':
    main()
