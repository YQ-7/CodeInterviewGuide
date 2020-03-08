# -*- coding: utf-8 -*-

import unittest


def replace(chas):
    """
        题目：
            chas右半区全是空字符，左半区不含有空字符。现在想将左半区中所有的空格字符替换成＂%20＂，假设chas右半区足够大
    """
    if chas is None or len(chas) == 0:
        return
    # 数组左半区空格的个数
    num = 0
    # 数组左半区长度
    length = 0
    for c in chas:
        if c is None:
            break
        if c == ' ':
            num += 1
        length += 1

    # 替换后，左半区最后一个字符的索引
    j = length + num * 2 -1
    # 从左半区最后一个字符位置开始替换
    for i in range(length - 1, -1, -1):
        if chas[i] != ' ':
            chas[j] = chas[i]
            j -= 1
        else:
            chas[j] = '0'
            j -= 1
            chas[j] = '2'
            j -= 1
            chas[j] = '%'
            j -= 1


def modify(chas):
    """
        题目：
            chas[]中只含有数字字符和“*”字符。现在想把所有的“*”字符挪到chas的左边，数字字符挪到chas的右边
    """
    if chas is None or len(chas) == 0:
        return
    j = len(chas) - 1
    # 逆序将非"*"字符复制到数组尾部
    for i in range(len(chas) - 1, -1, -1):
        if chas[i] != '*':
            chas[j] = chas[i]
            j -= 1
    # 字符头部填充"*"
    for i in range(j + 1):
        chas[i] = '*'


class MyTestCase(unittest.TestCase):
    def test_replace(self):
        chas = ["a", " ", "b", " ", " ", "c"] + [None] * 10
        replace(chas)
        self.assertEqual("a%20b%20%20c", ''.join(chas[0:12]))

    def test_modify(self):
        chas = ["1", "2", "*", "*", "3", "4", "5"]
        modify(chas)
        self.assertEqual("**12345", ''.join(chas))


if __name__ == '__main__':
    unittest.main()
