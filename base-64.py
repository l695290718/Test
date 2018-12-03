#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   base64.py

@Time    :   2018/11/10 16:09

@Desc    :

"""

import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.b64decode('5p2l6IeqU01UUOeahOmXruWAmeKApuKApg=='))
print(bytes.decode(base64.b64decode('5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==')))
print(bytes.decode(base64.b64decode('566h55CG5ZGY')))
print(bytes.decode(b'\xc4\xfa\xc3\xbb\xd3\xd0\xc8\xa8\xcf\xde\xca\xb9\xd3\xc3\xb9\xa6\xc4\xdc', 'GBK'))




# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
sb = bytes(s, encoding="utf8")

# bytes to str
bs = str(b, encoding="utf8")

# an alternative method
# str to bytes
sb2 = str.encode(s)

# bytes to str
bs2 = bytes.decode(b)

