# -*- coding: utf-8 -*-
"""
题目：旋变字符串问题
"""
import unittest


def is_scramble_1(s1, s2):
    """
        暴力递归法
    """
    if (s1 is None and s2 is not None) or (s2 is None and s1 is not None):
        return False
    if s1 == s2:
        return True
    if not same_type_same_number(s1, s2):
        return False
    return process(s1, s2, 0, 0, len(s1))


def same_type_same_number(s1, s2):
    """
        判断s1、s2字符个数是否一致
    """
    if len(s1) != len(s2):
        return False
    m = {}
    for c in s1:
        m[c] = m.get(c, 0) + 1
    for c in s2:
        m[c] = m.get(c, 0) - 1
        if m[c] < 0:
            return False
    return True


def process(s1, s2, l1, l2, size):
    """
    判断s1[l1..l1+size]与s2[l2..l2+size]是否是旋变字符串
    """
    # 基本情况
    if size == 1:
        return s1[l1] == s2[l2]

    # 循环遍历每一种可能情况
    for left_part in range(1, size):
        if (process(s1, s2, l1, l2, left_part)
            and process(s1, s2, l1 + left_part, l2 + left_part, size - left_part)) \
                or (process(s1, s2, l1, l2 + size - left_part, left_part)
                    and process(s1, s2, l1 + left_part, l2, size - left_part)):
            return True
    return False


def is_scramble_2(s1, s2):
    """
        动态规范
    """
    if (s1 is None and s2 is not None) or (s2 is None and s1 is not None):
        return False
    if s1 == s2:
        return True
    if not same_type_same_number(s1, s2):
        return False
    n = len(s1)
    dp = [[[False for i in range(n + 1)] for j in range(n)] for k in range(n)]
    # 初始化dp[*][*][1]
    for l1 in range(n):
        for l2 in range(n):
            dp[l1][l2][1] = s1[l1] == s2[l2]
    # 基于dp[*][*][size-1]计算dp[*][*][size]
    for size in range(2, n + 1):
        for l1 in range(n - size + 1):
            for l2 in range(n - size + 1):
                for left_part in range(1, size):
                    if (dp[l1][l2][left_part] and dp[l1 + left_part][l2 + left_part][size - left_part]) \
                            or (dp[l1][l2 + size - left_part][left_part] and dp[l1 + left_part][l2][size - left_part]):
                        dp[l1][l2][size] = True
                        break
    return dp[0][0][n]


class MyTestCase(unittest.TestCase):
    def test_is_scramble_1(self):
        self.assertTrue(is_scramble_1("dbac", "abcd"))
        self.assertFalse(is_scramble_1("abcd", "cadb"))

    def test_is_scramble_2(self):
        self.assertTrue(is_scramble_2("dbac", "abcd"))
        self.assertFalse(is_scramble_2("abcd", "cadb"))


if __name__ == '__main__':
    unittest.main()
