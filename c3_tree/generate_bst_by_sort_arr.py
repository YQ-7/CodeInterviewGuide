# -*- coding: utf-8 -*-
"""
题目：
    给定一个有序数组sortArr，已知其中没有重复值，用这个有序数组生成一棵平衡搜索二叉树，
    并且该搜索二叉树中序遍历的结果与sortArr一致。
解答:
    用有序数组中最中间的数生成搜索二叉树的头节点，然后用这个数左边的数生成左子树，用右边的数生成右子树即可。
"""

import unittest
from utils.linked_list import TreeNode


def generate_tree(sort_arr):
    if sort_arr is None:
        return None
    return generate(sort_arr, 0, len(sort_arr) - 1)


def generate(sort_arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    head = TreeNode(sort_arr[mid])
    head.left = generate(sort_arr, start, mid - 1)
    head.right = generate(sort_arr, mid + 1, end)
    return head


class MyTestCase(unittest.TestCase):
    def test_something(self):
        head = generate_tree([1, 2, 3, 4, 5])
        self.assertEqual(3, head.data)
        self.assertEqual(1, head.left.data)
        self.assertEqual(2, head.left.right.data)
        self.assertEqual(4, head.right.data)
        self.assertEqual(5, head.right.right.data)


if __name__ == '__main__':
    unittest.main()
