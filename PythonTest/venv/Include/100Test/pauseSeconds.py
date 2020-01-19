#
#
# 题目：暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    time.sleep(1)
    print(key, value)
