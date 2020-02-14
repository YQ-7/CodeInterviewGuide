# -*- coding: utf-8 -*-
"""
题目：
    给定二叉树的一个头节点head，已知其中没有重复值的节点，判断是否是完全二叉树
解答:
    1.按层遍历二叉树，从每层的左边向右边依次遍历所有的节点。
    2.如果当前节点有右孩子节点，但没有左孩子节点，则直接返回false。
    3.如果当前节点并不是左右孩子节点全有，那么之后的节点必须都为叶节点，否则返回false。
    4.遍历过程中如果不返回false，则遍历结束后返回true。
"""

import unittest
from utils.queue import Queue
from utils.linked_list import TreeNode


def is_cbt(head):
    if head is None:
        return True
    queue = Queue()
    leaf = False  # 是否只有叶节点
    queue.enqueue(head)
    while not queue.is_empty():
        cur = queue.dequeue()
        l_node = cur.left
        r_node = cur.right
        if (leaf and (l_node is not None or r_node is not None)) or (r_node is not None and l_node is None):
            return False
        if l_node is not None:
            queue.enqueue(l_node)
        if r_node is not None:
            queue.enqueue(r_node)
        else:
            # 没有右节点时，后续节点需要都是叶节点
            leaf = True
    return True


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(4)
        node_2 = TreeNode(2)
        node_3 = TreeNode(5)
        node_4 = TreeNode(1)
        node_5 = TreeNode(3)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        return head

    def test_something(self):
        self.assertTrue(is_cbt(self.make_data()))


if __name__ == '__main__':
    unittest.main()
