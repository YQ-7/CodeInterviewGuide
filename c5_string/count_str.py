# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符串str，返回str的统计字符串。
    例如，＂aaabbadddffc＂的统计字符串为＂a3b2a1d3f2c1＂
"""
import unittest


def get_count_string(s):
    if s is None or len(s) == 0:
        return ""
    res = s[0]
    num = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res = res + str(num) + s[i]
            num = 1
        else:
            num += 1
    return res + str(num)


def get_char_at(cstr, index):
    """
    返回索引位置的字符
    :param cstr: 统计字符串，以"_"分隔字符和词频数字
    :param index: 索引位置
    :return:
    """
    if cstr is None or len(cstr) == 0:
        return 0
    # start是否即将遇到字符
    stage = True
    # 字符总个数
    sum = 0
    # 当前字符的个数
    num = 0
    cur = 0
    for c in cstr:
        if c == "_":
            stage = not stage
        elif stage:
            # 遇到字符
            sum += num
            if sum > index:
                return cur
            num = 0
            cur = c
        else:
            # 遇到数字
            num = num * 10 + ord(c) - ord('0')

    return cur if sum + num > index else 0


class MyTestCase(unittest.TestCase):
    def test_get_count_string(self):
        self.assertEqual("a3b2a1d3f2c1", get_count_string("aaabbadddffc"))

    def test_get_char_at(self):
        self.assertEqual("b", get_char_at("a_1_b_100", 50))


if __name__ == '__main__':
    unittest.main()
