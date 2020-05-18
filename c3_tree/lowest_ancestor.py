# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head，以及这棵树中的两个节点o1和o2，请返回o1和o2的最近公共祖先节点
"""

import unittest
from utils.linked_list import TreeNode


def lowest_ancestor(head, o1, o2):
    """
        方法一：后续遍历二叉树，先处理左子树，在处理右子树
    """
    if head is None or head == o1 or head == o2:
        return head
    left = lowest_ancestor(head.left, o1, o2)
    right = lowest_ancestor(head.right, o1, o2)
    if left is not None and right is not None:
        return head
    return left if left is not None else right


def query_1(head, o1, o2):
    """
        方法二：通过构建父节点表，来节省查询次数
    """
    record = record_map(head)
    # 存储o1祖先节点
    path = set()
    while o1 in record:
        path.add(o1)
        o1 = record[o1]

    # 依次检查o2的祖先节点是否在path中
    # 第一个匹配的就是o1、o2公共节点
    while o2 not in path:
        o2 = record[o2]
    return o2


# 构建父节点记录表：key:节点，value:父节点
def record_map(head):
    record_map = {}
    if head is not None:
        record_map[head] = None
    set_map(record_map, head)
    return record_map


def set_map(record_map, head):
    if head is None:
        return
    if head.left is not None:
        record_map[head.left] = head
    if head.right is not None:
        record_map[head.right] = head
    set_map(record_map, head.left)
    set_map(record_map, head.right)


def query_2(head, o1, o2):
    """
        方法三：先建立任意两节点之间的最近公共祖先记录
    """
    if o1 == o2:
        return o1
    record_map = record_map2(head)
    if o1 in record_map:
        return record_map[o1][o2]
    if o2 in record_map:
        return record_map[o2][o1]
    return None


def record_map2(head):
    record_map = {}
    init_map(record_map, head)
    set_map2(record_map, head)
    return record_map


def init_map(record_map, head):
    if head is None:
        return
    record_map[head] = {}
    init_map(record_map, head.left)
    init_map(record_map, head.right)


def set_map2(record_map, head):
    if head is None:
        return
    # 子节点与头结点的最近公共节点为头结点
    head_record(record_map, head.left, head)
    head_record(record_map, head.right, head)
    sub_record(record_map, head)
    set_map2(record_map, head.left)
    set_map2(record_map, head.right)


def head_record(record_map, n, h):
    if n is None:
        return
    record_map[n][h] = h
    head_record(record_map, n.left, h)
    head_record(record_map, n.right, h)


def sub_record(record_map, head):
    if head is None:
        return
    pre_left(record_map, head.left, head.right, head)
    sub_record(record_map, head.left)
    sub_record(record_map, head.right)


def pre_left(record_map, l, r, h):
    if l is None:
        return
    pre_right(record_map, l, r, h)
    pre_left(record_map, l.left, r, h)
    pre_left(record_map, l.right, r, h)


def pre_right(record_map, l, r, h):
    if r is None:
        return
    record_map[l][r] = h
    pre_right(record_map, l, r.left, h)
    pre_right(record_map, l, r.right, h)


class MyTestCase(unittest.TestCase):

    def test_lowest_ancestor(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        node_7.left = node_8

        self.assertEqual(node_2, lowest_ancestor(head, node_4, node_5))
        self.assertEqual(node_3, lowest_ancestor(head, node_6, node_8))
        self.assertEqual(node_1, lowest_ancestor(head, node_5, node_8))

    def test_query_1(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        node_7.left = node_8

        self.assertEqual(node_2, query_1(head, node_4, node_5))
        self.assertEqual(node_3, query_1(head, node_6, node_8))
        self.assertEqual(node_1, query_1(head, node_5, node_8))

    def test_query_2(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        node_7.left = node_8

        self.assertEqual(node_2, query_2(head, node_4, node_5))
        self.assertEqual(node_3, query_2(head, node_6, node_8))
        self.assertEqual(node_1, query_2(head, node_5, node_8))


if __name__ == '__main__':
    unittest.main()
