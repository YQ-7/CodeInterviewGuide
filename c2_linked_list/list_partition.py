# -*- coding: utf-8 -*-
"""
题目：
    给定一个单向链表的头节点head，节点的值类型是整型，再给定一个整数pivot。
    实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点。
"""
import unittest
from utils.linked_list import Node


def list_partition_1(head, pivot):
    """
        把链表中的所有节点放入一个额外的数组中，然后统一调整位置。
        基于分割元素划分的左、中、右三个部分的内部不做顺序要求，
        时间复杂度：O(N)
        空间复杂度：O(N)
    """
    if head is None:
        return head
    # 将链表元素依次放入数组
    node_arr = []
    cur = head
    while cur is not None:
        node_arr.append(cur)
        cur = cur.next
    # 按照pivot划分数组：把小于pivot的节点放在左边，把相等的放中间，把大于的放在右边
    arr_partition(node_arr, pivot)
    # 将数组元素依次重连成链表
    for i in range(1, len(node_arr)):
        node_arr[i - 1].next = node_arr[i]
    node_arr[len(node_arr) - 1].next = None
    return node_arr[0]


def arr_partition(node_arr, pivot):
    small = -1
    big = len(node_arr)
    index = 0
    while index != big:
        if node_arr[index].data < pivot:
            small += 1
            swap(node_arr, index, small)
            index += 1
        elif node_arr[index].data == pivot:
            index += 1
        else:
            big -= 1
            swap(node_arr, index, big)


def swap(node_arr, a, b):
    tmp = node_arr[a]
    node_arr[a] = node_arr[b]
    node_arr[b] = tmp


def list_partition_2(head, pivot):
    """
        1.将原链表中的所有节点依次划分进三个链表，三个链表分别为small代表左部分，equal代表中间部分，big代表右部分。
        2.将small、equal和big三个链表重新串起来即可。
        时间复杂度：O(N)
        空间复杂度：O(1)
    """
    small_h = None
    small_t = None

    equal_h = None
    equal_t = None

    big_h = None
    big_t = None
    # 将节点按照pivot划分为3个链表
    while head is not None:
        next = head.next
        head.next = None
        if head.data < pivot:
            if small_h is None:
                small_h = head
                small_t = head
            else:
                small_t.next = head
                small_t = head
        elif head.data == pivot:
            if equal_h is None:
                equal_h = head
                equal_t = head
            else:
                equal_t.next = head
                equal_t = head
        else:
            if big_h is None:
                big_h = head
                big_t = head
            else:
                big_t.next = head
                big_t = head
        head = next
    # 链接划分的3个链表
    if small_t is not None:
        small_t.next = equal_h
        equal_t = equal_t if equal_t is not None else small_t

    if equal_t is not None:
        equal_t.next = big_h

    head = small_h if small_h is not None else \
        (equal_h if equal_h is not None else big_h)
    return head


class MyTestCase(unittest.TestCase):
    def test_list_partition_1(self):
        head = Node(9)
        node_2 = Node(0)
        node_3 = Node(4)
        node_4 = Node(3)
        node_5 = Node(5)
        node_6 = Node(1)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        head = list_partition_1(head, 3)
        self.assertTrue(head.data < 3)
        self.assertTrue(head.next.data < 3)
        self.assertTrue(head.next.next.data == 3)
        self.assertTrue(head.next.next.next.data > 3)

    def test_list_partition_2(self):
        head = Node(7)
        node_2 = Node(9)
        node_3 = Node(1)
        node_4 = Node(8)
        node_5 = Node(5)
        node_6 = Node(2)
        node_7 = Node(5)
        head.next = node_2
        node_2.next = node_3
        node_3.next = node_4
        node_4.next = node_5
        node_5.next = node_6
        node_6.next = node_7
        head = list_partition_2(head, 5)
        self.assertEqual(1, head.data)
        self.assertEqual(2, head.next.data)
        self.assertEqual(5, head.next.next.data)
        self.assertEqual(5, head.next.next.next.data)
        self.assertEqual(7, head.next.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
