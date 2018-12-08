# coding:utf-8
from ctypes import *
import time

# 调用dll文件
dd_dll = windll.LoadLibrary('DD85590.64.dll')

# DD虚拟码
vk = {'a': 401, 's': 402, 'd': 403, 'w': 302}


# 进行一组按键，1按下，2松开
def down_up(code):
    dd_dll.DD_key(vk[code], 1)
    dd_dll.DD_key(vk[code], 2)

if __name__ == '__main__':
    while True:
        down_up('a')



