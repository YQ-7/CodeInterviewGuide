# -*- coding: utf-8 -*-

"""
题目：
    给定一个整型矩阵map，其中的值只有0和1两种，求其中全是1的所有矩形区域中，最大的矩形区域为1的数量。
解答：
    1.矩阵的行数为N，以每一行做切割，统计以当前行作为底的情况下，每个位置往上的1的数量。使用高度数组height来表示。
    2.对于每一次切割，都利用更新后的height数组来求出以当前行为底的情况下，最大的矩形是什么。那么这么多次切割中，最大的那个矩形就是我们要的答案。
        实质是在一个大的直方图中求最大矩形的面积。
"""

import unittest
from utils.stack import Stack


def max_rec_size(rec_map):
    if rec_map is None or len(rec_map) == 0 or len(rec_map[0]) == 0:
        return 0
    max_area = 0
    height = [0] * len(rec_map[0])
    # 对每一行做分割
    for line in rec_map:
        for i, val in enumerate(line):
            height[i] = 0 if val == 0 else height[i] + val
        # 计算以当前行为地的情况下，矩阵的最大区域数量
        temp_max_area = max_rec_from_bottom(height)
        max_area = max_area if max_area > temp_max_area else temp_max_area
    return max_area


def max_rec_from_bottom(height):
    if height is None or len(height) == 0:
        return 0
    max_area = 0
    stack = Stack()
    for i, val in enumerate(height):
        while not stack.is_empty() and val <= height[stack.peek()]:
            j = stack.pop()
            k = -1 if stack.is_empty() else stack.peek()
            curr_area = (i - k - 1) * height[j]
            max_area = curr_area if curr_area > max_area else max_area
        stack.push(i)

    while not stack.is_empty():
        j = stack.pop()
        k = -1 if stack.is_empty() else stack.peek()
        curr_area = (len(height) - k - 1) * height[j]
        max_area = curr_area if curr_area > max_area else max_area

    return max_area


class MyTestCase(unittest.TestCase):
    def test_max_rec_size(self):
        rec_map = []
        rec_map.append([1, 0, 1, 1])
        rec_map.append([1, 1, 1, 1])
        rec_map.append([1, 1, 1, 0])
        self.assertEqual(6, max_rec_size(rec_map))
        rec_map.append([1, 1, 1, 0])
        self.assertEqual(9, max_rec_size(rec_map))


if __name__ == '__main__':
    unittest.main()
