#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   MySQLTest.py

@Time    :   2018/11/11 20:36

@Desc    :

"""

# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='1204', database='RUNOOB')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# print(cursor.rowcount)
# conn.commit()
# cursor.close()
#
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:1204@localhost:3306/RUNOOB')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
"""create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息;

'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'"""


class School(Base):
    __tablename__ = 'school'
    id = ...
    name = ...


# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询,filter是where条件,最后调用one()返回唯一行,如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
