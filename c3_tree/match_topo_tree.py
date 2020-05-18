# -*- coding: utf-8 -*-
"""
题目：
    判断t1树是否包含t2树全部的拓扑结构
"""

import unittest
from utils.linked_list import TreeNode


def contains(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    return check(t1, t2) or check(t1.left, t2) or check(t1.right, t2)


def check(h, t2):
    """
        按照先序遍历判断是否匹配
    """
    if t2 is None:
        return True
    if h is None or h.data != t2.data:
        return False
    return check(h.left, t2.left) and check(h.right, t2.right)


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_t1_data():
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

    @staticmethod
    def make_t2_data():
        node_2 = TreeNode(2)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        head = node_2
        node_2.left = node_4
        node_2.right = node_5
        return head

    def test_contains(self):
        self.assertTrue(contains(self.make_t1_data(), self.make_t2_data()))


if __name__ == '__main__':
    unittest.main()
