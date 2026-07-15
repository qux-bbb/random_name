#!/usr/bin/env python3
# coding:utf8

'''
随机姓名生成器
姓用的是百家姓（xing.txt）
名用的是汉语常见3500字（ming.txt）
这两个txt文件可以自己更换，格式照着改就行，最后别有空格

用法：
  random_name.py                     # 默认 xing.txt + ming.txt
  random_name.py --ming ming_男.txt  # 指定名字文件
  random_name.py -x 其他姓.txt -m ming_女.txt  # 同时指定姓和名
'''

import os
import random
import argparse

# 获取脚本所在目录，保证从任何路径运行都能找到数据文件
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 默认文件名
DEFAULT_XING = 'xing.txt'
DEFAULT_MING = 'ming.txt'


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
    parser = argparse.ArgumentParser(description='随机中文姓名生成器')
    parser.add_argument(
        '--xing', '-x',
        default=DEFAULT_XING,
        help=f'姓氏字库文件（默认: {DEFAULT_XING}）'
    )
    parser.add_argument(
        '--ming', '-m',
        default=DEFAULT_MING,
        help=f'名字字库文件（默认: {DEFAULT_MING}）'
    )
    args = parser.parse_args()

    xings = load_words(args.xing)
    mings = load_words(args.ming)
    name = generate_name(xings, mings)
    print(name)


if __name__ == '__main__':
    main()
