# -*- coding: utf-8 -*-
"""
题目：找到指定的新类型字符串
    新类型字符的定义如下：
        1.新类型字符是长度为1或者2的字符串。
        2.表现形式可以仅是小写字母，例如，＂e＂；
          也可以是大写字母+小写字母，例如，＂Ab＂；
          还可以是大写字母+大写字母，例如，＂DC＂。
    现在给定一个字符串str，str一定是若干新类型字符正确组合的结果。
    再给定一个整数k，代表str中的位置。请返回被k位置指定的新类型字符。
"""
import unittest


def point_new_char(s, k):
    if s is None or len(s) == 0 or k < 0 or k >= len(s):
        return 0
    # 从k-1向左遍历，统计连续出现大写字母的个数
    u_num = 0
    for i in range(k - 1, 0, -1):
        if s[i].islower():
            break
        u_num += 1
    # u_num为奇数，s[k-1, k]是第k个新类型字符串
    if u_num & 1 == 1:
        return s[k - 1: k + 1]

    # u_num为偶数且s[k]是大写字母，s[k, k+1]是第k个新类型字符串
    if s[k].isupper():
        return s[k: k + 2]
    # u_num为偶数且s[k]是小写字母，s[k]是第k个新类型字符串
    return s[k]


class MyTestCase(unittest.TestCase):
    def test_point_new_char(self):
        self.assertEqual("Ec", point_new_char("aaABCDEcBCg", 7))
        self.assertEqual("CD", point_new_char("aaABCDEcBCg", 4))
        self.assertEqual("g", point_new_char("aaABCDEcBCg", 10))


if __name__ == '__main__':
    unittest.main()
