# -*- coding: utf-8 -*-
"""
题目：
    实现一个函数，较为直观的打印二叉树
"""

import unittest
from utils.linked_list import TreeNode


def print_tree_shape(head):
    print_in_order(head, 0, "H", 17)


def print_in_order(head, height, lab, length):
    if head is None:
        return
        # 打印右子树
    print_in_order(head.right, height + 1, "v", length)
    # 打印当前节点
    val = lab + str(head.data) + lab
    len_m = len(val)
    len_l = (length - len_m) // 2
    len_r = length - len_m - len_l
    val = " " * len_l + val + " " * len_r
    print(" " * height * length + val)
    # 打印左子树
    print_in_order(head.left, height + 1, "^", length)


class MyTestCase(unittest.TestCase):

    def test_print_tree_shape(self):
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
        node_3.left = node_5
        node_3.right = node_6
        node_4.right = node_7
        print_tree_shape(head)


if __name__ == '__main__':
    unittest.main()
