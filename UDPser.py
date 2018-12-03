#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Ramberiu}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   UDPser.py

@Time    :   2018/11/10 15:17

@Desc    :

"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    data, addr = s.recvfrom(1024)
    print('Received %s:%s' % addr)
    s.sendto(b'Hello, %s' % data, addr)

