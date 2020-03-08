# -*- coding: utf-8 -*-
"""
题目：
    判断t1树是否有与t2树相同的子树
"""

import unittest
from utils.linked_list import TreeNode
from c9_other import kmp


def is_sub_tree(t1, t2):
    # 将树通过先序遍历序列化成字符串
    t1_str = serial_by_pre(t1)
    t2_str = serial_by_pre(t2)
    # 通过kmp算法查找t1是否包含t2
    return kmp.get_index_of(t1_str, t2_str) != -1


def serial_by_pre(head):
    """
        将树序列化为字符串
        #:表示Null值
        !:节点结尾标志
    """
    if head is None:
        return "#!"
    res = str(head.data) + "!"
    res += serial_by_pre(head.left)
    res += serial_by_pre(head.right)
    return res

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

    def test_is_sub_tree(self):
        self.assertTrue(is_sub_tree(self.make_t1_data(), self.make_t2_data()))


if __name__ == '__main__':
    unittest.main()
