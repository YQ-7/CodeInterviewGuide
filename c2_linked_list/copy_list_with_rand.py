# -*- coding: utf-8 -*-
"""
题目：
    复制含有随机节点的链表
"""


import unittest
from utils.linked_list import Node


class RandNode(Node):

    def __init__(self, data):
        super().__init__(data)
        self._rand = None

    @property
    def rand(self):
        return self._rand

    @rand.setter
    def rand(self, value):
        self._rand = value


def copy_list_with_rand_1(head):
    """
    使用哈希表版本
    """
    if head is None:
        return head
    # 将链表节点复制到哈希表中：key:原节点 value:副本节点
    node_copy_map = {}
    cur = head
    while cur is not None:
        node_copy_map[cur] = RandNode(cur.data)
        cur = cur.next
    # 对副本节点next、rand变量赋值
    cur = head
    while cur is not None:
        node_copy_map.get(cur).next = node_copy_map.get(cur.next)
        node_copy_map.get(cur).rand = node_copy_map.get(cur.rand)
        cur = cur.next
    # 返回副本节点头节点
    return node_copy_map.get(head)


def copy_list_with_rand_2(head):
    """
    不使用哈希表版本
    """
    if head is None:
        return head
    # 复制并链接每一个节点：副本节点放置在cur和下一个节点中间
    cur = head
    next = None
    while cur is not None:
        next = cur.next
        cur.next = RandNode(cur.data)
        cur.next.next = next
        cur = next
    # 设置副本节点的rand指针
    cur = head
    cur_copy = None
    while cur is not None:
        next = cur.next.next
        cur_copy = cur.next
        cur_copy.rand = cur.rand.next if cur.rand is not None else None
        cur = next
    # 拆分出原链表和副本链表
    cur = head
    res = head.next
    while cur is not None:
        next = cur.next.next
        cur_copy = cur.next
        cur.next = next
        cur_copy.next = next.next if next is not None else None
        cur = next
    # 返回副本节点头节点
    return res


class MyTestCase(unittest.TestCase):
    def test_copy_list_with_rand_1(self):
        head = RandNode(1)
        node_2 = RandNode(2)
        node_3 = RandNode(3)
        head.next = node_2
        head.rand = node_3
        node_2.next = node_3
        node_3.rand = head
        new_head = copy_list_with_rand_1(head)
        self.assertEqual(1, new_head.data)
        self.assertEqual(3, new_head.rand.data)
        self.assertEqual(2, new_head.next.data)
        self.assertIsNone(new_head.next.rand)
        self.assertEqual(3, new_head.next.next.data)
        self.assertEqual(1, new_head.next.next.rand.data)

    def test_copy_list_with_rand_2(self):
        head = RandNode(1)
        node_2 = RandNode(2)
        node_3 = RandNode(3)
        head.next = node_2
        head.rand = node_3
        node_2.next = node_3
        node_3.rand = head
        new_head = copy_list_with_rand_2(head)
        self.assertEqual(1, new_head.data)
        self.assertEqual(3, new_head.rand.data)
        self.assertEqual(2, new_head.next.data)
        self.assertIsNone(new_head.next.rand)
        self.assertEqual(3, new_head.next.next.data)
        self.assertEqual(1, new_head.next.next.rand.data)


if __name__ == '__main__':
    unittest.main()
