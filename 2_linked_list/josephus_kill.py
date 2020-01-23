# -*- coding: utf-8 -*-
"""
题目：
    环形单链表的约瑟夫问题

"""

import unittest
from utils.linked_list import Node


def josephus_kill_1(head, m):
    if head is None or head.next == head or m < 1:
        return head
    last = head
    # 将last指向链表尾节点
    while last.next != head:
        last = last.next
    count = 0
    while head != last:
        count += 1
        if count == m:
            last.next = head.next
            count = 0
        else:
            last = last.next
        head = last.next
    return head


def josephus_kill_2(head, m):
    if head is None or head.next == head or m < 1:
        return head
    cur = head.next
    tmp_len = 1
    while cur != head:
        tmp_len += 1
        cur = cur.next
    tmp = get_live(tmp_len, m)
    tmp -= 1
    while tmp != 0:
        tmp -= 1
        head = head.next
    head.next = head
    return head


def get_live(i, m):
    if i == 1:
        return 1
    return (get_live(i - 1, m) + m - 1) % i + 1


class MyTestCase(unittest.TestCase):
    def test_josephus_kill_1(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = head
        self.assertEqual(3, josephus_kill_1(head, 2).data)
        # self.assertEqual(4, josephus_kill_1(head, 3).data)

    def test_josephus_kill_2(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = head
        # self.assertEqual(3, josephus_kill_2(head, 2).data)
        self.assertEqual(4, josephus_kill_2(head, 3).data)


if __name__ == '__main__':
    unittest.main()
