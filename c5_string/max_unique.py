# -*- coding: utf-8 -*-
"""
题目：找到字符串的最长无重复字符子串
    给定一个字符串str，返回str的最长无重复字符子串的长度
"""
import unittest


def max_unique(s):
    """
        时间复杂度：O(n)
        空间复杂度：O(m)
    """
    if s is None or len(s) == 0:
        return 0
    # 记录字符最近出现的位置
    # key:字符，value:最近一次出现的位置
    s_map = {}
    max_len = 0
    # s[i-1]字符结尾的情况下，最长无重复字符串开始位置的前一个位置
    pre = -1
    for i in range(len(s)):
        # s_map[s[i]] 出现在pre左边，以s[i]结尾最长无重复字符串开始位置为：pre+1
        # s_map[s[i]] 出现在pre右边，以s[i]结尾最长无重复字符串开始位置为：s_map[s[i]]+1
        pre = max(pre, s_map.get(s[i], -1))
        cur = i - pre
        max_len = max(max_len, cur)
        s_map[s[i]] = i
    return max_len


class MyTestCase(unittest.TestCase):
    def test_max_unique(self):
        self.assertEqual(4, max_unique("abcd"))
        self.assertEqual(3, max_unique("aabcb"))


if __name__ == '__main__':
    unittest.main()
