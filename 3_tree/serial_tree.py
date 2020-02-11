# -*- coding: utf-8 -*-
"""
题目：
    设计一种序列化和反序列化的方案
"""

import unittest
from utils.linked_list import TreeNode
from utils.queue import Queue


def serial_by_pre(head):
    """
        通过先序遍历序列化二叉树
        #: 代表Null值
        !: 节点结尾标志
    """
    if head is None:
        return "#!"
    res = str(head.data) + "!"
    res += serial_by_pre(head.left)
    res += serial_by_pre(head.right)
    return res


def recon_by_pre_str(pre_str):
    """
        将先序遍历序列化字符串反序列化成二叉树
    """
    values = pre_str.split("!")
    values.pop()
    values.reverse()
    return recon_pre_order(values)


def recon_pre_order(values):
    data = values.pop()
    if "#" == data:
        return None
    head = TreeNode(int(data))
    head.left = recon_pre_order(values)
    head.right = recon_pre_order(values)
    return head


def serial_by_level(head):
    """
        按照层序遍历序列化二叉树
        #: 代表Null值
        !: 节点结尾标志
    """
    if head is None:
        return "#!"
    res = str(head.data) + "!"
    queue = Queue()
    queue.enqueue(head)
    while not queue.is_empty():
        d = queue.dequeue()
        if d.left is not None:
            res += str(d.left.data) + "!"
            queue.enqueue(d.left)
        else:
            res += "#!"
        if d.right is not None:
            res += str(d.right.data) + "!"
            queue.enqueue(d.right)
        else:
            res += "#!"
    return res


def recon_by_level_str(level_str):
    values = level_str.split("!")
    values.pop()
    index = 0
    head = generate_node(values[index])
    index += 1
    queue = Queue()
    if head is not None:
        queue.enqueue(head)
    while not queue.is_empty():
        node = queue.dequeue()
        node.left = generate_node(values[index])
        index += 1
        node.right = generate_node(values[index])
        index += 1
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
    return head


def generate_node(val_str):
    if "#" == val_str:
        return None
    return TreeNode(int(val_str))


class MyTestCase(unittest.TestCase):
    def test_serial_by_pre(self):
        node_1 = TreeNode(12)
        node_2 = TreeNode(3)
        head = node_1
        head.left = node_2
        pre_str = serial_by_pre(head)
        self.assertEqual("12!3!#!#!#!", pre_str)
        recon_head = recon_by_pre_str(pre_str)
        self.assertEqual(12, recon_head.data)
        self.assertEqual(3, recon_head.left.data)
        self.assertIsNone(recon_head.right)
        self.assertIsNone(recon_head.left.left)
        self.assertIsNone(recon_head.left.right)

    def test_serial_by_level(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_3.right = node_5
        level_str = serial_by_level(head)
        self.assertEqual("1!2!3!4!#!#!5!#!#!#!#!", level_str)
        level_head = recon_by_level_str(level_str)
        self.assertEqual(1, level_head.data)
        self.assertEqual(2, level_head.left.data)
        self.assertEqual(3, level_head.right.data)
        self.assertEqual(4, level_head.left.left.data)
        self.assertEqual(5, level_head.right.right.data)


if __name__ == '__main__':
    unittest.main()
