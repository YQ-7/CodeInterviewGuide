# -*- coding: utf-8 -*-
"""
题目:括号字符串的有效性
    给定一个字符串str，判断是不是整体有效的括号字符串
"""
import unittest


def is_valid_brace(s):
    brace_num = 0
    for c in s:
        # s中包含非'('')'字符返回False
        if '(' != c and ')' != c:
            return False
        if ')' == c:
            brace_num -= 1
            # 遇到')'时，若')'个数>'('个数，返回False
            if brace_num < 0:
                return False
        if '(' == c:
            brace_num += 1
    # '('与')'个数相等，返回True
    return brace_num == 0


class MyTestCase(unittest.TestCase):
    def test_is_valid_brace(self):

        self.assertTrue(is_valid_brace("()"))
        self.assertTrue(is_valid_brace("()()"))
        self.assertTrue(is_valid_brace("(())"))
        self.assertFalse(is_valid_brace("())"))
        self.assertFalse(is_valid_brace("((a))"))


if __name__ == '__main__':
    unittest.main()
