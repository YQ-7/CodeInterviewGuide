# -*- coding: utf-8 -*-
"""
题目：
    给定一个无序单链表的头节点head，删除其中值重复出现的节点。
"""

import unittest
from utils.stack import Stack
from utils.linked_list import Node


def remove_value_1(head, value):
    """
        方法一：利用栈或者其他容器收集节点的方法
            将值不等于num的节点用栈收集起来，收集完成后重新连接即可。
        时间复杂度:O(N)
        空间复杂度:O(N)
    """
    if head is None:
        return head
    # 依次遍历链表，将不等于value的节点压入栈
    data_stack = Stack()
    while head is not None:
        if head.data != value:
            data_stack.push(head)
        head = head.next
    # 将栈中的节点重新链接
    while not data_stack.is_empty():
        data_stack.peek().next = head
        head = data_stack.pop()
    return head


def remove_value_2(head, value):
    """
        方法二：不用任何容器而直接调整的方法
            从链表头开始遍历，删除匹配的节点
        时间复杂度:O(N)
        空间复杂度:O(1)
    """
    # 若头节点是需要删除的节点，重置头节点
    while head is not None:
        if head.data != value:
            break
        head = head.next
    # 遍历后续节点，删除值匹配的节点
    cur = head
    pre = head
    while cur is not None:
        if cur.data == value:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head


class MyTestCase(unittest.TestCase):
    def test_remove_value_1(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(3)
        node_5 = Node(4)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = remove_value_1(head, 3)
        self.assertEqual(1, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(4, head.next.next.data)

    def test_remove_value_2(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(3)
        node_5 = Node(4)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = remove_value_2(head, 3)
        self.assertEqual(1, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(4, head.next.next.data)


if __name__ == '__main__':
    unittest.main()
