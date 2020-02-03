# -*- coding: utf-8 -*-
"""
题目：
    给定一个单链表的头部节点head，链表长度为N，如果N为偶数，那么前N/2个节点算作左半区，
    后N/2个节点算作右半区；如果N为奇数，那么前N/2个节点算作左半区，后N/2+1个节点算作右半区。
    左半区从左到右依次记为L1-＞L2-＞…，右半区从左到右依次记为R1-＞R2-＞…，请将单链表调整成L1-＞R1-＞L2-＞R2-＞…的形式。
"""

import unittest
from utils.linked_list import Node


def relocate(head):
    if head is None or head.next is None:
        return
    # 查找左半区间最后一个节点
    mid = head
    right = head.next
    while right.next is not None and right.next.next is not None:
        mid = mid.next
        right = right.next.next
    right = mid.next
    # 将左边区域和后半区域交叉合并
    mid.next = None
    merge_l_r(head, right)


def merge_l_r(left, right):
    next = None
    while left.next is not None:
        next = right.next
        right.next = left.next
        left.next = right
        left = right.next
        right = next
    left.next = next


class MyTestCase(unittest.TestCase):
    def test_relocate(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        relocate(head)
        self.assertEqual(1, head.data)
        self.assertEqual(3, head.next.data)
        self.assertEqual(2, head.next.next.data)
        self.assertEqual(4, head.next.next.next.data)
        self.assertEqual(5, head.next.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
