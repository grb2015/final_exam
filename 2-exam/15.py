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
def q15a(x,y):
    a = x*y
    b = q15b(a)
    print('#2')   #2
    print(b)   #2 = 20
    return None
def q15b(x):
    print('#1')   
    print(x)   #1    =2
    x *= 10
    print('#3')   
    print(x)
    return x
t = q15a(1,2)




