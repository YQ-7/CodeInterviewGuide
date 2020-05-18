# -*- coding: utf-8 -*-
"""
题目：
    给定一个数组arr，该数组无序，但每个值均为正数，再给定一个正数k。
    求arr的所有子数组中所有元素相加和为k的最长子数组长度。
解答：
    用两个位置来标记子数组的左右两头，记为left和right
    1.开始时变量left=0，right=0，代表子数组arr[left..right]
    2.变量sum始终表示子数组arr[left..right]的和。开始时sum=arr[0]，即arr[0..0]的和
    3.变量len一直记录累加和为k的所有子数组中最大子数组的长度。开始时，len=0
    4.根据sum与k的比较结果决定是left移动还是right移动
"""

import unittest


def get_max_length(arr, k):
    if arr is None or len(arr) == 0 or k <= 0:
        return 0
    left = 0
    right = 0
    add_sum = arr[0]
    max_len = 0
    while right < len(arr):
        if add_sum == k:
            # 累加和=k，更新max_len
            max_len = max(max_len, right - left + 1)
            # 移动left,更新add_sum
            add_sum -= arr[left]
            left += 1
        elif add_sum < k:
            # 累加和 < k，right向前移动，更新累加和
            right += 1
            if right == len(arr):
                break
            add_sum += arr[right]
        else:
            # 累加和 > k，left向前移动，更新累加和
            add_sum -= arr[left]
            left -= 1
    return max_len


class MyTestCase(unittest.TestCase):
    def test_get_max_length(self):
        arr = [1, 2, 1, 1, 1]
        self.assertEqual(3, get_max_length(arr, 3))


if __name__ == '__main__':
    unittest.main()
