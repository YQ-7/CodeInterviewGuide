# -*- coding: utf-8 -*-

"""
题目：
    给定两个字符串str1和str2，如果str1和str2中出现的字符种类一样且每种字符出现的次数也一样，那么str1与str2互为变形词。
    请实现函数判断两个字符串是否互为变形词。
"""
import unittest


def is_deformation(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        return False
    # 用哈希表统计字符词频，字符少的情况，可以用数组统计
    str_map = {}
    # 遍历s1，并记录字符出现的次数
    for s in s1:
        str_map[s] = str_map.get(s, 0) + 1
    # 遍历s2，将统计表中词频减下来
    for s in s2:
        str_map[s] = str_map.get(s, 0) - 1
        # 词频<0,则不是互为变形词
        if str_map[s] < 0:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_is_deformation(self):
        self.assertTrue(is_deformation("1213", "2311"))
        self.assertFalse(is_deformation("123", "2331"))


if __name__ == '__main__':
    unittest.main()
