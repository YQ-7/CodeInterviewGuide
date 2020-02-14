# -*- coding: utf-8 -*-
"""
题目：
    给定一棵完全二叉树的头节点head，返回这棵树的节点个数
"""

import unittest
from utils.linked_list import TreeNode


def num_num(head):
    """
        时间复杂度：O(h^2)，每层只会选择一个节点进行bs递归O(h)，每次调用bs，都会计算节点右子树的最左节点O(h)
    """
    if head is None:
        return 0
    return bs(head, 1, most_left_level(head, 1))


def bs(node, level, h):
    if level == h:
        return 1
    if most_left_level(node.right, level + 1) == h:
        # node右子树叶节点能到达h层，证明node左子树为h-level的满二叉树
        return (1 << (h - level)) + bs(node.right, level + 1, h)
    else:
        # node右子树叶节点未能到达h层，证明node右子树为高度为h-level-1的满二叉树
        return (1 << (h - level - 1)) + bs(node.left, level + 1, h)


# 计算以node节点为头结点，最左边节点在整个树中的高度
def most_left_level(node, level):
    while node is not None:
        level += 1
        node = node.left
    return level - 1


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

    def test_num_num(self):
        self.assertEqual(5, num_num(self.make_data()))


if __name__ == '__main__':
    unittest.main()
