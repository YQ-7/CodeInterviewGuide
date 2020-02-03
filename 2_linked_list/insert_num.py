# -*- coding: utf-8 -*-
"""
题目：
    向有序的环形单链表中插入新节点
"""

import unittest
from utils.linked_list import Node


def insert_num(head, num):
    new_node = Node(num)
    if head is None:
        new_node.next = new_node
        return new_node
    pre = head
    cur = head.next
    while cur != head:
        if pre.data <= num <= cur.data:
            break
        pre = cur
        cur = cur.next
    pre.next = new_node
    new_node.next = cur
    return head if head.data < num else new_node


class MyTestCase(unittest.TestCase):
    def test_insert_num1(self):
        head = insert_num(None, 1)
        self.assertEqual(1, head.data)
        self.assertEqual(1, head.next.data)

    def test_insert_num2(self):
        head = Node(2)
        node_1 = Node(2)
        node_2 = Node(3)
        head.next = node_1
        node_1.next = node_2
        node_2.next = head
        head = insert_num(head, 3)
        self.assertEqual(2, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(3, head.next.next.data)
        self.assertEqual(3, head.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
