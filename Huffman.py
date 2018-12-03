#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Chenghan}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {1978786350@qq.com}

@Software:   PyCharm

@File    :   Huffman.py

@Time    :   2018/12/2 17:23

@Desc    :

"""


# Tree-Node Template
class Node:
    def __init__(self, frequency):
        self.leftNode = None
        self.rightNode = None
        self.fatherNode = None
        self.freq = frequency

    def isLeft(self):
        return self.father.left == self

# create nodes创建叶子节点
def createLeafNodes(frequency):
    return [Node(frequency) for frequency in frequency]


# create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        leftNode = queue.pop(0)
        rightNode = queue.pop(0)
        fatherNode = Node(leftNode.freq + rightNode.freq)
        fatherNode.left = leftNode
        fatherNode.right = rightNode
        leftNode.father = fatherNode
        rightNode.father = fatherNode
        queue.append(fatherNode)
    queue[0].father = None
    return queue[0]


# Huffman编码
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        tempNode = nodes[i]
        while tempNode != root:
            if tempNode.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            tempNode = tempNode.father
    return codes


if __name__ == '__main__':
    print("Input chars eg. A,B,C  ... Enter the end : ")
    chars = input()
    charList = chars.split(",")
    print("Input frequences eg. 1,2,3  ... Enter the end : ")
    frequency = input()
    frequencyList = frequency.split(",")
    frequencyList = [float(frequencyList[i]) for i in range(len(frequencyList))]
    frequencyChars = list(zip(charList, frequencyList))
    nodes = createLeafNodes([item[1] for item in frequencyChars])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)
    for item in zip(frequencyChars, codes):
        print('Character:%s  frequency:%0.2f  Encoding: %s' % (item[0][0], item[0][1], item[1]))
