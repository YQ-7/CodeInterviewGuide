# -*- coding: utf-8 -*-
"""
题目：
    判断二叉树是否为平衡二叉树
"""

import unittest
from utils.linked_list import TreeNode


class ReturnType(object):

    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


def process(head):
    # base case
    if head is None:
        return ReturnType(True, 0)
    # 获取左子树信息
    left_data = process(head.left)
    right_data = process(head.right)
    # 获取右子树信息
    # 整合信息：判断当前节点是否是平衡树
    height = max(left_data.height, right_data.height) + 1
    is_balanced = left_data.is_balanced and right_data.is_balanced and abs(left_data.height - right_data.height) < 2
    return ReturnType(is_balanced, height)


def is_balanced(head):
    return process(head).is_balanced


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_3.right = node_5

    def test_is_balanced(self):
        self.assertTrue(is_balanced(self.make_data()))


if __name__ == '__main__':
    unittest.main()
