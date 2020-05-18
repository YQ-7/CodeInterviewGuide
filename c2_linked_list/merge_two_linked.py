# -*- coding: utf-8 -*-
"""
题目：
    向有序的环形单链表中插入新节点给定两个有序单链表的头节点head1和head2，
    请合并两个有序链表，合并后的链表依然有序，并返回合并后链表的头节点。
"""
import unittest
from utils.linked_list import Node


def merge_tow_liked(head1, head2):
    if head1 is None or head2 is None:
        return head1 if head1 is not None else head2
    new_head = head1 if head1.data < head2.data else head2
    cur1 = head1 if new_head == head1 else head2
    cur2 = head2 if new_head == head1 else head1
    while cur1 is not None and cur2 is not None:
        if cur1.data <= cur2.data:
            pre = cur1
            cur1 = cur1.next
        else:
            next = cur2.next
            pre.next = cur2
            cur2.next = cur1
            pre = cur2
            cur2 = next
    pre.next = cur2 if cur1 is None else cur1
    return new_head


class MyTestCase(unittest.TestCase):
    def test_merge_tow_liked(self):
        head1 = Node(1)
        node_2 = Node(3)
        node_3 = Node(3)
        node_4 = Node(5)
        head1.next = node_2
        node_2.next = node_3
        node_3.next = node_4

        head2 = Node(2)
        node2_2 = Node(4)
        node2_3 = Node(7)
        head2.next = node2_2
        node2_2.next = node2_3

        new_head = merge_tow_liked(head1, head2)
        self.assertEqual(1, new_head.data)
        self.assertEqual(2, new_head.next.data)
        self.assertEqual(3, new_head.next.next.data)
        self.assertEqual(3, new_head.next.next.next.data)
        self.assertEqual(4, new_head.next.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
