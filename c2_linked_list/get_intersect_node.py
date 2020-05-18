# -*- coding: utf-8 -*-
"""
题目：
    判断两个链表是否相交，若相交则并返回第一个相交的节点
"""
import unittest
from utils.linked_list import Node


def get_loop_node(head):
    """
        判断一个链表是否有环，如果有，则返回第一个进入环的节点，没有则返回null。
    """
    if head is None or head.next is None or head.next.next is None:
        return None
    # 设置一个慢指针slow(每次移动1步)和一个快指针fast(每次移动2步)
    # 如果链表没有环，fast指针一定先移动到Node
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next is None or fast.next.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    # 如果有环，fast和slow会在某个位置相遇
    # 相遇后，调制移动方式：fast指向链表头，fast和slow每次移动1步
    # fast指针和slow指针一定会再次相遇，并且在第一个入环的节点处相遇
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


def get_cross_no_loop(head1, head2):
    """
        判断两个无环链表是否相交，相交则返回第一个相交节点，不相交则返回null。
    """
    # 分别遍历到链表尾节点，记录链表长度
    if head1 is None or head2 is None:
        return None
    len_1 = 1
    cur1 = head1
    while cur1.next is not None:
        len_1 += 1
        cur1 = cur1.next
    len_2 = 1
    cur2 = head2
    while cur2.next is not None:
        len_2 += 1
        cur2 = cur2.next
    # 尾节点是同一个节点，则两链表相交
    if cur1 != cur2:
        return None
    # 先将较长的链表移动|len1 - len2|的长度
    len_sub = len_1 - len_2
    long_cur = head1 if len_sub > 0 else head2
    short_cur = head2 if long_cur == head1 else head1
    len_sub = abs(len_sub)
    while len_sub > 0:
        len_sub -= 1
        long_cur = long_cur.next
    # 两链表开始同时遍历，第一个相同的节点即第一个交点
    while long_cur != short_cur:
        long_cur = long_cur.next
        short_cur = short_cur.next
    return long_cur


def both_loop(head1, loop1, head2, loop2):
    """
       判断两个有环链表是否相交，相交则返回第一个相交节点，不相交则返回null。
    """
    if loop1 == loop2:
        len_1 = 0
        cur1 = head1
        while cur1 != loop1:
            len_1 += 1
            cur1 = cur1.next
        len_2 = 0
        cur2 = head2
        while cur2 != loop2:
            len_2 += 1
            cur2 = cur2.next
        # 尾节点是同一个节点，则两链表相交
        if cur1 != cur2:
            return None
        # 先将较长的链表移动|len1 - len2|的长度
        len_sub = len_1 - len_2
        long_cur = head1 if len_sub > 0 else head2
        short_cur = head2 if long_cur == head1 else head1
        len_sub = abs(len_sub)
        while len_sub > 0:
            len_sub -= 1
            long_cur = long_cur.next
        # 两链表开始同时遍历，第一个相同的节点即第一个交点
        while long_cur != short_cur:
            long_cur = long_cur.next
            short_cur = short_cur.next
        return long_cur
    else:
        cur_1 = loop1.next
        while cur_1 != loop1:
            if cur_1 == loop2:
                return loop1
            cur_1 = cur_1.next
        return None


def get_intersect_node(head1, head2):
    if head1 is None or head2 is None:
        return None
    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    if loop1 is None and loop2 is None:
        return get_cross_no_loop(head1, head2)
    if loop1 is not None and loop2 is not None:
        return both_loop(head1, head2, loop1, loop2)
    return None


class MyTestCase(unittest.TestCase):
    def test_get_loop_node(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        self.assertIsNone(get_loop_node(head))
        node_5.next = node_3
        self.assertTrue(3, get_loop_node(head).data)

    def test_get_cross_no_loop(self):
        head1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5

        head2 = Node(11)
        node2_2 = Node(12)
        head2.next = node2_2
        self.assertIsNone(get_cross_no_loop(head1, head2))
        self.assertIsNone(get_intersect_node(head1, head2))
        node2_2.next = node_3
        self.assertEqual(3, get_cross_no_loop(head1, head2).data)
        self.assertEqual(3, get_intersect_node(head1, head2).data)

    def test_get_cross_no_loop(self):
        head1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head1.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_3

        head2 = Node(11)
        node2_2 = Node(12)
        node2_3 = Node(13)
        head2.next = node2_2
        node2_2.next = node2_3
        node2_3.next = node_2
        self.assertTrue(2, get_intersect_node(head1, head2).data)


if __name__ == '__main__':
    unittest.main()
