# -*- coding: utf-8 -*-

"""
题目：
    给定链表的头节点head，实现删除链表的中间节点的函数。
    例如：
        不删除任何节点；
        1-＞2，删除节点1；
        1-＞2-＞3，删除节点2；
        1-＞2-＞3-＞4，删除节点2；
        1-＞2-＞3-＞4-＞5，删除节点3；
    解答：
        链表长度每增加2（3，5，7…），要删除的节点就后移一个节点。
"""

import unittest
from utils.linked_list import Node


# 移除中间节点，返回更新后的头结点
def remove_mid_node(head):
    if head is None or head.next is None:
        return head
    if head.next.next is None:
        return head.next
    del_pre_node = head
    cur = head.next.next
    while (cur.next is not None) and (cur.next.next is not None):
        del_pre_node = del_pre_node.next
        cur = cur.next.next
    del_pre_node.next = del_pre_node.next.next
    return head


class MyTestCase(unittest.TestCase):
    def test_remove_mid_node(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = remove_mid_node(head)
        self.assertEqual(4, head.next.next.data)
        head = remove_mid_node(head)
        self.assertEqual(4, head.next.data)
        head = remove_mid_node(head)
        self.assertEqual(5, head.next.data)


if __name__ == '__main__':
    unittest.main()
