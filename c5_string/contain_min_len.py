# -*- coding: utf-8 -*-
"""
题目:最小包含子串长度
    给定字符串str1和str2，求str1的子串中含有str2所有字符的最小子串长度
"""

import unittest


def contain_min_len(s1, s2):
    """
        时间复杂度O(N)
    """
    if s1 is None or s2 is None or len(s1) < len(s2):
        return 0
    # 记录待匹配每个字符的个数
    tmp_map = {}
    for c in s2:
        tmp_map[c] = tmp_map.get(c, 0) + 1
    left = 0
    # 记录待匹配字符总个数
    match = len(s2)
    min_len = None
    # 先通过right向右扩，让所有的字符被“有效”地还完
    for right in range(len(s1)):
        tmp_map[s1[right]] = tmp_map.get(s1[right], 0) - 1
        if tmp_map[s1[right]] >= 0:
            match -= 1
        # 都还完时，s[left..right]是符合要求的，但还要经过left向右缩的过程来看被框住的子串能不能变得更短。
        if match == 0:
            while tmp_map[s1[left]] < 0:
                tmp_map[s1[left]] += 1
                left += 1
            min_len = (right - left + 1) if min_len is None else \
                min(min_len, right - left + 1)
            match += 1
            tmp_map[s1[left]] += 1
            left += 1
    return 0 if min_len is None else min_len


class MyTestCase(unittest.TestCase):
    def test_contain_min_len(self):
        self.assertEqual(3, contain_min_len("abcde", "ac"))
        self.assertEqual(0, contain_min_len("12345", "344"))


if __name__ == '__main__':
    unittest.main()
