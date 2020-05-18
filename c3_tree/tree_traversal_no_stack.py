# -*- coding: utf-8 -*-
"""
题目：
    给定一棵二叉树的头节点head，完成二叉树的先序、中序和后序遍历。如果二叉树的节点数为N，
    则要求时间复杂度为O（N），额外空间复杂度为O（1）。
解答：
    利用Morris遍历实现
    Morris遍历的实质就是避免用栈结构，而是让下层到上层有指针，具体是通过让底层节点指向null的空闲指针指回上层的某个节点，
    从而完成下层到上层的移动。
"""

import unittest
from utils.linked_list import TreeNode


def morris_pre(head):
    """
        通过Morris遍历实现二叉树先序遍历
        1.对于cur只能到达一次的节点（无左子树的节点），cur到达时直接打印。
        2.对于cur可以到达两次的节点（有左子树的节点），cur第一次到达时打印，第二次到达时打印。
    """
    if head is None:
        return
    cur = head
    while cur is not None:
        # cur有左子树
        most_right = cur.left
        if most_right is not None:
            # 找到cur左子树上最右节点
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                # mon_right.right指向cur
                # 以便遍历完左子树后，可以通过此索引返回
                most_right.right = cur
                print(cur.data, end=" ")
                # cur 相左移动
                cur = cur.left
                continue
            else:
                # 若过most_right.right == cur,将其还原为null
                most_right.right = None
        else:
            print(cur.data, end=" ")
        # cur没有左子树，cur向右移动
        # 或cur左子树最右节点右指针指向cur，cur向右移动
        cur = cur.right


def morris_in(head):
    """
        通过Morris遍历实现二叉树中序遍历
        1.对于cur只能到达一次的节点（无左子树的节点），cur到达时直接打印。
        2.对于cur可以到达两次的节点（有左子树的节点），cur第一次到达时不打印，第二次到达时打印。
    """
    if head is None:
        return
    cur = head
    while cur is not None:
        # cur有左子树
        most_right = cur.left
        if most_right is not None:
            # 找到cur左子树上最右节点
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                # mon_right.right指向cur
                # 以便遍历完左子树后，可以通过此索引返回
                most_right.right = cur
                # cur 相左移动
                cur = cur.left
                continue
            else:
                # 若过most_right.right == cur,将其还原为null
                most_right.right = None
        print(cur.data, end=" ")
        # cur没有左子树，cur向右移动
        # 或cur左子树最右节点右指针指向cur，cur向右移动
        cur = cur.right


def morris_post(head):
    """
        通过Morris遍历实现二叉树后序遍历
        1.对于cur只能到达一次的节点（无左子树的节点），直接跳过，没有打印行为。
        2.对于cur可以到达两次的任何一个节点（有左子树的节点）X，cur第一次到达X时没有打印行为；
          当第二次到达X时，逆序打印X左子树的右边界。
        3.cur遍历完成后，逆序打印整棵树的右边界。
    """
    if head is None:
        return
    cur = head
    while cur is not None:
        # cur有左子树
        most_right = cur.left
        if most_right is not None:
            # 找到cur左子树上最右节点
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                # mon_right.right指向cur
                # 以便遍历完左子树后，可以通过此索引返回
                most_right.right = cur
                # cur 相左移动
                cur = cur.left
                continue
            else:
                # 若过most_right.right == cur,将其还原为null
                most_right.right = None
                print_edge(cur.left)
        # cur没有左子树，cur向右移动
        # 或cur左子树最右节点右指针指向cur，cur向右移动
        cur = cur.right
    print_edge(head)


# 逆序打印树的右边界
def print_edge(head):
    tail = reverse_edge(head)
    cur = tail
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.right
    reverse_edge(tail)


def reverse_edge(head):
    pre = None
    while head is not None:
        next = head.right
        head.right = pre
        pre = head
        head = next
    return pre


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

    def test_morris_pre(self):
        print("morris pre order:", end=' ')
        morris_pre(self.make_data())
        print()

    def test_morris_in(self):
        print("morris in order:", end=' ')
        morris_in(self.make_data())
        print()

    def test_morris_post(self):
        print("morris post order:", end=' ')
        morris_post(self.make_data())
        print()


if __name__ == '__main__':
    unittest.main()
