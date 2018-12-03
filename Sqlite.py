#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   Sqlite.py

@Time    :   2018/11/11 18:52

@Desc    :

"""

# # 导入SQLite驱动:
# import sqlite3
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在,会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句,创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 继续执行一条SQL语句,插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# # 通过rowcount获得插入的行数:
# cursor.rowcount
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()

# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# #执行查询语句:
# cursor.execute('select * from user where id=?', ('1',))
# #获得查询结果集:
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

"""多个参数    cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))     """

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


def takeThird(elem):
    return elem[:][2]


def get_score_in(low, high):
    cursor.execute('select * from user where score>? AND score<? ', (low, high))
    values = cursor.fetchall()
    result = sorted(values, key=(lambda x: x[:][2]))
    print(result)


conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
print(get_score_in(60, 100))
cursor.close()
conn.commit()
conn.close()
