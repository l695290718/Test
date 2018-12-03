#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   hello.py.py

@Time    :   2018/11/12 22:04

@Desc    :

"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
