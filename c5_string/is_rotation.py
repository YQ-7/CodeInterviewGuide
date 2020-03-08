# -*- coding: utf-8 -*-

"""
题目：
    把字符串str前面任意的部分挪到后面形成的字符串叫作str的旋转词
    给定两个字符串a和b，请判断a和b是否互为旋转词
"""

import unittest
from c9_other import kmp


def is_rotation(a, b):
    if a is None or b is None or len(a) != len(b):
        return False
    b2 = b + b
    # b2中包含a,则a和b互为旋转词
    return kmp.get_index_of(b2, a) != -1


class MyTestCase(unittest.TestCase):
    def test_is_rotation(self):
        self.assertTrue(is_rotation("cdab", "abcd"))
        self.assertFalse(is_rotation("1ab2", "ab12"))


if __name__ == '__main__':
    unittest.main()
