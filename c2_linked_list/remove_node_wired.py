# -*- coding: utf-8 -*-
"""
题目：
    链表节点值类型为int型，给定一个链表中的节点node，但不给定整个链表的头节点。如何在链表中删除node？
    请实现这个函数，并分析这样做会出现哪些问题。
存在问题：
    1.这样的删除方式无法删除最后一个节点。
    2.这种删除方式在本质上根本就不是删除了node节点，而是把node节点的值改变，
      然后删除node的下一个节点，在实际的工程中可能会带来很大问题。
"""

import unittest
from utils.linked_list import Node


def remove_node_wired(node):
    if node is None:
        return
    next_node = node.next
    if next_node is None:
        raise Exception("can not remove last node.")
    node.data = next_node.data
    node.next = next_node.next


class MyTestCase(unittest.TestCase):
    def test_remove_node_wired(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        head.next = node_2
        node_2.next = node_3
        remove_node_wired(node_2)
        self.assertEqual(1, head.data)
        self.assertEqual(3, head.next.data)
        self.assertIsNone(head.next.next)


if __name__ == '__main__':
    unittest.main()
