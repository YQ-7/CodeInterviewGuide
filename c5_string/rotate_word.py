# -*- coding: utf-8 -*-

"""
    题目：
        给定一个字符类型的数组chas，请在单词间做逆序调整。只要做到单词的顺序逆序即可，对空格的位置没有特别要求
"""

import unittest


def rotate_word(chas):
    if chas is None or len(chas) == 0:
        return
    # 将字符串逆序
    reverse(chas, 0, len(chas) - 1)
    # 将字符串中的每个单词分别逆序
    word_l = -1
    word_r = -1
    for i in range(len(chas)):
        if chas[i] != ' ':
            word_l = i if i == 0 or chas[i - 1] == ' ' else word_l
            word_r = i if i == len(chas) - 1 or chas[i + 1] == ' ' else word_r
        if word_l != -1 and word_r != -1:
            reverse(chas, word_l, word_r)
            word_l = -1
            word_r = -1


def reverse(chas, start, end):
    while start < end:
        tmp = chas[start]
        chas[start] = chas[end]
        chas[end] = tmp
        start += 1
        end -= 1


class MyTestCase(unittest.TestCase):
    def test_rotate_word(self):
        chas = list("dog loves pig")
        rotate_word(chas)
        self.assertEqual("pig loves dog", "".join(chas))


if __name__ == '__main__':
    unittest.main()
