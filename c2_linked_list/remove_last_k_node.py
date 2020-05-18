# -*- coding: utf-8 -*-

"""
题目：
    分别实现两个函数，一个可以删除单链表中倒数第K个节点，另一个可以删除双链表中倒数第K个节点。
"""

import unittest
from utils.linked_list import Node, DoubleNode


# 移除单链表倒数第k个节点，返回更新后的头结点
def remove_last_k_node(head, last_k):
    if head is None or last_k < 1:
        return head
    cur = head
    while cur is not None:
        last_k -= 1
        cur = cur.next
    # 删除的节点为头结点
    if last_k == 0:
        head = head.next

    if last_k < 0:
        cur = head
        last_k += 1
        while last_k < 0:
            last_k += 1
            cur = cur.next
        cur.next = cur.next.next
    return head


# 移除双向链表倒数第k个节点，返回更新后的头结点
def remove_last_k_double_node(head, last_k):
    if head is None or last_k < 1:
        return head
    cur = head
    while cur is not None:
        last_k -= 1
        cur = cur.next
    # 删除的节点为头结点
    if last_k == 0:
        head = head.next
        head.last = None
    if last_k < 0:
        cur = head
        last_k += 1
        while last_k < 0:
            last_k += 1
            cur = cur.next
        new_next = cur.next.next
        cur.next = new_next
        if new_next is not None:
            new_next.last = cur
    return head


class MyTestCase(unittest.TestCase):
    def test_remove_last_k_node(self):
        head1 = Node(1)
        node1_2 = Node(2)
        node1_3 = Node(3)
        node1_4 = Node(4)
        node1_5 = Node(5)
        head1.next = node1_2
        node1_2.next = node1_3
        node1_3.next = node1_4
        node1_4.next = node1_5
        head1 = remove_last_k_node(head1, 5)
        self.assertEqual(2, head1.data)
        head1 = remove_last_k_node(head1, 3)
        self.assertEqual(4, head1.next.data)

    def test_remove_last_k_double_node(self):
        head1 = DoubleNode(1)
        node1_2 = DoubleNode(2)
        node1_3 = DoubleNode(3)
        node1_4 = DoubleNode(4)
        node1_5 = DoubleNode(5)

        head1.next = node1_2
        node1_2.last = head1
        node1_2.next = node1_3
        node1_3.last = node1_2
        node1_3.next = node1_4
        node1_4.last = node1_3
        node1_4.next = node1_5
        node1_5.last = node1_4
        head1 = remove_last_k_double_node(head1, 5)
        self.assertEqual(2, head1.data)
        self.assertIsNone(head1.last)
        head1 = remove_last_k_double_node(head1, 3)
        self.assertEqual(4, head1.next.data)
        self.assertEqual(2, head1.next.last.data)


if __name__ == '__main__':
    unittest.main()
