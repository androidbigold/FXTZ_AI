# coding:utf-8
from ctypes import *
import time

# ����dll�ļ�
dd_dll = windll.LoadLibrary('DD85590.64.dll')

# DD������
vk = {'a': 401, 's': 402, 'd': 403, 'w': 302}


# ����һ�鰴����1���£�2�ɿ�
def down_up(code):
    dd_dll.DD_key(vk[code], 1)
    dd_dll.DD_key(vk[code], 2)

if __name__ == '__main__':
    while True:
        down_up('a')



