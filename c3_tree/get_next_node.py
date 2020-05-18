# -*- coding: utf-8 -*-
"""
题目：
    二叉树中每个节点包含指向父节的指针，请按照中序遍历顺序，返回给定节点的后继节点。
解答:
"""

import unittest
from utils.linked_list import TreeNode


class Node(TreeNode):

    def __init__(self, data):
        super().__init__(data)
        self.parent = Node


def get_next_node(node):
    if node is None:
        return None
    # node有右子树，则后继节点为右子树的最左节点
    if node.right is not None:
        return get_left_most(node.right)
    # node没有右子树
    # node是其父节点的左孩子，后继节点为父节点
    # node是其父节点的右孩子，则向上遍历，找到某个节点是其父节点的左孩子为止，则此父节点为node的后继节点
    # 否则，没有后继节点
    parent = node.parent
    while parent is not None and parent.left is not node:
        node = parent
        parent = node.parent
    return parent


def get_left_most(node):
    if node is None:
        return
    while node.left is not None:
        node = node.left
    return node


class MyTestCase(unittest.TestCase):

    def test_get_next_node(self):
        node_1 = Node(6)
        node_2 = Node(3)
        node_3 = Node(9)
        node_4 = Node(1)
        node_5 = Node(4)
        node_6 = Node(8)
        node_7 = Node(10)
        node_8 = Node(2)
        node_9 = Node(5)
        node_10 = Node(7)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_2.parent = node_1
        node_3.left = node_6
        node_3.right = node_7
        node_3.parent = node_1
        node_4.right = node_8
        node_4.parent = node_2
        node_5.right = node_9
        node_5.parent = node_2
        node_6.left = node_10
        node_6.parent = node_3
        node_7.parent = node_3
        node_8.parent = node_4
        node_9.parent = node_5
        node_10.parent = node_6

        self.assertEqual(6, get_next_node(node_9).data)
        self.assertEqual(2, get_next_node(node_4).data)
        self.assertEqual(8, get_next_node(node_10).data)


if __name__ == '__main__':
    unittest.main()
