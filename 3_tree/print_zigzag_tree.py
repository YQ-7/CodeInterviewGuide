# -*- coding: utf-8 -*-
"""
题目：
    给定二叉树的头结点，实现按ZigZag打印节点
"""

import unittest
from utils.linked_list import TreeNode
from utils.deque import Deque


def print_zigzag(head):
    if head is None:
        return
    deque = Deque()
    deque.append(head)
    level = 1
    # 记录打印方向
    # True: 左 -> 右
    # False: 右 -> 左
    lr = True
    # 记录当前层最右侧节点
    last = head
    # 跟踪记录宽度优先队列中的最新加入的节点
    n_last = None
    print_title(level, lr)
    while not deque.is_empty():
        if lr:
            # 从左向右过程
            # 取出队列头部元素
            head = deque.popleft()
            # 将左节点从尾部进入队列
            if head.left is not None:
                n_last = head.left if n_last is None else n_last
                deque.append(head.left)
            # 将右节点从尾部进入队列
            if head.right is not None:
                n_last = head.right if n_last is None else n_last
                deque.append(head.right)
        else:
            # 从右向左过程
            # 取出队列尾部元素
            head = deque.pop()
            # 将右节点从头部进入队列
            if head.right is not None:
                n_last = head.right if n_last is None else n_last
                deque.appendleft(head.right)
            # 将左节点从头部进入队列
            if head.left is not None:
                n_last = head.left if n_last is None else n_last
                deque.appendleft(head.left)
        # 判断是否换行
        # 更新lr、last、n_last
        print(head.data, end=" ")
        if head == last and not deque.is_empty():
            lr = not lr
            last = n_last
            n_last = None
            print()
            level += 1
            print_title(level, lr)


def print_title(level, lr):
    print("Level %d from " % level, end='')
    print("left to right: " if lr else "right to left: ", end='')


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

    def test_print_zigzag(self):
        print_zigzag(self.make_data())


if __name__ == '__main__':
    unittest.main()
