#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {YourName}

@License :   (C) Copyright 2013-2017, {YourCompany}

@Contact :   {YourEmail}

@Software:   PyCharm

@File    :   mydict.py

@Time    :   2018/10/22 21:43

@Desc    :

"""


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


