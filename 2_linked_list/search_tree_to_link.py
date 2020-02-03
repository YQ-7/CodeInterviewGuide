# -*- coding: utf-8 -*-
"""
题目：
    将搜索二叉树转换成双向链表
"""

import unittest
from utils.queue import Queue
from utils.linked_list import TreeNode


def search_tree_to_link_1(head):
    """
        方法一：用队列等容器收集二叉树中序遍历结果的方法
        时间复杂度为O（N）
        空间复杂度为O（N）
    """
    queue = Queue()
    # 按照二叉树中序遍历将节点放入队列
    in_order_to_queue(head, queue)
    # 将队列中的节点弹出并链接
    head = queue.dequeue()
    pre = head
    pre.left = None
    while not queue.is_empty():
        cur = queue.dequeue()
        pre.right = cur
        cur.left = pre
        pre = cur
    cur.right = None
    return head


def in_order_to_queue(head, queue):
    if head is None:
        return
    in_order_to_queue(head.left, queue)
    queue.enqueue(head)
    in_order_to_queue(head.right, queue)


class ReturnType(object):

    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value


def search_tree_to_link_2(head):
    """
        方法二：利用递归函数，除此之外，不使用任何容器的方法。
            先把以X为头的搜索二叉树的左子树转换为有序双向链表，并且返回左子树有序双向链表的头和尾，
            然后把以X为头的搜索二叉树的右子树转换为有序双向链表，并且返回右子树有序双向链表的头和尾，
            接着通过X把两部分接起来即可。
        时间复杂度为O（N）
        空间复杂度为O（h），h为二叉树的高度。
    """
    if head is None:
        return head
    return process(head).start


def process(head):
    if head is None:
        return ReturnType(None, None)
    left_list = process(head.left)
    right_list = process(head.right)
    if left_list.end is not None:
        left_list.end.right = head
    head.left = left_list.end
    head.right = right_list.start
    if right_list.start is not None:
        right_list.start.left = head
    return ReturnType(
        left_list.start if left_list.start is not None else head,
        right_list.end if right_list.end is not None else head
    )


class MyTestCase(unittest.TestCase):
    def test_search_tree_to_link_1(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        node_9 = TreeNode(9)
        head = node_6
        head.left = node_4
        head.right = node_7
        node_4.left = node_2
        node_4.right = node_5
        node_2.left = node_1
        node_2.right = node_3
        node_7.right = node_9
        node_9.left = node_8
        head = search_tree_to_link_1(head)

        self.assertEqual(1, head.data)
        self.assertEqual(2, head.right.data)
        self.assertEqual(1, head.right.left.data)
        self.assertEqual(3, head.right.right.data)
        self.assertEqual(4, head.right.right.right.data)
        self.assertEqual(2, head.right.right.left.data)

    def test_search_tree_to_link_2(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        node_9 = TreeNode(9)
        head = node_6
        head.left = node_4
        head.right = node_7
        node_4.left = node_2
        node_4.right = node_5
        node_2.left = node_1
        node_2.right = node_3
        node_7.right = node_9
        node_9.left = node_8
        head = search_tree_to_link_2(head)

        self.assertEqual(1, head.data)
        self.assertEqual(2, head.right.data)
        self.assertEqual(1, head.right.left.data)
        self.assertEqual(3, head.right.right.data)
        self.assertEqual(4, head.right.right.right.data)
        self.assertEqual(2, head.right.right.left.data)


if __name__ == '__main__':
    unittest.main()
