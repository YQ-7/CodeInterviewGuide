# -*- coding: utf-8 -*-
"""
题目：
    给定一个无序单链表的头节点head，实现单链表的选择排序。要求：额外空间复杂度为O（1）
"""

import unittest
from utils.linked_list import Node


def selection_sort(head):
    # 依次寻找待排序部分的最小节点
    tail = None  # 排序部分尾部
    cur = head  # 未排序部分头部
    while cur is not None:
        small = cur  # 最小的节点
        small_pre = get_smallest_pre_node(cur)
        # 将最小节点链接至已排序链表尾部
        if small_pre is not None:
            small = small_pre.next
            small_pre.next = small.next
        cur = cur.next if cur == small else cur
        if tail is None:
            head = small
        else:
            tail.next = small
        tail = small
    return head


def get_smallest_pre_node(head):
    small = head
    small_pre = None
    pre = head
    cur = head.next
    while cur is not None:
        if cur.data < small.data:
            small_pre = pre
            small = cur
        pre = cur
        cur = cur.next
    return small_pre


class MyTestCase(unittest.TestCase):
    def test_selection_sort(self):
        head = Node(3)
        node_2 = Node(1)
        node_3 = Node(2)
        node_4 = Node(4)
        node_5 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = selection_sort(head)
        self.assertEqual(1, head.data)
        self.assertEqual(1, head.next.data)
        self.assertEqual(2, head.next.next.data)
        self.assertEqual(3, head.next.next.next.data)
        self.assertEqual(4, head.next.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
