# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head和一个整数sum，二叉树节点值类型为整型，求累加和为sum的最长路径长度。
    路径是指从某个节点往下，每次最多选择一个孩子节点或者不选所形成的节点链。
"""

import unittest
from utils.linked_list import TreeNode


def get_max_length(head, k):
    sum_map = {0: 0}
    return pre_order(head, k, 0, 1, 0, sum_map)


def pre_order(head, k, pre_sum, level, max_len, sum_map):
    if head is None:
        return max_len
    cur_sum = pre_sum + head.data
    if sum_map.get(cur_sum) is None:
        sum_map[cur_sum] = level
    if sum_map.get(cur_sum - k) is not None:
        max_len = max(level - sum_map.get(cur_sum - k), max_len)
    max_len = pre_order(head.left, k, cur_sum, level + 1, max_len, sum_map)
    max_len = pre_order(head.right, k, cur_sum, level + 1, max_len, sum_map)
    # 遍历完子树返回父节点时，需要将当前层的累加和从map中移除，避免路径不是自顶向下的
    if level == sum_map.get(cur_sum):
        sum_map.pop(cur_sum)
    return max_len


class MyTestCase(unittest.TestCase):
    @staticmethod
    def make_data():
        node_1 = TreeNode(-3)
        node_2 = TreeNode(3)
        node_3 = TreeNode(1)
        node_4 = TreeNode(0)
        node_5 = TreeNode(1)
        node_6 = TreeNode(6)
        node_7 = TreeNode(-9)
        node_8 = TreeNode(2)
        node_9 = TreeNode(1)
        head = node_1
        head.left = node_2
        head.right = node_7
        node_2.left = node_3
        node_2.right = node_4
        node_7.left = node_8
        node_7.right = node_9
        node_4.left = node_5
        node_4.right = node_6
        return head

    def test_get_max_length(self):
        self.assertEqual(4, get_max_length(self.make_data(), 6))
        self.assertEqual(1, get_max_length(self.make_data(), -9))


if __name__ == '__main__':
    unittest.main()
