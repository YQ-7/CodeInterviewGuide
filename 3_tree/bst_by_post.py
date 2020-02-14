# -*- coding: utf-8 -*-
"""
题目：
    给定一个整型数组arr，已知其中没有重复值，判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果
"""

import unittest
from utils.linked_list import TreeNode


def is_search_post(arr):
    if arr is None or len(arr) == 0:
        return False
    return is_post(arr, 0, len(arr) - 1)


def is_post(arr, start, end):
    # 只剩1个元素，返回True
    if start == end:
        return True
    less = -1  # 比end小的第一个元素索引
    more = end  # 比end大的第一个元素索引
    for i in range(start, end + 1):
        if arr[end] > arr[i]:
            less = i
        else:
            more = i if more == end else more
    # more == end: end是最大值
    # less == -1 end是或最小值
    if less == -1 or more == end:
        return is_post(arr, start, end - 1)
    if less != more - 1:
        return False
    return is_post(arr, start, less) and is_post(arr, more, end - 1)


def post_arr_to_bst(arr):
    """
        基于不含重复元素的搜索树的后序数组，生成搜索树。
    """
    if arr is None:
        return None
    return post_to_bse(arr, 0, len(arr) - 1)


def post_to_bse(arr, start, end):
    if start > end:
        return None
    head = TreeNode(arr[end])
    less = -1  # 比end小的第一个元素索引
    more = end  # 比end大的第一个元素索引
    for i in range(start, end + 1):
        if arr[end] > arr[i]:
            less = i
        else:
            more = i if more == end else more
    head.left = post_to_bse(arr, start, less)
    head.right = post_to_bse(arr, more, end - 1)
    return head


class MyTestCase(unittest.TestCase):
    def test_is_search_post(self):
        self.assertTrue(is_search_post([2, 1, 3, 6, 5, 7, 4]))

    def test_post_arr_to_bst(self):
        head = post_arr_to_bst([2, 1, 3, 6, 5, 7, 4])
        self.assertEqual(4, head.data)
        self.assertEqual(3, head.left.data)
        self.assertEqual(7, head.right.data)
        self.assertEqual(1, head.left.left.data)
        self.assertEqual(2, head.left.left.right.data)
        self.assertEqual(5, head.right.left.data)
        self.assertEqual(6, head.right.left.right.data)


if __name__ == '__main__':
    unittest.main()
