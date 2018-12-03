#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   Leetcode.py

@Time    :   2018/11/19 23:24

@Desc    :

"""


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         if not nums1:
#             return (max(nums2) + min(nums2)) / 2
#         if not nums2:
#             return (max(nums1) + min(nums1)) / 2
#         maxs1 = max(nums1)
#         mins1 = min(nums1)
#         maxs2 = max(nums2)
#         mins2 = min(nums2)
#         if maxs1 == (max(nums2) + min(nums2)) / 2:
#             return maxs1
#         if maxs2 == (max(nums1) + min(nums1)) / 2:
#             return maxs2
#         if maxs2 > maxs1 > 0:
#             return (maxs1 + mins2) / 2
#         if maxs1 > maxs2 > 0:
#             return (mins1 + maxs2) / 2
#         if maxs1 > maxs2 and maxs2 < 0:
#             return (maxs1 + abs(mins2)) / 2
#         if maxs1 < maxs2 and maxs1 < 0:
#             return (abs(mins1) + maxs2) / 2
#
#     print(findMedianSortedArrays(findMedianSortedArrays, [], [1]))
#     print(findMedianSortedArrays(findMedianSortedArrays, [1, 2], [3, 4]))
#     print(findMedianSortedArrays(findMedianSortedArrays, [3], [-2, -1]))
#     print(findMedianSortedArrays(findMedianSortedArrays, [-2,-1], [-3]))


# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         if nums1 == []:
#             res = nums2
#         elif nums2 == []:
#             res = nums1
#         else:
#             res = nums1 + nums2
#             res.sort()
#             l = len(res)
#             if l % 2 == 1:
#                 return res[l // 2]
#             else:
#                 return (res[l // 2 - 1] + res[l // 2]) / 2.0
#
#     print(findMedianSortedArrays(findMedianSortedArrays, [3], [-2, -1]))

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums = nums1 + nums2
#         nums.sort()
#         l = len(nums)
#         if l % 2 == 0:
#             return (nums[int(l / 2)] + nums[int(l / 2 - 1)]) / 2
#         else:
#             return nums[int((l - 1) / 2)]
#
#     print(findMedianSortedArrays(findMedianSortedArrays, [3], [-2, -1]))
#     print(findMedianSortedArrays(findMedianSortedArrays, [], [1]))

# class Solution:
#     def longestPalindrome(self, s):
#         s1 = list(s)
#         s2 = list(s)
#         s2.reverse()
#         lista = ""
#         for i in range(len(s)):
#
#             if len(s) < 3 and s1[i] != s2[i]:
#                 return s[0]
#             if s1[i] == s2[i]:
#                 lista = lista + s1[i]
#             else:
#                 continue
#         return lista
#     print(longestPalindrome(longestPalindrome, "babad"))
#     print(longestPalindrome(longestPalindrome, "ac"))
#     print(longestPalindrome(longestPalindrome, "bb"))

# def twoSum(self, nums, target):
#     d = {}
#     for x in range(len(nums)):
#         if nums[x] in d:
#             return d[nums[x]], x
#         else:
#             print(target - nums[x])
#             print(nums[x])
#             print(x)
#             d[target - nums[x]] = x
#             print(d)
#             continue
#
# print(twoSum(twoSum, [1,2,3],5))

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         for i in range(n):
#             nums1[m] = nums2[i - 1]
#             m += 1
#         nums1.sort()
#         print(nums1)
#
#     print(merge(merge, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

# class Solution:
#
#     def generateMatrix(self, n):
#         list = [i + 1 for i in range(n**2)]
#
#     print(generateMatrix(generateMatrix, 3))

#
# from collections import Counter
#
#
# class Solution:
#     def containsDuplicate(self, nums):
#         if not nums:
#             return False
#         c = Counter(nums)
#         # print(c.most_common())
#         # print(type(c.most_common()))
#         # print(type(c))
#         for i in range(len(c.most_common())):
#             if c.most_common()[i][1] >= 2:
#                 return True
#             else:
#                 return False
#
#     print(containsDuplicate(containsDuplicate, []))

# BUG
# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
#         minmin = []
#         s = []
#         for i in range(len(strs)):
#             minmin.append(len(strs[i]))
#         step = min(minmin)
#         for j in range(step):
#             temp = strs[0][j]
#             for i in range(len(strs)):
#                 if temp == strs[i][j]:
#                     if i != len(strs) - 1:
#                         continue
#                     else:
#                         s.append(temp)
#                 break
#
#         return "".join(s)
#
#     print(longestCommonPrefix(longestCommonPrefix, ["c", "acc", "ccc"]))
#     print(longestCommonPrefix(longestCommonPrefix, ["flow", "flower", "flight"]))
#     print(longestCommonPrefix(longestCommonPrefix, ["aca", "cba"]))

# 记录下索引试试？
class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] == nums[i + 1]:
                    nums.pop(i)
                else:
                    continue
        return nums

    print(removeDuplicates(removeDuplicates, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(removeDuplicates(removeDuplicates, [1, 1, 2]))
