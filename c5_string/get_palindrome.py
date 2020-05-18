# -*- coding: utf-8 -*-
"""
题目
    添加最少字符使字符串整体都是回文字符串
    给定一个字符串str，如果可以在str的任意位置添加字符，请返回在添加字符最少的情况下，让str整体都是回文字符串的一种结果。
"""
import unittest


def get_palindrome_1(s):
    if s is None or len(s) < 2:
        return s
    # 计算字符串及子串变成回文需要添加的字符个数
    dp = get_dp(s)
    # 生成回文串
    res = [None] * (len(s) + dp[0][len(s) - 1])
    i = 0
    j = len(s) - 1
    res_l = 0
    res_r = len(res) - 1
    while i <= j:
        if s[i] == s[j]:
            res[res_l] = s[i]
            res_l += 1
            i += 1
            res[res_r] = s[j]
            res_r -= 1
            j -= 1
        elif dp[i][j - 1] < dp[i + 1][j]:
            res[res_l] = s[j]
            res_l += 1
            res[res_r] = s[j]
            res_r -= 1
            j -= 1
        else:
            res[res_l] = s[i]
            res_l += 1
            res[res_r] = s[i]
            res_r -= 1
            i += 1
    return "".join(res)


def get_dp(chas):
    """
        利用动态规划计数出chas所有子串转化成回文串所需的最小长度
        时间复杂度：O(n^2)
    """
    dp = [[0] * len(chas) for v in range(len(chas))]
    for j in range(1, len(chas)):
        dp[j - 1][j] = 0 if chas[j - 1] == chas[j] else 1
        for i in range(j - 2, -1, -1):
            if chas[i] == chas[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp


def get_palindrome_2(s, slps):
    """
    已知最大回文子串的情况下，求解s添加最少的字符串，使之变成回文
    时间复杂度：O(N)
    :param s:
    :param slps: s的最大回文子串
    """
    if s is None or len(s) == 0:
        return ""
    # 整体回文串长度=2 * len(s)-len(slps)
    res = [None] * (2 * len(s) - len(slps))
    s_left = 0
    s_right = len(s) - 1
    slps_left = 0
    slps_right = len(slps) - 1
    res_left = 0
    res_right = len(res) - 1
    # 以”剥洋葱“的方法，从外向内进行回文转换
    while slps_left <= slps_right:
        tmp_left = s_left
        tmp_right = s_right
        # 先定位slps对称字符在s中的位置
        while s[s_left] != slps[slps_left]:
            s_left += 1
        while s[s_right] != slps[slps_right]:
            s_right -= 1
        # s[tmp_left..s_left] =
        # s[s_right..tmp_right]
        set_part(res, res_left, res_right, s, tmp_left, s_left, s_right, tmp_right)
        res_left += s_left - tmp_left + tmp_right - s_right
        res_right -= s_left - tmp_left + tmp_right - s_right
        res[res_left] = s[s_left]
        res_left += 1
        s_left += 1
        res[res_right] = s[s_right]
        res_right -= 1
        s_right -= 1
        slps_left += 1
        slps_right -= 1
    return "".join(res)


def set_part(res, res_l, res_r, s, ls, le, rs, re):
    for i in range(ls, le):
        res[res_l] = s[i]
        res_l += 1
        res[res_r] = s[i]
        res_r -= 1
    for i in range(re, rs, -1):
        res[res_l] = s[i]
        res_l += 1
        res[res_r] = s[i]
        res_r -= 1


class MyTestCase(unittest.TestCase):
    def test_get_palindrome_1(self):
        self.assertEqual("ABA", get_palindrome_1("AB"))
        self.assertEqual("A", get_palindrome_1("A"))
        self.assertEqual("AC1B2B1CA", get_palindrome_1("A1B21C"))

    def test_get_palindrome_2(self):
        self.assertEqual("AF1BCED22DECB1FA", get_palindrome_2("A1BC22DE1F", "1221"))


if __name__ == '__main__':
    unittest.main()
