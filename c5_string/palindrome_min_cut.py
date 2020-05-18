# -*- coding: utf-8 -*-
"""
题目：回文最少分割数
    给定一个字符串str，返回把str全部切成回文子串的最小分割数
"""
import unittest


def palindrome_min_cut(s):
    """
        定义动态规划数组dp[i] :
            s[i..len-1]至少需要切割几次，才能把s[i..len-1]全部切割成回文子串
    """
    dp = [None] * (len(s) + 1)
    dp[-1] = -1
    # p[i][j] == True: s[i..j]是回文
    p = [[False for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                p[i][j] = True
                # dp[i]=min{dp[j+1]+1（i≤j＜len，且str[i..j]必须是回文串）}
                dp[i] = dp[j + 1] + 1 if dp[i] is None else \
                    min(dp[i], dp[j + 1] + 1)
    return dp[0]


class MyTestCase(unittest.TestCase):
    def test_palindrome_min_cut(self):
        self.assertEqual(0, palindrome_min_cut("CAC"))
        self.assertEqual(2, palindrome_min_cut("ACDCDCDAD"))


if __name__ == '__main__':
    unittest.main()
