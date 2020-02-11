# -*- coding: utf-8 -*-
"""
题目：
    给定两个字符串str和match，长度分别为N和M。
    实现一个算法，如果字符串str中含有子串match，则返回match在str中的开始位置，不含有则返回-1。
"""

import unittest


def get_index_of(s, m):
    """
        str中匹配的位置是不退回的，match则一直向右滑动，如果在str中的某个位置完全匹配出match，整个过程停止。
        否则match滑到str的最右侧过程也停止，所以滑动的长度最大为N，时间复杂度为O（N）。
    """
    if s is None or m is None or len(m) < 1 or len(s) < len(m):
        return -1
    si = 0
    mi = 0
    next_arr = get_next_array(m)
    while si < len(s) and mi < len(m):
        if s[si] == m[mi]:
            si += 1
            mi += 1
        elif next_arr[mi] == -1:
            si += 1
        else:
            mi = next_arr[mi]
    return si - mi if mi == len(m) else -1


def get_next_array(ms):
    if len(ms) == 1:
        return [-1]
    next_arr = [None] * len(ms)
    next_arr[0] = -1
    next_arr[1] = 0
    pos = 2
    cn = 0
    while pos < len(next_arr):
        if ms[pos - 1] == ms[cn]:
            cn += 1
            next_arr[pos] = cn
            pos += 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[pos] = 0
            pos += 1
    return next_arr


class MyTestCase(unittest.TestCase):
    def test_get_index_of(self):
        self.assertEqual(2, get_index_of("acbc", "bc"))
        self.assertEqual(-1, get_index_of("acbc", "bcc"))


if __name__ == '__main__':
    unittest.main()
