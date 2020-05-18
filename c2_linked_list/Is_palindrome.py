# -*- coding: utf-8 -*-
"""
题目：
    给定一个链表的头节点head，请判断该链表是否为回文结构。
"""
import unittest
from utils.linked_list import Node
from utils.stack import Stack


def is_palindrome_1(head):
    """
        从左到右遍历链表，遍历的过程中把每个节点依次压入栈中。
        因为栈是先进后出的，所以在遍历完成后，从栈顶到栈底的节点值出现顺序会与原链表从左到右的值出现顺序反过来。
        那么，如果一个链表是回文结构，逆序之后，值出现的次序还是一样的，如果不是回文结构，顺序就肯定对不上。
        时间复杂度：O(N)
        空间复杂度：O(N)
    """
    if head is None or head.next is None:
        return True
    stack = Stack()
    cur = head
    while cur is not None:
        stack.push(cur.data)
        cur = cur.next

    while head is not None:
        if head.data != stack.pop():
            return False
        head = head.next
    return True


def is_palindrome_2(head):
    """
        把整个链表的右半部分压入栈中，压入完成后，再检查栈顶到栈底值出现的顺序是否和链表左半部分的值相对应。
        时间复杂度：O(N)
        空间复杂度：O(N) 相比方法1，节省了2/n空间
    """
    if head is None or head.next is None:
        return True

    right = head.next
    cur = head

    while cur.next is not None and cur.next.next is not None:
        right = right.next
        cur = cur.next.next

    stack = Stack()
    while right is not None:
        stack.push(right.data)
        right = right.next

    while not stack.is_empty():
        if head.data != stack.pop():
            return False
        head = head.next
    return True


def is_palindrome_3(head):
    """
        1.改变链表右半区的结构，使整个右半区反转，最后指向中间节点。
        2.leftStart和rightStart同时向中间点移动，移动每一步时都比较leftStart和rightStart节点的值，看是否一样。如果都一样，说明链表为回文结构，否则不是回文结构。
        3.不管最后返回的是true还是false，在返回前都应该把链表恢复成原来的样子。
        时间复杂度：O(N)
        空间复杂度：O(1)
    """
    if head is None or head.next is None:
        return True
    # 定位到中间节点
    n1 = head
    n2 = head
    while n2.next is not None and n2.next.next is not None:
        n1 = n1.next
        n2 = n2.next.next
    # 反转右半区节点
    n2 = n1.next
    n1.next = None
    n3 = None
    while n2 is not None:
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    # 回文检测
    n3 = n1
    n2 = head
    res = True
    while n1 is not None and n2 is not None:
        if n1.data != n2.data:
            res = False
            break
        n1 = n1.next
        n2 = n2.next
    # 恢复右半区节点
    n1 = n3.next
    n3.next = None
    while n1 is not None:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2
    return res


class MyTestCase(unittest.TestCase):
    def test_is_palindrome_1(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(2)
        node_5 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        self.assertEqual(True, is_palindrome_1(head))
        node_6 = Node(6)
        node_5.next = node_6
        self.assertEqual(False, is_palindrome_1(head))

    def test_is_palindrome_2(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(2)
        node_5 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        self.assertEqual(True, is_palindrome_2(head))
        node_6 = Node(6)
        node_5.next = node_6
        self.assertEqual(False, is_palindrome_2(head))

    def test_is_palindrome_3(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(2)
        node_5 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        self.assertEqual(True, is_palindrome_3(head))
        node_6 = Node(6)
        node_5.next = node_6
        self.assertEqual(False, is_palindrome_3(head))


if __name__ == '__main__':
    unittest.main()
