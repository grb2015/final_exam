#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     13-14.py
#   breif��
#   history:   2017-08-17renbin.guo created
#   usage��
#   note�� 
#
#================================================================
def q13a(x,y):
    a = x*y
    b = q13b(a)
    print('#2')   #2
    print(b)   #2 = 20
    return None
def q13b(x):
    print('#1')   
    print(x)   #1    =2
    x *= 10
    print('#3')   
    print(x)
    return None
t = q13a(1,2)


'''
[root@localhost final_exam]# python 13-14.py 
#1
2
#3
20
#2
None
[root@localhost final_exam]# 
'''


