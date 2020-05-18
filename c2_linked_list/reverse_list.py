# -*- coding: utf-8 -*-

"""
题目：
    分别实现反转单向链表和反转双向链表的函数。
"""
import unittest
from utils.linked_list import Node, DoubleNode


# 反转单链表
def reverse_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


# 反转单链表
def reverse_double_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre


class MyTestCase(unittest.TestCase):
    def test_reverse_list(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        reverse_head = reverse_list(head)
        self.assertEqual(5, reverse_head.data)
        self.assertEqual(4, reverse_head.next.data)
        self.assertEqual(3, reverse_head.next.next.data)

    def test_reverse_double_list(self):
        head = DoubleNode(1)
        node_2 = DoubleNode(2)
        node_3 = DoubleNode(3)
        node_4 = DoubleNode(4)
        node_5 = DoubleNode(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        reverse_head = reverse_double_list(head)
        self.assertEqual(5, reverse_head.data)
        self.assertEqual(4, reverse_head.next.data)
        self.assertEqual(5, reverse_head.next.last.data)
        self.assertEqual(3, reverse_head.next.next.data)


if __name__ == '__main__':
    unittest.main()
