#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   两数之和.py

@Time    :   2018/11/19 23:24

@Desc    :

"""


# import time
# class Solution:
#     def twoSum(self, nums, target):
#         N = len(nums)
#         for i in range(N):
#             for j in range(N):
#                 if N > j != i and (nums[i] + nums[j]) == target:
#                     return [i, j]
#
#     print(twoSum(twoSum, [3, 2, 4], 6))
#     print(time.process_time())


# for i, j in enumerate([3, 2, 4]):
#     print(i,j)


# class Solution:
#     def twoSum(self, nums, target):
#         N = len(nums)
#         for i in range(N):
#             x = 0
#             while 1:
#                 if (nums[x] + nums[i]) != target:
#                     x += 1
#                 if (nums[x] + nums[i]) == target and x != i:
#                     return i, x
#                 if x == N:
#                     break
#
#
#
#     print(twoSum(twoSum, [-3, 4, 3, 90], 0))
#     print(time.process_time())

import time
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for x in range(len(nums)):
            if nums[x] in d:
                return d[nums[x]], x
            else:
                d[target - nums[x]] = x
                continue

    print(twoSum(twoSum, [1, 2, 3, 4], 6))
    print(time.process_time())




