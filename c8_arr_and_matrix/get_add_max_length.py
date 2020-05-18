# -*- coding: utf-8 -*-
"""
题目：
    给定一个无序数组arr，其中元素可正、可负、可0。给定一个整数k，求arr所有的子数组中累加和为k的最长子数组长度
解答：
    s（i）代表子数组arr[0..i]所有元素的累加和。那么子数组arr[j..i]（0≤j≤i＜arr.length）的累加和为s（i）-s（j-1）
    构建一个map来存放s(i), {key: s(i), value: i}
"""

import unittest


def get_add_max_length(arr, k):
    if arr is None or len(arr) == 0:
        return 0
    sum_map = {0: -1}   # 避免漏掉从0开始的子数组
    max_len = 0
    add_sum = 0
    for i in range(len(arr)):
        add_sum += arr[i]
        if sum_map.get(add_sum - k) is not None:
            max_len = max(max_len, i - sum_map.get(add_sum - k))
        if sum_map.get(add_sum) is None:
            sum_map[add_sum] = i
    return max_len


def get_neg_pos_max_length(arr):
    """
    题目：
        给定一个无序数组arr，其中元素可正、可负、可0。求arr所有的子数组中正数与负数个数相等的最长子数组长度
    """
    if arr is None or len(arr) == 0:
        return 0
    sum_map = {0: -1}   # 避免漏掉从0开始的子数组
    max_len = 0
    add_sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            add_sum += 1
        elif arr[i] < 0:
            add_sum -= 1
        if sum_map.get(add_sum) is not None:
            max_len = max(max_len, i - sum_map.get(add_sum))
        if sum_map.get(add_sum) is None:
            sum_map[add_sum] = i
    return max_len


def get_zero_max_length(arr):
    """
    题目：
        给定一个无序数组arr，其中元素只是1或0。求arr所有的子数组中0和1个数相等的最长子数组长度
    """
    if arr is None or len(arr) == 0:
        return 0
    sum_map = {0: -1}   # 避免漏掉从0开始的子数组
    max_len = 0
    add_sum = 0
    for i in range(len(arr)):
        add_sum += 1 if arr[i] == 1 else -1
        if sum_map.get(add_sum) is not None:
            max_len = max(max_len, i - sum_map.get(add_sum))
        if sum_map.get(add_sum) is None:
            sum_map[add_sum] = i
    return max_len


class MyTestCase(unittest.TestCase):
    def test_get_add_max_length(self):
        arr = [1, 2, 3, 3]
        self.assertEqual(3, get_add_max_length(arr, 6))

    def test_get_neg_pos_max_length(self):
        arr = [1, 0, -2, 3, 3]
        self.assertEqual(3, get_neg_pos_max_length(arr))

    def test_get_zero_max_length(self):
        arr = [1, 1, 0, 1, 1]
        self.assertEqual(2, get_zero_max_length(arr))


if __name__ == '__main__':
    unittest.main()
