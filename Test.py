# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#
# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])


# # 对切片对象判断
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
#
# f = Fib()
# print(f[:10])


# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     # def __getattr__(self, attr):
#     #     if attr == 'score':
#     #         return 99
#     def __getattr__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
#
# s = Student()
# print(s.name)
# # print(s.score)
# print(s.age())
# print(s.score)


# 链式调用API
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
#
# s = Chain()
# print(s.status.user.timeline.list)


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
#
# s = Student('Michael')
# print(s())
#
# print(callable(s))
# print(callable(Student))
# print(callable([1, 2, 3, 4]))

# ## 枚举型
# from enum import Enum, unique
#
# # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # for name, member in Month.__members__.items():
# #     print(name, '=>', member, ',', member.value)
#
#
# @unique
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(Weekday(1))

# def fn(self, name='world'):
#     print('Hello, %s' % name)
#
#
# ##注意Tuple单元素写法
# """"要创建一个class对象,type()函数依次传入3个参数;
# class的名称；
# 继承的父类集合,注意Python支持多重继承,如果只有一个父类,别忘了tuple的单元素写法；
# class的方法名称与函数绑定,这里我们把函数fn绑定到方法名hello上。"""
# Hello = type('Hello', (object,), dict(hello=fn))
# h = Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))

# try:
#     print('try...')
#     r = 10 / 0
#     print('result', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
#
# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error', e)
#     finally:
#         print('finally')
#
#
# print(main())

# import logging
#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
#
# print(main())
# print('END')

# # 在必要的时候才定义我们自己的错误类型
# class FooError(ValueError):
#     pass
#
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
#
# foo('0')

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()

# #启动Python解释器时可以用-O参数来关闭assert
# def foo(s):
#     n = int(s)
#     assert n != 0
#     return 10 / n
# def main():
#     foo('0')
#
# print(main())


# #debug,info,warning,error
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# #pdb调试
# s = '0'
# n = int(s)
# print(10 / n)

# import pdb
# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10 / n)

# import unittest
# from mydict import Dict
#
#
# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
#
# if __name__ == '__main__':
#     unittest.main()
# #连接数据库用
# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')

# import re
# m = re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))
#
# def abs(n):

# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

# 如果文件很小,read()一次性读取最方便；如果不能确定文件大小,反复调用read(size)比较保险；如果是配置文件,调用readlines()最方便
# f = open('C:/Users/Ramberiu/test.txt', 'r')
# print(f.read())
# f.close()
#
# try:
#     f = open('C:/Users/Ramberiu/test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open('C:/Users/Ramberiu/test.txt', 'r') as f:
#     print(f.read())
#
# with open('C:/Users/Ramberiu/test.txt', 'rb') as f:
#     print(f.read())
# with open('C:/Users/Ramberiu/test.txt', 'r', encoding='gbk') as f:
#     print(f.read())
# with open('C:/Users/Ramberiu/test.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())

# with open('C:/Users/Ramberiu/test.txt', 'w') as f:
#     f.write('Good')
# with open('C:/Users/Ramberiu/test.txt', 'r') as f:
#     print(f.read())

# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())
#
# f = StringIO('Hello!\nHi\nGoodbye')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.stripm())

# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())

# import os
#
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))
#
# print(os.path.abspath('.'))
# print(os.path.join('F:\PycharmProjects\Test', 'testdir'))  # 把两个路径合成一个
# os.mkdir(r'F:\PycharmProjects\Test\testdir')  # 然后创建一个目录:
# os.rmdir(r'F:\PycharmProjects\Test\testdir')  # 删掉一个目录:
#
# print(os.path.split(r'F:\PycharmProjects\Test\file.txt'))  # 拆分路径
# print(os.path.splitext(r'F:\PycharmProjects\Test\file.txt'))  # 得到扩展名
# # shutil 提供copyfile()函数
# # 过滤文件
# print([x for x in os.listdir('.') if os.path.isdir(x)])  # 列出所有目录
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1] == '.py'])  # 列出所有的.py文件

# import pickle
# # d = dict(name='bob', age='20', score=88)
# # print(pickle.dumps(d))
# # f = open('dump.txt', 'wb')
# # pickle.dump(d, f)
# # f.close()
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import json
# d = dict(name='bob', age=20, score=88)
# print(json.dumps(d))  # **********dumps()方法返回一个str,内容就是标准的JSON*********
#
# json_str = '{"age":20, "score":88, "name": "bob"}'
# print(json.loads(json_str))  # ***********8把JSON反序列化为Python对象*************
#
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# s = Student('Bob', 20, 88)
# # print(json.dumps(s))
#
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
#
# print(json.dumps(s, default=student2dict))  # *******这两句等效********
# print(json.dumps(s, default=lambda obj: obj.__dict__))
#
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
#
# json_str = '{"name": "Bob", "age": 20, "score": 88}'
# print(json.loads(json_str, object_hook=dict2student))  # ***********反序列化***********
# temp = json.loads(json_str, object_hook=dict2student)  # *********实例化**********
# print(temp.name)

# from multiprocessing import Process
# import os
#
#
# def run_proc(name):
#     print("Run child process %s (%s)..." % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()  # *********************等待子进程结束后再继续往下运行,通常用于进程间的同步。**************************
#     print('Child process end.')

# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#     # print(start)
#     # print(time.sleep(random.random() * 3))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(8)
#     for i in range(9):
#         p.apply_async(long_time_task, args=(i, ))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code', r)
#
#
# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
#
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))    # windows 默认用GBK编码 utf-8报错**********************
# print('Exit code:', p.returncode)

# # ***************进程间通信***************
# from multiprocessing import Process, Queue
# import os, time, random
# #*************写数据进程执行的代码*************
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue' % value)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()  # ****************pr进程里是死循环,无法等待其结束,只能强行终止:

# import time, threading
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')  # 名字可以不起 python默认
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)

# import time, threading
#
# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# **********死循环*******************
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
#
# import multiprocessing
# print(multiprocessing.cpu_count())

# # ***********************ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。******
# import threading
#
# local_school = threading.local()
#
#
# def process_student():
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name="Thread-B")
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# # 正则表达式re  ****************************************
# import re
#
# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')
#
# print('a b   c'.split(' '))
# print(re.split(r'\s+', 'a b   c'))  # ***************least one space
# print(re.split(r'[\s\,]+', 'a,b, c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m)
# print(m.group(0), m.group(1), m.group(2))
#
# t = '19:05:30'
# m = re.match(
#     r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
#     t)
# print(m.groups())
#
# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # more ?
#
# re_telephone = re.compile(r'(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())
# print(re_telephone.match('010-8086').groups())

# from datetime import datetime  # ********有注意事项 如果仅导入import datetime,则必须引用全名datetime.datetime
#
# now = datetime.now()
# print(now)
# print(type(now))
#
# dt = datetime(2015, 4, 19, 12, 20)
# print(dt)
#
# print(dt.timestamp())
# print(now.timestamp())
#
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))  # -8
#
# print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
# print(now.strftime('%a, %b %d %H:%M'))
#
# from datetime import timedelta
#
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
# print(now + timedelta(days=2, hours=12))
#
# from datetime import timezone
#
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# print(utc_dt.astimezone(timezone(timedelta(hours=8))))

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)
# print(isinstance(p, Point))
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
#
# from collections import deque
#
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)
#
# from collections import defaultdict
#
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'], dd['key2'])
#
# from collections import OrderedDict   # order dict   the key order the order
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# # collections*********************************************
# ******************OrderedDict create a FIFO***************
# from collections import OrderedDict
#
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)


# # chainmap****************************************
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob
# from collections import ChainMap
# import os, argparse
#
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
#
# combined = ChainMap(command_line_args, os.environ, defaults)
#
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

# *******************统计字符个数**************
# from collections import Counter
# c = Counter()
# for ch in 'Programming':
#     c[ch] = c[ch] + 1
# print(c)

# # base64************************
# import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#
# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# # struct************************
# import struct
#
# print(struct.pack('>I', 10240099))
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# with open('C:/Users/Ramberiu/Desktop/test.bmp', 'rb') as f:
#     print(f.read())

# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())


# # 模拟用户登录  hashlib******************
# import hashlib, random
#
#
# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
#
#
# def login(username, password):
#     user = db[username]
#     return user.password == get_md5(password + user.salt)
#
# print(login('michael', '123456'))

# import hmac
# message = b'Hello world'
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# print(h.hexdigest())

# # use hmac- ***************
# import hmac, random
#
#
# def hmac_md5(key, s):
#     return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = hmac_md5(self.key, password)
#
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
#
#
# def login(username, password):
#     user = db[username]
#     return user.password == hmac_md5(user.key, password)
#
# print(login('michael', '123456'))


# ## ***************itertools*************
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#     if n == 999:
#         raise ValueError('END')

# import itertools
# i = 0
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
#     i += 1
#     if i == 100:
#         raise ValueError('END')

# # 定次数的重复输出 itertools ******************************************
# import itertools
#
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)
#
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
#
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)
#
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))
#
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))

# # 计算pi**********************************
# import itertools
#
# listB = []
#
#
# def pi(N):
#     natuals = itertools.count(1, 2)
#     ns = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals)
#     listA = list(ns)
#     print(listA)
#     for i in range(len(listA)):
#         if i % 2 != 0:
#             listB.append(-4 / listA[i])
#         else:
#             listB.append(4 / listA[i])
#     print(sum(listB))
#
#
# pi(999)

# # enter exit**************************
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# with Query('Bob') as q:
#     q.query()

# # contextlib ***************** 简化 enter exit
# from contextlib import contextmanager
#
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
#
#
# with create_query('Bob') as q:
#     q.query()

# # 代码前后自动执行特定代码
#
# from contextlib import contextmanager
#
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
# with tag("h1"):
#     print('hello')
#     print('world')

# # urlopen 打印出网站 ******************************
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)

# # urllib*************                                      GET
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data', data.decode('utf-8'))
#
# # 伪装成iphone6
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, '
#                              'like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data', f.read().decode('utf-8'))

# # POST ************************** 模仿微博登陆
# from urllib import request, parse
#
# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('http://passport.weibo.cn/sso/login') req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML,
# like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') req.add_header('Referer',
# 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data', f.read().decode('utf-8'))

# # handler 更复杂的控制 Proxy
# import urllib
# from urllib import request
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

# # json 序列化为Python 对象
# import json
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data', data.decode('utf-8'))
#     print('#########################################################################')
#     print(json.loads(data.decode('utf-8')))


# # 读取XML
# from base64 import encode
# from xml.parsers.expat import ParserCreate
#
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:stast_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)


# # 生成XLM
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# return''.join(L)

# #获取天气预报 如何提取出信息？
# from xml.parsers.expat import ParserCreate
# from urllib import request
#
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D' \
#       '%202151330&format=xml '
#
# with request.urlopen(URL, timeout=10) as f:
#     data = f.read()
#
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:stast_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(data.decode('utf-8'))

# # HTMLParser解析HTML
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s' % name)
#
#     def handle_charref(self, name):
#         print('&#%s:' % name)
#
#
# parser = MyHTMLParser()
#
#
# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org/events/python-events/')) as page:
#     # print(page.read().decode('utf-8'))
#     # for line in page:
#     parser.feed(page.read().decode('utf-8'))

# pillow***********************************
# from PIL import Image, ImageFilter
#
# # 修改图片大小
# im = Image.open('test.jpg')
# w, h = im.size
# print("Original image size: %s%s" % (w, h))
# im.thumbnail((w // 2, h // 2))
# print('Resize image to: %sx%s' % (w // 2, h // 2))
# im.save('thumbnail.jpg', 'jpeg')
#
# # 图像模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')
#
# # 验证码制作
# from PIL import ImageDraw, ImageFont
# import random
#
#
# def rndChar():
#     return chr(random.randint(65, 90))
#
#
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
#
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
#
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
#
# font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# draw = ImageDraw.Draw(image)
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=(rndColor()))
#
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
# image.show('code.jpg')


# # GET ***************************
# import requests
# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)
# rp = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'}) # 带参数的请求
# print(rp.url) # 实际请求的URL
# print(r.encoding) # 自动检测编码
# print(r.content) # 获得byte对象
#
# # 转换为json
# rj = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid'
#                   '%20%3D%202151330&format=json')
# print(rj.json())
#
# # 传入HTTP Header 传入dict作为参数
#
# rd = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like
# Mac ' 'OS X) AppleWebKit'}) print(rd.text)

# # POST
# import requests  # POST默认编码 application/x-www-form-urlencoded
#
# r = requests.post('https://accounts.douban.com/login',
#                   data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r)

# #可直接传入JSON数据
# params = {'key': 'value'}
# r = requests.post(url, json=params)

# # 上传文件 在读取文件时,注意务必使用'rb'即二进制模式读取,这样获取的bytes长度才是文件的长度。
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

# # 获取相应头
# import requests
# r = requests.get('https://www.douban.com/')
# print(r.headers)
# print(r.headers['Content-Type'])

# # 获取cookie
# print(r.cookies)

# # 请求中传入Cookie use dict
# cs = {'token': '12345', 'status': 'working'}
# rc = requests.get(url, cookies=cs)

# # 指定超时
# r = requests.get(url, timeout=2.5) # 2.5秒后超时

# # chardet 检测编码
# import chardet
# print(chardet.detect(b'Hello,world!')) # 有个confidence字段,表示检测正确的概率是1.0(即100%)
# data =  '离离原上草,一岁一枯荣'.encode('gbk')
# print(chardet.detect(data))
# data = '离离原上草,一岁一枯荣'.encode('utf-8')
# print(chardet.detect(data))
# data = '最新の主要ニュース'.encode('euc-jp')
# print(chardet.detect(data))


# # psutil psutil = process and system utilities 实现系统监控
# import psutil
#
# print(psutil.cpu_count())
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_times())  # 统计CPU的用户／系统／空闲时间
#
# for x in range(5):
#     print(psutil.cpu_percent(interval=1, percpu=True))  # 实现类似top命令的CPU使用率,每秒刷新一次,累计5次
#
# print(psutil.virtual_memory())  # 取物理内存和交换内存信息
# print(psutil.swap_memory())
#
# print(psutil.disk_partitions())  # 获取磁盘分区、磁盘使用率和磁盘IO信息
# print(psutil.disk_usage('.'))
# print(psutil.disk_io_counters())
#
# print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
# print(psutil.net_if_addrs())  # 获取网络接口信息
# print(psutil.net_if_stats())  # 获取网络接口状态
# print(psutil.net_connections())  # 获取当前网络连接信息
#
# print(psutil.pids())  # 所有进程ID
# p = psutil.Process(10444)  # 获取指定进程ID=10444,其实就是当前Python交互环境
# print(p.name())  # 进程名称
# print(p.exe())  # 进程exe路径
# print(p.cwd())  # 进程工作目录
# print(p.cmdline())  # 进程启动的命令行
# print(p.ppid())  # 父进程ID
# print(p.parent())  # 父进程
# print(p.children())  # 子进程列表
# print(p.status())  # 进程状态
# print(p.username())  # 进程用户名
# print(p.create_time())  # 进程创建时间
# # print(p.terminal())  # 进程终端
# print(p.cpu_times())  # 进程使用的CPU时间
# print(p.memory_info())  # 进程使用的内存
# print(p.open_files())  # 进程打开的文件
# print(p.connections())  # 进程相关网络连接
# print(p.num_threads())  # 进程的线程数量
# print(p.threads())  # 所有线程信息
# print(p.environ())  # 进程环境变量
# print(p.terminate())  # 结束进程

# import psutil  # 还可以获取用户信息、Windows服务等很多有用的系统信息
# print(psutil.test())  # test()函数,可以模拟出ps命令的效果

# # Tkinter 图形界面
# from tkinter import *
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()  # pack()方法把Widget加入到父容器中,并实现布局。pack()是最简单的布局,grid()可以实现更复杂的布局。
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello,world')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
#
# app = Application()
# app.master.title('Hello,world')
# app.mainloop()

# from tkinter import *
# import tkinter.messagebox as messagebox
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
#
# app = Application()
# app.master.title('Hello,world')  # 设置窗口标题:
# app.mainloop()  # 主消息循环:


# #网络编程 Socket
# #导入socket库:
# import socket
#
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# import socket
# import threading
# import time
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 9999))
# s.listen(5)
# print('Waiting for connection...')
#
#
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
#
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# #******UDP*******
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 9999))
# print('Bind UDP on 9999')
# while True:
#     data, addr = s.recvfrom(1024)
#     print('Received %s:%s' % addr)
#     s.sendto(b'Hello, %s' % data, addr)

# #电子邮件 SMTP

# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# # 带附件的邮件
# # 邮件对象:
# from email import encoders
# from email.header import Header
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#
# # 添加附件就是加上一个MIMEBase,从本地读取一个图片:
# with open('/Users/michael/Downloads/test.png', 'rb') as f:
#     # 设置附件的MIME和文件名,这里是png类型:
#     mime = MIMEBase('image', 'png', filename='test.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
"""
要把图片嵌入到邮件正文中,我们只需按照发送附件的方式,先把邮件作为附件添加进去,然后,在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片,给它们依次编号,然后引用不同的cid:x即可。

把上面代码加入MIMEMultipart的MIMEText从plain改为html,然后在适当的位置引用图片;

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
"""
# 加密SMTP
import time

"""
Gmail的SMTP端口是587,因此,修改代码如下;
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
"""

# # 协程
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)

# import asyncio
#
# # @asyncio.coroutine把一个generator标记为coroutine类型,然后,我们就把这个coroutine扔到EventLoop中执行。
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

"""把@asyncio.coroutine替换为async；
把yield from替换为await。"""
# import asyncio
#
#
# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio

from aiohttp import web

# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

# s = 'abc'
# sl = list(s)
# print(sl)
# print(sl.reverse())
# print(sl)

# x = input()
# xlist = x.split(",")
#
# print(xlist)
# xlist = [int(xlist[i]) for i in range(len(xlist))]
# print(xlist)
#
# y = input()
# ylist = y.split(",")
#
# print(ylist)
#
# zipo = zip(xlist, ylist)
#
# print(list(zipo))




