# -*- coding: utf-8 -*-
"""
题目：
    假设链表中每一个节点的值都在0～9之间，那么链表整体就可以代表一个整数。
    给定两个这种链表的头节点head1和head2，请生成代表两个整数相加值的结果链表。
"""

import unittest
from utils.stack import Stack
from utils.linked_list import Node


def add_list_1(head1, head2):
    """
        利用栈结构
    """
    # 分别将2个链表值压入栈
    stack1 = Stack()
    stack2 = Stack()
    cur = head1
    while cur is not None:
        stack1.push(cur.data)
        cur = cur.next
    cur = head2
    while cur is not None:
        stack2.push(cur.data)
        cur = cur.next
    # 依次将栈中的元素相加，生成结果链
    ca = 0  # 进位
    n1 = 0  # 加数1
    n2 = 0  # 加数2
    n = 0  # n1 + n2 + ca
    res_node_head = None  # 结果链
    pre = None
    while not stack1.is_empty() or not stack2.is_empty():
        n1 = stack1.pop() if not stack1.is_empty() else 0
        n2 = stack2.pop() if not stack2.is_empty() else 0
        n = n1 + n2 + ca
        pre = res_node_head
        res_node_head = Node(n % 10)
        res_node_head.next = pre
        ca = n // 10
    if ca == 1:
        pre = res_node_head
        res_node_head = Node(1)
        res_node_head.next = pre
    return res_node_head


def add_list_2(head1, head2):
    """
        利用链表的逆序求解，节约用栈的空间
    """
    # 将2个链表逆序
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    # 遍历逆序后的链表，计算结果链
    ca = 0  # 进位
    n1 = 0  # 加数1
    n2 = 0  # 加数2
    n = 0  # n1 + n2 + ca
    res_node_head = None  # 结果链
    pre = None
    cur1 = head1
    cur2 = head2
    while cur1 is not None or cur2 is not None:
        n1 = cur1.data if cur1 is not None else 0
        n2 = cur2.data if cur2 is not None else 0
        n = n1 + n2 + ca
        pre = res_node_head
        res_node_head = Node(n % 10)
        res_node_head.next = pre
        ca = n // 10
        cur1 = cur1.next if cur1 is not None else None
        cur2 = cur2.next if cur2 is not None else None
    if ca == 1:
        pre = res_node_head
        res_node_head = Node(1)
        res_node_head.next = pre
    # 还原逆序的链表
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    return res_node_head


def reverse_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


class MyTestCase(unittest.TestCase):
    def test_add_list_1(self):
        head1 = Node(9)
        node1_2 = Node(3)
        node1_3 = Node(7)
        head1.next = node1_2
        node1_2.next = node1_3

        head2 = Node(6)
        node2_2 = Node(3)
        head2.next = node2_2
        res = add_list_1(head1, head2)
        self.assertEqual(1, res.data)
        self.assertEqual(0, res.next.data)
        self.assertEqual(0, res.next.next.data)
        self.assertEqual(0, res.next.next.next.data)

    def test_add_list_2(self):
        head1 = Node(9)
        node1_2 = Node(3)
        node1_3 = Node(7)
        head1.next = node1_2
        node1_2.next = node1_3

        head2 = Node(6)
        node2_2 = Node(3)
        head2.next = node2_2
        res = add_list_2(head1, head2)
        self.assertEqual(1, res.data)
        self.assertEqual(0, res.next.data)
        self.assertEqual(0, res.next.next.data)
        self.assertEqual(0, res.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
