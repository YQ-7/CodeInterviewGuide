# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head，已知其中所有节点的值都不一样，找到含有节点最多的搜索二叉子树，并返回这棵子树的头节点。
"""

import unittest
from utils.linked_list import TreeNode
import sys


class ReturnType(object):

    def __init__(self, max_bst_head, max_bst_size, min_val, max_val):
        self.max_bst_head = max_bst_head
        self.max_bst_size = max_bst_size
        self.min_val = min_val
        self.max_val = max_val


def get_max_bst(head):
    return process(head).max_bst_head


def process(x):
    # base case:子树是空树，最大值为系统最小，最小值为系统最大
    if x is None:
        return ReturnType(None, 0, sys.maxsize, -sys.maxsize - 1)
    # 递归获取左子树信息
    left_data = process(x.left)
    # 递归获取右子树信息
    right_data = process(x.right)
    # 信息整合
    # 获取符合要求搜索树的最小值
    min_val = min(x.data, left_data.min_val, right_data.min_val)
    # 获取符合要求搜索树的最大值
    max_val = max(x.data, left_data.max_val, right_data.max_val)
    # 获取左右子树最大二叉树节点个数
    max_bst_size = max(left_data.max_bst_size, right_data.max_bst_size)
    # 获取左右子树最大二叉树节节点
    max_bst_head = left_data.max_bst_head \
        if left_data.max_bst_size >= right_data.max_bst_size \
        else right_data.max_bst_head
    # 判断以x为头结点的树，是否是搜索二叉树
    if x.left == left_data.max_bst_head and x.right == right_data.max_bst_head \
            and left_data.max_val < x.data < right_data.min_val:
        max_bst_size = left_data.max_bst_size + right_data.max_bst_size + 1
        max_bst_head = x
    # 返回整理后的信息
    return ReturnType(max_bst_head, max_bst_size, min_val, max_val)


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(6)
        node_2 = TreeNode(1)
        node_3 = TreeNode(12)
        node_4 = TreeNode(0)
        node_5 = TreeNode(3)
        node_6 = TreeNode(10)
        node_7 = TreeNode(13)
        node_8 = TreeNode(4)
        node_9 = TreeNode(14)
        node_10 = TreeNode(20)
        node_11 = TreeNode(16)
        node_12 = TreeNode(2)
        node_13 = TreeNode(5)
        node_14 = TreeNode(11)
        node_15 = TreeNode(15)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        node_6.left = node_8
        node_6.right = node_9
        node_7.left = node_10
        node_7.right = node_11
        node_8.left = node_12
        node_8.right = node_13
        node_9.left = node_14
        node_9.right = node_15
        return head

    def test_get_max_bst(self):
        bst_head = get_max_bst(self.make_data())
        self.assertEqual(10, bst_head.data)
        self.assertEqual(4, bst_head.left.data)
        self.assertEqual(14, bst_head.right.data)
        self.assertEqual(2, bst_head.left.left.data)
        self.assertEqual(5, bst_head.left.right.data)
        self.assertEqual(11, bst_head.right.left.data)
        self.assertEqual(15, bst_head.right.right.data)


if __name__ == '__main__':
    unittest.main()
