# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符类型数组chas[]，判断chas中是否所有的字符都只出现过一次
"""

import unittest
from utils.heap_sort import heap_sort


def is_unique_1(chas):
    """
        方法一：依次遍历字符串，用哈希表存储已遍历过的字符，若哈希表中已存在当前遍历的字符则证明字符不唯一
        时间复杂度O(N)
        空间复杂度O(N)
    """
    if chas is None:
        return True
    c_set = set()
    for c in chas:
        if c in c_set:
            return False
        c_set.add(c)
    return True


def is_unique_2(chas):
    """
        方法二：先将字符串排序，再遍历字符串，判断相邻元素是否有相等的
        排序选择非递归版的堆排序
        时间复杂度O(NlogN)
        空间复杂度O(1)
    """
    if chas is None:
        return False
    # 堆排序
    arr = list(chas)
    heap_sort(arr)
    # 遍历排序后的字符，若相邻字符有相等的，则字符不唯一
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_is_unique_1(self):
        self.assertTrue(is_unique_1("abc"))
        self.assertFalse(is_unique_1("121"))

    def test_is_unique_2(self):
        self.assertTrue(is_unique_2("abcfed"))
        self.assertFalse(is_unique_2("12146134"))


if __name__ == '__main__':
    unittest.main()
