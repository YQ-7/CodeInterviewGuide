# -*- coding: utf-8 -*-
"""
题目：
    将单链表的每k个节点之间逆序
"""

import unittest
from utils.linked_list import Node
from utils.stack import Stack


def reverse_k_node_1(head, k):
    """
    方法一：利用栈结构的解法。
        1.从左到右遍历链表，如果栈的大小不等于K，就将节点不断压入栈中。
        2.当栈的大小第一次到达K时，说明第一次凑齐了K个节点进行逆序，从栈中依次弹出这些节点，并根据弹出的顺序重新连接，
        这一组逆序完成后，需要记录一下新的头部，同时第一组的最后一个节点（原来是头节点）应该连接下一个节点。
        3.步骤2之后，当栈的大小每次到达K时，说明又凑齐了一组应该进行逆序的节点，从栈中依次弹出这些节点，并根据弹出的顺序重新连接。
    时间复杂度:O(N)
    空间复杂度:O(K)
    """
    if k < 2:
        return head
    # 依次将k个节点压入栈
    # 待栈中压入k个节点时，依次出栈并链接
    k_stack = Stack()
    new_head = head  # 逆序链的头结点
    cur = head
    pre = None
    next = None
    while cur is not None:
        next = cur.next
        k_stack.push(cur)
        if k == k_stack.size():
            # 将新生成的k个逆序链与上一个链链接，并和下一个节点链接
            pre = reverse_k_stack(k_stack, pre, next)
            new_head = cur if new_head == head else new_head
        cur = next
    return new_head


def reverse_k_stack(stack, left, right):
    cur = stack.pop()
    if left is not None:
        left.next = cur
    next = None
    while not stack.is_empty():
        next = stack.pop()
        cur.next = next
        cur = next
    cur.next = right
    return cur


def reverse_k_node_2(head, k):
    """
    方法二：不需要栈结构，在原链表中直接调整。
        用变量记录每一组开始的第一个节点和最后一个节点，然后直接逆序调整，把这一组的节点都逆序。
        时间复杂度:O(N)
        空间复杂度:O(1)
    """
    if k < 2:
        return head
    # 依次遍历k个节点，记录这一段k节点的开始、结束节点
    cur = head
    pre = None
    start = None
    count = 1
    while cur is not None:
        next = cur.next
        if count == k:
            # 逆序开始到结束的节点
            start = head if pre is None else pre.next
            head = cur if pre is None else head
            reverse_k(pre, start, cur, next)
            pre = start
            count = 0
        count += 1
        cur = next
    return head


def reverse_k(left, start, end, right):
    pre = start
    cur = start.next
    next = None
    while cur != right:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    if left is not None:
        left.next = end
    start.next = right


class MyTestCase(unittest.TestCase):
    def test_reverse_k_node_1(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_8 = Node(8)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        node_6.next = node_7
        node_7.next = node_8
        new_head = reverse_k_node_1(head, 3)
        self.assertEqual(3, new_head.data)
        self.assertEqual(1, new_head.next.next.data)
        self.assertEqual(6, new_head.next.next.next.data)

    def test_reverse_k_node_2(self):
        head1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_8 = Node(8)
        head1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        node_6.next = node_7
        node_7.next = node_8
        new_head = reverse_k_node_2(head1, 3)
        self.assertEqual(3, new_head.data)
        self.assertEqual(1, new_head.next.next.data)
        self.assertEqual(6, new_head.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
