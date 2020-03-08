# -*- coding: utf-8 -*-
"""
题目：
    子数组的最大累加和问题
"""
import unittest


def find_maximum_subarray(arr):
    """
        时间复杂度：Θ(n)
    """
    max_sum = 0
    max_left = None
    max_right = None
    cur_sum = 0
    cur_left = 0
    for i in range(len(arr)):
        if cur_sum == 0:
            cur_left = i
        cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_left = cur_left
            max_right = i
        if cur_sum < 0:
            cur_sum = 0
    return max_left, max_right, max_sum


class MyTestCase(unittest.TestCase):
    def test_find_maximum_subarray_1(self):
        arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        left, right, max_sum = find_maximum_subarray(arr)
        self.assertEqual(7, left)
        self.assertEqual(10, right)
        self.assertEqual(43, max_sum)


if __name__ == '__main__':
    unittest.main()
