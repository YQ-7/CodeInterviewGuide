# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符串str，如果str符合日常书写的整数形式，并且属于32位整数的范围，
    返回str所代表的整数值，否则返回0
    str="123" 返回123
    str="-123" 返回-123
    str="0123" 返回0
    str="A123" 返回0
"""

import unittest

# 32位整数最小值
INT_32_MIN = -(1 << 31)


def convert(s):
    if s is None or len(s) == 0:
        return 0
    if not is_valid(s):
        return 0
    # 判断整数正负符号
    posi = False if s[0] == '-' else True
    minq = INT_32_MIN // 10
    minr = INT_32_MIN % 10
    res = 0
    cur = 0
    for i in s:
        if i == '-':
            continue
        cur = ord('0') - ord(i)
        # 判断整数是否溢出
        if res < minq or (res == minq and cur < minr):
            return 0
        res = res * 10 + cur
    # posi为正，但结果==最小整数，则溢出
    if posi and res == INT_32_MIN:
        return 0
    # 恢复正负符号
    return -res if posi else res


def is_valid(s):
    """
        判断字符串s是否符合日常书写的整数形式
    """
    # s只能以"-"和数字开头
    if s[0] != '-' and (ord(s[0]) < ord('0') or ord(s[0]) > ord('9')):
        return False
    # s以"-"开头，但是长度为1，不合法
    if s[0] == '-' and len(s) == 1:
        return False
    # s以"0"开头，但是长度大于1，不合法
    if s[0] == '0' and len(s) > 1:
        return False
    # s[1..N-1]是否包含非数字字符
    for i in range(1, len(s)):
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(123, convert("123"))
        self.assertEqual(-123, convert("-123"))
        self.assertEqual(0, convert("0"))
        self.assertEqual(0, convert("0123"))
        self.assertEqual(0, convert("A12"))
        self.assertEqual(-2147483648, convert("-2147483648"))
        self.assertEqual(0, convert("2147483648"))


if __name__ == '__main__':
    unittest.main()
