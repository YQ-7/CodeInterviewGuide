# -*- coding: utf-8 -*-
"""
题目：
    给定二叉树的头结点，实现按层打印节点
"""

import unittest
from utils.linked_list import TreeNode
from utils.my_queue import Queue


def print_level(head):
    if head is None:
        return
    queue = Queue()
    queue.enqueue(head)
    level = 1
    # 记录当前层最右侧节点
    last = head
    # 跟踪记录宽度优先队列中的最新加入的节点
    n_last = None
    print("Level %d : " % level, end='')
    while not queue.is_empty():
        head = queue.dequeue()
        print(head.data, end=' ')
        if head.left is not None:
            queue.enqueue(head.left)
            n_last = head.left
        if head.right is not None:
            queue.enqueue(head.right)
            n_last = head.right
        if head == last and not queue.is_empty():
            level += 1
            print()
            print("Level %d: " % level, end='')
            last = n_last


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.right = node_4
        node_3.left = node_5
        node_3.right = node_6
        node_5.left = node_7
        node_5.right = node_8
        return head

    def test_print_level(self):
        print_level(self.make_data())


if __name__ == '__main__':
    unittest.main()
