# -*- coding: utf-8 -*-
"""
题目：
    遍历二叉树
"""

import unittest
from utils.linked_list import TreeNode
from utils.stack import Stack


def pre_order_recur(head):
    """
    先序遍历，递归版
    """
    if head is None:
        return
    print(head.data, end=' ')
    pre_order_recur(head.left)
    pre_order_recur(head.right)


def pre_order_un_recur(head):
    """
    先序遍历，非递归版，用栈实现
    """
    if head is None:
        return
    stack = Stack()
    # 先将头节点入栈
    stack.push(head)
    while not stack.is_empty():
        # 将栈底数据出栈打印
        cur = stack.pop()
        print(cur.data, end=' ')
        # 将右节点入栈
        if cur.right is not None:
            stack.push(cur.right)
        # 将左节点入栈
        if cur.left is not None:
            stack.push(cur.left)


def in_order_recur(head):
    """
    中序遍历，递归版
    """
    if head is None:
        return
    in_order_recur(head.left)
    print(head.data, end=' ')
    in_order_recur(head.right)


def in_order_un_recur(head):
    """
    中序遍历，非递归版，用栈实现
    """
    if head is None:
        return
    stack = Stack()
    cur = head
    while not stack.is_empty() or cur is not None:
        if cur is not None:
            # 将当前节点入栈
            stack.push(cur)
            # 优先遍历左节点
            cur = cur.left
        else:
            # 出栈元素并打印
            cur = stack.pop()
            print(cur.data, end=' ')
            # 遍历右节点
            cur = cur.right


def post_order_recur(head):
    """
    后序遍历，递归版
    """
    if head is None:
        return
    post_order_recur(head.left)
    post_order_recur(head.right)
    print(head.data, end=' ')


def post_order_un_recur1(head):
    """
    后序遍历，非递归版，用2个栈来实现
    """
    if head is None:
        return
    s = Stack()
    print_s = Stack()  # 按后序顺序存储
    s.push(head)
    while not s.is_empty():
        cur = s.pop()
        print_s.push(cur)
        if cur.left is not None:
            s.push(cur.left)
        if cur.right is not None:
            s.push(cur.right)
    while not print_s.is_empty():
        cur = print_s.pop()
        print(cur.data, end=' ')


def post_order_un_recur2(head):
    """
    后序遍历，非递归版，用1个栈来实现
    """
    if head is None:
        return
    stack = Stack()
    stack.push(head)
    h = None
    while not stack.is_empty():
        c = stack.peek()
        if c.left is not None and h != c.left and h != c.right:
            stack.push(c.left)
        elif c.right is not None and h != c.right:
            stack.push(c.right)
        else:
            print(stack.pop().data, end=' ')
            h = c


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
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.left = node_6
        node_3.right = node_7
        return head

    def test_pre_order_recur(self):
        print("pre order recur:", end=' ')
        pre_order_recur(self.make_data())
        print()

    def test_pre_order_un_recur(self):
        print("pre order unRecur:", end=' ')
        pre_order_un_recur(self.make_data())
        print()

    def test_in_order_recur(self):
        print("in order recur:", end=' ')
        in_order_recur(self.make_data())
        print()

    def test_in_order_un_recur(self):
        print("in order unRecur:", end=' ')
        in_order_un_recur(self.make_data())
        print()

    def test_post_order_recur(self):
        print("post order recur:", end=' ')
        post_order_recur(self.make_data())
        print()

    def test_post_order_un_recur1(self):
        print("post order unrRecur1:", end=' ')
        post_order_un_recur1(self.make_data())
        print()

    def test_post_order_un_recur2(self):
        print("post order unrRecur2:", end=' ')
        post_order_un_recur2(self.make_data())
        print()


if __name__ == '__main__':
    unittest.main()
