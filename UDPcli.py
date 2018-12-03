#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Ramberiu}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   UDPcli.py

@Time    :   2018/11/10 15:17

@Desc    :

"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
