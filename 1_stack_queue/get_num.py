# -*- coding: utf-8 -*-

"""
题目：
    给定数组arr和整数num，共返回有多少个子数组满足如下情况：
    max（arr[i..j]）表示子数组arr[i..j]中的最大值，min（arr[i..j]）表示子数组arr[i..j]中的最小值。
"""
import unittest
from utils.deque import Deque


def get_num(arr, num):
    if arr is None or len(arr) == 0 or num < 0:
        return 0
    q_min = Deque()
    q_max = Deque()
    j = 0
    res = 0
    for i in range(len(arr)):
        while j < len(arr):
            j_val = arr[j]
            if q_min.is_empty() or q_min.peek_left() != j:
                while not q_min.is_empty() and arr[q_min.peek_left()] >= j_val:
                    q_min.popleft()
                q_min.appendleft(j)
                while not q_max.is_empty() and arr[q_max.peek_left()] <= j_val:
                    q_max.popleft()
                q_max.appendleft(j)
            if arr[q_max.peek()] - arr[q_min.peek()] > num:
                break
            j += 1
        res += j - i
        if q_min.peek() == i:
            q_min.pop()
        if q_max.peek() == i:
            q_max.pop()
    return res


class MyTestCase(unittest.TestCase):
    def test_get_num(self):
        arr = [3, 1, 2, 1, 6]
        self.assertEqual(11, get_num(arr, 3))


if __name__ == '__main__':
    unittest.main()
