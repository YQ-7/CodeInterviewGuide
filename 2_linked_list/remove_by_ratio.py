# -*- coding: utf-8 -*-

"""
题目：
    给定链表的头节点head、整数a和b，实现删除位于a/b处节点的函数。
    例如：
        链表：1-＞2-＞3-＞4-＞5，假设a/b的值为r。
        如果r等于0，不删除任何节点；
        如果r在区间（0，1/5]上，删除节点1；
        如果r在区间（1/5，2/5]上，删除节点2；
        如果r在区间（2/5，3/5]上，删除节点3；
        如果r在区间（3/5，4/5]上，删除节点4；
        如果r在区间（4/5，1]上，删除节点5；
        如果r大于1，不删除任何节点。
    解答：
        计算doubler=（（double）（a*n））/（（double）b）的值，
        然后r向上取整之后的整数值代表该删除的节点是第几个节点。
"""

import unittest
from utils.linked_list import Node
import math


def remove_by_ratio(head, a, b):
    if a < 1 or a > b:
        return head
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next
    del_index = math.ceil(a * n / b)
    if del_index == 1:
        return head.next
    if del_index > 1:
        cur = head
        del_index -= 1
        while del_index != 1:
            del_index -= 1
            cur = cur.next
        cur.next = cur.next.next
    return head


class MyTestCase(unittest.TestCase):
    def test_remove_by_ratio(self):
        head = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        head = remove_by_ratio(head, 1, 5)
        self.assertEqual(2, head.data)
        head = remove_by_ratio(head, 3, 4)
        self.assertEqual(5, head.next.next.data)
        head = remove_by_ratio(head, 2, 3)
        self.assertEqual(2, head.data)
        self.assertEqual(5, head.next.data)


if __name__ == '__main__':
    unittest.main()
