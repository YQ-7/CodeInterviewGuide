# -*- coding: utf-8 -*-
"""
题目:括号字符串的最长有效性长度
    给定一个字符串str，返回最长的有效括号子串的长度
"""
import unittest


def max_valid_brace_length(s):
    """
        利用动态规划求解
        时间复杂度：O(N)
        空间复杂度：O(N)
    """
    if s is None or len(s) == 0:
        return 0
    # dp[i]: s[0..i]中以s[i]结尾的字符串的最大有效括号长度
    dp = [0] * len(s)
    res = 0
    for i in range(1, len(s)):
        # s[i] == '('  dp[i]=0,循环里不用处理
        if s[i] == ')':
            # 获取dp[i - 1]有效括号的开始字符位置
            pre = i - dp[i - 1] - 1
            if pre >= 0 and s[pre] == '(':
                # s[pre..i]是符合要求的，且需要加上dp[pre-1]
                dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre > 0 else 0)
        res = max(res, dp[i])
    return res


class MyTestCase(unittest.TestCase):
    def test_max_valid_brace_length(self):
        self.assertEqual(0, max_valid_brace_length(")("))
        self.assertEqual(2, max_valid_brace_length("())"))
        self.assertEqual(8, max_valid_brace_length("((()()))"))
        self.assertEqual(4, max_valid_brace_length("()(()()("))


if __name__ == '__main__':
    unittest.main()
