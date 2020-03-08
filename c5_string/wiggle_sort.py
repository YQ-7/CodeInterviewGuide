# -*- coding: utf-8 -*-

"""
    题目：
        给定一个数组arr，请将数组调整为依次相邻的数字总是先＜=、再＞=的关系，并交替下去
"""
import unittest
from c5_string.shuffle import shuffle
from utils.heap_sort import heap_sort


def wiggle_sort(arr):
    """
        时间复杂度为O(NlgN)
        额外空间复杂度为O(1)
    """
    if arr is None or len(arr) == 0:
        return
    # 排序
    heap_sort(arr)
    # 进行完美洗牌
    if len(arr) & 1 == 1:
        shuffle(arr, 1, len(arr) - 1)
    else:
        shuffle(arr, 0, len(arr) - 1)
        for i in range(0, len(arr), 2):
            tmp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = tmp


class MyTestCase(unittest.TestCase):
    def test_wiggle_sort(self):
        arr = [1, 2, 3, 4, 5, 6]
        wiggle_sort(arr)
        self.assertEqual(1, arr[0])
        self.assertEqual(4, arr[1])
        self.assertEqual(2, arr[2])
        self.assertEqual(5, arr[3])
        self.assertEqual(3, arr[4])
        self.assertEqual(6, arr[5])


if __name__ == '__main__':
    unittest.main()
