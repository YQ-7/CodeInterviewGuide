# -*- coding: utf-8 -*-
"""
题目：
    已知一棵二叉树所有的节点值都不同，给定这棵树正确的先序和中序数组，
    不要重建整棵树，而是通过这两个数组直接生成正确的后序数组
"""

import unittest


def get_pos_arr(pre_arr, in_arr):
    if pre_arr is None or in_arr is None:
        return None
    length = len(pre_arr)
    pos_arr = [None] * length
    in_map = {}
    for i in range(length):
        in_map[in_arr[i]] = i
    set_pos(pre_arr, 0, length - 1,
            in_arr, 0, length - 1,
            pos_arr, length - 1,
            in_map)
    return pos_arr


def set_pos(pre_arr, pi, pj,
            in_arr, ni, nj,
            pos_arr, si,
            in_map):
    if pi > pj:
        return si
    # 从右往左填充后续数组
    pos_arr[si] = pre_arr[pi]
    si -= 1
    i = in_map.get(pre_arr[pi])
    # 先基于右子树设置后续数组
    si = set_pos(pre_arr, pj - nj + i + 1, pj,
                 in_arr, i + 1, nj,
                 pos_arr, si,
                 in_map)
    # 在基于左子树设置后续数组
    return set_pos(pre_arr, pi + 1, pi + i - ni,
                   in_arr, ni, i - 1,
                   pos_arr, si,
                   in_map)


class MyTestCase(unittest.TestCase):
    def test_get_pos_arr(self):
        pre_arr = [1, 2, 4, 5, 3, 6, 7]
        in_arr = [4, 2, 5, 1, 6, 3, 7]
        pos_arr = get_pos_arr(pre_arr, in_arr)
        self.assertEqual(4, pos_arr[0])
        self.assertEqual(5, pos_arr[1])
        self.assertEqual(2, pos_arr[2])
        self.assertEqual(6, pos_arr[3])
        self.assertEqual(7, pos_arr[4])
        self.assertEqual(3, pos_arr[5])
        self.assertEqual(1, pos_arr[6])


if __name__ == '__main__':
    unittest.main()
