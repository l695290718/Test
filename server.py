#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Ramberiu}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   server.py

@Time    :   2018/11/10 15:07

@Desc    :

"""
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    print(sock)
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

