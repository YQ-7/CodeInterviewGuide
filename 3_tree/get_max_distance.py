# -*- coding: utf-8 -*-
"""
题目：
    从二叉树的节点A出发，可以向上或者向下走，但沿途的节点只能经过一次，当到达节点B时，路径上的节点数叫作A到B的距离
    求树的最大距离
"""

import unittest
from utils.linked_list import TreeNode


class ReturnType(object):

    def __init__(self, max_distance, height):
        self.max_distance = max_distance  # 树的最大距离
        self.height = height  # 树高度


def get_max_distance(head):
    return process(head).max_distance


def process(head):
    if head is None:
        return ReturnType(0, 0)
    # 获取左子树信息
    left_data = process(head.left)
    # 获取右子树信息
    right_data = process(head.right)
    # 整合当前节点信息
    height = max(left_data.height, right_data.height) + 1
    max_distance = max(left_data.height + right_data.height + 1
                       , left_data.max_distance
                       , right_data.max_distance)
    return ReturnType(max_distance, height)


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        return head

    def test_get_max_distance(self):
        self.assertEqual(5, get_max_distance(self.make_data()))


if __name__ == '__main__':
    unittest.main()
