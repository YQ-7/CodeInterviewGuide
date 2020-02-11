# -*- coding: utf-8 -*-
"""
题目：
    调整搜索二叉树中两个错误的节点
"""

import unittest
from utils.linked_list import TreeNode
from utils.stack import Stack


def get_tow_err_node(head):
    """
        找到出现错误的两个节点
        如果对所有的节点值都不一样的搜索二叉树进行中序遍历，那么出现的节点值会一直升序
        因此，如果有两个节点位置错了，就一定会出现降序
        第一个错误节点为第一次降序时较大的节点，第二个错误节点为最后一次降序时较小的节点
    """
    errs = [None] * 2
    if head is None:
        return errs
    # 中序遍历二叉树
    stack = Stack()
    cur = head
    pre = None
    while not stack.is_empty() or cur is not None:
        if cur is not None:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if pre is not None and pre.data > cur.data:
                # 第一个错误节点为第一次降序时较大的节点
                errs[0] = pre if errs[0] is None else errs[0]
                # 第二个错误节点为最后一次降序时较小的节点
                errs[1] = cur
            pre = cur
            cur = cur.right
    return errs


def recover_tree(head):
    """
        调整错误的两个节点，恢复搜索树
        基于两给节点的位置，共有14种情况
    """
    errs = get_tow_err_node(head)
    parents = get_two_parents(head, errs[0], errs[1])
    e1 = errs[0]
    e1_p = parents[0]
    e1_l = e1.left
    e1_r = e1.right
    e2 = errs[1]
    e2_p = parents[1]
    e2_l = e2.left
    e2_r = e2.right

    if e1 == head:
        if e1 == e2_p:
            # 1.e1是头节点，e1是e2的父节点，此时e2只可能是e1的右孩子节点
            e1.left = e2_l
            e1.right = e2_r
            e2.right = e1
            e2.left = e1_l
        elif e2_p.left == e2:
            # 2.e1是头节点，e1不是e2的父节点，e2是e2P的左孩子节点
            e2_p.left = e1
            e2.left = e1_l
            e2.right = e1_r
            e1.left = e2_l
            e1.right = e2_r
        else:
            # 3.e1是头节点，e1不是e2的父节点，e2是e2P的右孩子节点
            e2_p.right = e1
            e2.left = e1_l
            e2.right = e1_r
            e1.left = e2_l
            e1.right = e2_r
        head = e2
    elif e2 == head:
        if e2 == e1_p:
            # 4.e2是头节点，e2是e1的父节点，此时e1只可能是e2的左孩子节点
            e2.left = e1_l
            e2.right = e1_r
            e1.left = e1
            e1.right = e1_r
        elif e1_p == e1:
            # 5.e2是头节点，e2不是e1的父节点，e1是e1P的左孩子节点
            e1_p.left = e2
            e1.left = e2_l
            e1.right = e2_r
            e2.left = e1_l
            e2.right = e1_r
        else:
            # e2是头节点，e2不是e1的父节点，e1是e1P的右孩子节点
            e1_p.right = e2
            e1.left = e2_l
            e1.right = e2_r
            e2.left = e1_l
            e2.right = e1_r
        head = e1
    else:
        if e1 == e2_p:
            if e1_p.left == e1:
                # e1和e2都不是头节点，e1是e2的父节点，此时e2只可能是e1的右孩子节点，e1是e1P的左孩子节点
                e1_p.left = e2
                e1.left = e2_l
                e1.right = e2_r
                e2.left = e1_l
                e2.right = e1
            else:
                # e1和e2都不是头节点，e1是e2的父节点，此时e2只可能是e1的右孩子节点，e1是e1P的左孩子节点
                e1_p.right = e2
                e1.left = e2_l
                e1.right = e2_r
                e2.left = e1_l
                e2.right = e1
        elif e2 == e1_p:
            if e2_p.left == e2:
                # e1和e2都不是头节点，e2是e1的父节点，此时e1只可能是e2的左孩子节点，e2是e2P的左孩子节点
                e2_p.left = e1
                e2.left = e1_l
                e2.right = e1_r
                e1.left = e2
                e1.right = e2_r
            else:
                # e1和e2都不是头节点，e2是e1的父节点，此时e1只可能是e2的左孩子节点，e2是e2P的右孩子节点
                e2_p.right = e1
                e2.left = e1_l
                e2.right = e1_r
                e1.left = e2
                e1.right = e2_r
        else:
            if e1_p.left == e1:
                if e2_p.left == e2:
                    # e1和e2都不是头节点，谁也不是谁的父节点，e1是e1P的左孩子节点，e2是e2P的左孩子节点
                    e1.left = e2_l
                    e1.right = e2_r
                    e2.left = e1_l
                    e2.right = e1_r
                    e1_p.left = e2
                    e2_p.left = e1
                else:
                    # e1和e2都不是头节点，谁也不是谁的父节点，e1是e1P的左孩子节点，e2是e2P的右孩子节点
                    e1.left = e2_l
                    e1.right = e2_r
                    e2.left = e1_l
                    e2.right = e1_r
                    e1_p.left = e2
                    e2_p.right = e1
            else:
                if e2_p.left == e2:
                    # e1和e2都不是头节点，谁也不是谁的父节点，e1是e1P的右孩子节点，e2是e2P的左孩子节点
                    e1.left = e2_l
                    e1.right = e2_r
                    e2.left = e1_l
                    e2.right = e1_r
                    e1_p.right = e2
                    e2_p.left = e1
                else:
                    # e1和e2都不是头节点，谁也不是谁的父节点，e1是e1P的右孩子节点，e2是e2P的右孩子节点
                    e1.left = e2_l
                    e1.right = e2_r
                    e2.left = e1_l
                    e2.right = e1_r
                    e1_p.right = e2
                    e2_p.right = e1

    return head


def get_two_parents(head, e1, e2):
    parents = [None] * 2
    if head is None:
        return parents
    stack = Stack()
    cur = head
    while not stack.is_empty() or cur is not None:
        if cur is not None:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur.left == e1 or cur.right == e1:
                parents[0] = cur
            if cur.left == e2 or cur.right == e2:
                parents[1] = cur
            cur = cur.right
    return parents


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(5)
        node_2 = TreeNode(1)
        node_3 = TreeNode(4)
        node_4 = TreeNode(3)
        node_5 = TreeNode(2)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_3.left = node_4
        node_3.right = node_5
        return head

    def test_get_tow_err_node(self):
        errs = get_tow_err_node(self.make_data())
        self.assertEqual(5, errs[0].data)
        self.assertEqual(2, errs[1].data)

    def test_recover_tree(self):
        head = recover_tree(self.make_data())
        self.assertEqual(2, head.data)
        self.assertEqual(1, head.left.data)
        self.assertEqual(4, head.right.data)
        self.assertEqual(3, head.right.left.data)
        self.assertEqual(5, head.right.right.data)


if __name__ == '__main__':
    unittest.main()
