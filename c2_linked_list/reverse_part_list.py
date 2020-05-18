# -*- coding: utf-8 -*-

"""
题目：
    给定一个单向链表的头节点head，以及两个整数from和to，在单向链表上把第from个节点到第to个节点这一部分进行反转。
"""

import unittest
from utils.linked_list import Node


def reverse_part(head, from_i, to_i):
    len = 0
    # 第from_i - 1个节点
    f_pre = None
    # 第to_i + 1个节点
    t_pos = None
    node1 = head

    # 找到f_pre、t_pos节点
    while node1 is not None:
        len += 1
        f_pre = node1 if len == from_i - 1 else f_pre
        t_pos = node1 if len == to_i + 1 else t_pos
        node1 = node1.next

    if from_i > to_i or from_i < 1 or to_i > len:
        return head

    node1 = head if f_pre is None else f_pre.next
    node2 = node1.next
    node1.next = t_pos
    next = None
    while node2 != t_pos:
        next = node2.next
        node2.next = node1
        node1 = node2
        node2 = next
    if f_pre is not None:
        f_pre.next = node1
        return head
    return node1


class MyTestCase(unittest.TestCase):
    def test_reverse_part(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = reverse_part(head, 2, 4)
        self.assertEqual(4, head.next.data)
        self.assertEqual(3, head.next.next.data)
        self.assertEqual(2, head.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
