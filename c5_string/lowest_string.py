# -*- coding: utf-8 -*-
"""
题目：拼接所有字符串产生字典顺序最小的大写字符串
    给定一个字符串类型的数组strs，请找到一种拼接顺序，使得将所有的字符串拼接起来组成的
    大写字符串是所有可能性中字典顺序最小的，并返回这个大写字符串。
"""
import unittest
from utils.heap_sort import heap_sort


def str_compare(a, b):
    return a + b > b + a


def lowest_string(strs):
    # 先对数组按照s1+s2 > s2+s1规则排序
    heap_sort(strs, compare=str_compare)
    # 将排序好的字符串连接起来
    return "".join(strs)


class MyTestCase(unittest.TestCase):
    def test_lowest_string(self):
        self.assertEqual("abcde", lowest_string(["abc", "de"]))
        self.assertEqual("bab", lowest_string(["b", "ba"]))


if __name__ == '__main__':
    unittest.main()
