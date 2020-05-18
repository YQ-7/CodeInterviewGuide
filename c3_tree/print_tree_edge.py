# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head，按照边界节点标准实现二叉树边界节点的逆时针打印。
"""

import unittest
from utils.linked_list import TreeNode


def print_edge_1(head):
    """
    边界节点标准：
        1.头节点为边界节点。
        2.叶节点为边界节点。
        3.如果节点在其所在的层中是最左的或最右的，那么该节点也是边界节点。
    """
    if head is None:
        return
    # 获取数高度
    h = get_height(head, 0)
    # 通过二维数组存储每一层左右边界的节点
    edge = [[None for i in range(2)] for j in range(h)]
    set_edge(head, 0, edge)
    # 打印左边界节点
    for n in edge:
        print(n[0].data, end=' ')
    # 打印非左右边界的叶子节点
    print_leaf_not_in_map(head, 0, edge)
    # 打印右边界节点
    for n in edge[::-1]:
        if n[0] != n[1]:
            print(n[1].data, end=' ')


def get_height(head, l):
    if head is None:
        return l
    return max(get_height(head.left, l + 1), get_height(head.right, l + 1))


def set_edge(h, l, edge):
    if h is None:
        return
        # 左边界
    edge[l][0] = h if edge[l][0] is None else edge[l][0]
    # 有边界
    edge[l][1] = h
    set_edge(h.left, l + 1, edge)
    set_edge(h.right, l + 1, edge)


def print_leaf_not_in_map(h, l, edge):
    if h is None:
        return
    if h.left is None and h.right is None and h != edge[l][0] and h != edge[l][1]:
        print(h.data, end=' ')
    print_leaf_not_in_map(h.left, l + 1, edge)
    print_leaf_not_in_map(h.right, l + 1, edge)


def print_edge_2(head):
    """
    边界节点标准：
        1.头节点为边界节点。
        2.叶节点为边界节点。
        3.树左边界延伸下去的路径为边界节点。
        4.树右边界延伸下去的路径为边界节点。
    """
    if head is None:
        return
    print(head.data, end=' ')
    if head.left is not None and head.right is not None:
        # 打印左边界延申路径及左子树的叶节点
        print_left_edge(head.left, True)
        # 打印右边界延申路径及右子树的叶节点
        print_right_edge(head.right, True)
    else:
        # 继续查找有第一个有左右节点的节点
        print_edge_2(head.left if head.left is not None else head.right)


def print_left_edge(h, should):
    if h is None:
        return
    if should or (h.left is None and h.right is None):
        # 打印叶节点
        print(h.data, end=' ')
    print_left_edge(h.left, should)
    print_left_edge(h.right, should and h.left is None)


def print_right_edge(h, should):
    if h is None:
        return
    print_right_edge(h.left, should and h.left is None)
    print_right_edge(h.right, should)
    if should or (h.left is None and h.right is None):
        # 打印叶节点
        print(h.data, end=' ')


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
        node_8 = TreeNode(8)
        node_9 = TreeNode(9)
        node_10 = TreeNode(10)
        node_11 = TreeNode(11)
        node_12 = TreeNode(12)
        node_13 = TreeNode(13)
        node_14 = TreeNode(14)
        node_15 = TreeNode(15)
        node_16 = TreeNode(16)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.right = node_4
        node_3.left = node_5
        node_3.right = node_6
        node_4.left = node_7
        node_4.right = node_8
        node_5.left = node_9
        node_5.right = node_10
        node_8.right = node_11
        node_11.left = node_13
        node_11.right = node_14
        node_9.left = node_12
        node_12.left = node_15
        node_12.right = node_16
        return head

    def test_print_edge_1(self):
        print("test_print_edge_1:", end=' ')
        print_edge_1(self.make_data())
        print()

    def test_print_edge_2(self):
        print("test_print_edge_2:", end=' ')
        print_edge_2(self.make_data())
        print()


if __name__ == '__main__':
    unittest.main()
