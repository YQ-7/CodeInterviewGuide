# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符串数组strs，再给定两个字符串str1和str2，返回在strs中str1与str2的最小距离，如果str1或str2为null，或不在strs中，返回-1。
"""

import unittest


def min_distance(s, s1, s2):
    if s is None or s1 is None or s2 is None:
        return -1
    if s1 == s2:
        return 0
    last_1 = -1
    last_2 = -1
    min_dis = -1
    for i in range(len(s)):
        if start_with(s, i, s1):
            dis = min_dis if last_2 == -1 else i - last_2
            min_dis = min(min_dis, dis) if min_dis != -1 else dis
            last_1 = i
        elif start_with(s, i, s2):
            dis = min_dis if last_1 == -1 else i - last_1
            min_dis = min(min_dis, dis) if min_dis != -1 else dis
            last_2 = i
    return min_dis


def start_with(s, start, s2):
    if len(s) - start < len(s2):
        return False
    for i in range(len(s2)):
        if s2[i] != s[start]:
            return False
        start += 1
    return True


class MyTestCase(unittest.TestCase):
    def test_min_distance(self):
        self.assertEqual(2, min_distance("1333231", "1", "2"))
        self.assertEqual(2, min_distance("1333231", "1", "2"))
        self.assertEqual(-1, min_distance("1333231", "1", "9"))
        self.assertEqual(1, min_distance("1333231", "13", "33"))
        self.assertEqual(3, min_distance("132332313555533", "13", "33"))


if __name__ == '__main__':
    unittest.main()
