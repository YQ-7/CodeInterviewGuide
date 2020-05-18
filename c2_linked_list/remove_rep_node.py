# -*- coding: utf-8 -*-
"""
题目：
    移除无序单链表中值重复出现的节点
"""

import unittest
from utils.linked_list import Node


def remove_rep_node_1(head):
    """
    方法一：利用哈希表
        哈希表存储遍历过的节点数据
        1.当前遍历节点值不在哈希表中，将值存入哈希表
        2.当前遍历节点值已在哈希表中，将当前节点移除
    时间复杂度:O(N)
    空间复杂度:O(N)
    """
    if head is None:
        return
    # 用哈希表存放已遍历过的节点
    node_set = set()
    pre = head
    cur = head.next
    node_set.add(head.data)
    while cur is not None:
        # 当前节点值已在哈希表中出现，则删除此节点
        if cur.data in node_set:
            pre.next = cur.next
        else:
            node_set.add(cur.data)
            pre = cur
        cur = cur.next


def remove_rep_node_2(head):
    """
    方法二：2层遍历节点
        第一层：依次遍历节点
            第二层：移除与第一层当前节点值相等的节点
    时间复杂度:O(N^2)
    空间复杂度:O(1)
    """
    if head is None:
        return
    cur = head
    while cur is not None:
        pre = cur
        next = cur.next
        while next is not None:
            if cur.data == next.data:
                pre.next = next.next
            else:
                pre = next
            next = next.next
        cur = cur.next


class MyTestCase(unittest.TestCase):
    def test_remove_rep_node_1(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(3)
        node_5 = Node(4)
        node_6 = Node(4)
        node_7 = Node(3)
        node_8 = Node(2)
        node_9 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        node_6.next = node_7
        node_7.next = node_8
        node_8.next = node_9
        remove_rep_node_1(head)
        self.assertEqual(1, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(3, head.next.next.data)
        self.assertEqual(4, head.next.next.next.data)
        self.assertIsNone(head.next.next.next.next)

    def test_remove_rep_node_2(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(3)
        node_5 = Node(4)
        node_6 = Node(4)
        node_7 = Node(3)
        node_8 = Node(2)
        node_9 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        node_6.next = node_7
        node_7.next = node_8
        node_8.next = node_9
        remove_rep_node_2(head)
        self.assertEqual(1, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(3, head.next.next.data)
        self.assertEqual(4, head.next.next.next.data)
        self.assertIsNone(head.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
