# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head，已知所有节点的值都不一样，返回其中最大的且符合搜索二叉树条件的最大拓扑结构的大小
"""

import unittest
from utils.linked_list import TreeNode


def bst_topo_size1(head):
    if head is None:
        return 0
    max_size = max_topo(head, head)
    max_size = max(bst_topo_size1(head.left), max_size)
    max_size = max(bst_topo_size1(head.right), max_size)
    return max_size


def max_topo(h, n):
    if h is not None and n is not None and is_bst_node(h, n, n.data):
        return max_topo(h, n.left) + max_topo(h, n.right) + 1
    return 0


def is_bst_node(h, n, data):
    if h is None:
        return False
    if h == n:
        return True
    return is_bst_node(h.left if h.data > data else h.right, n, data)


class Record(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


def bst_topo_size2(head):
    # 计算节点拓扑贡献值
    record_map = {}
    return pos_order(head, record_map)


def pos_order(h, record_map):
    if h is None:
        return 0

    # 计算左子树拓扑贡献值
    left_size = pos_order(h.left, record_map)
    # 计算右子树拓扑贡献值
    right_size = pos_order(h.right, record_map)
    # 基于左右子树的拓扑贡献计算
    modify_map(h.left, h.data, record_map, True)
    modify_map(h.right, h.data, record_map, False)
    left_record = record_map.get(h.left)
    right_record = record_map.get(h.right)
    left_bst = 0 if left_record is None else left_record.left + left_record.right + 1
    right_bst = 0 if right_record is None else right_record.left + right_record.right + 1
    record_map[h] = Record(left_bst, right_bst)
    return max(left_bst + right_bst + 1, left_size, right_size)


# 更新拓扑贡献值
def modify_map(n, v, record_map, is_left):
    if n is None or record_map.get(n) is None:
        return 0
    r = record_map.get(n)
    if (is_left and n.data > v) or ((not is_left) and n.data < v):
        record_map.pop(n)
        return r.left + r.right + 1
    else:
        minus = modify_map(n.right if is_left else n.left, v, record_map, is_left)
        if is_left:
            r.right -= minus
        else:
            r.left -= minus
        record_map[n] = r
        return minus


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

    def test_bst_topo_size1(self):
        self.assertEqual(8, bst_topo_size1(self.make_data()))

    def test_bst_topo_size2(self):
        self.assertEqual(8, bst_topo_size2(self.make_data()))


if __name__ == '__main__':
    unittest.main()
