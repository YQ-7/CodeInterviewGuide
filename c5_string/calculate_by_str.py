# -*- coding: utf-8 -*-
"""
题目:公式字符串求值
    给定一个字符串str，str表示一个公式，公式里可能有整数、加减乘除符号和左右括号，返回公式的计算结果。
"""

import unittest
from utils.deque import Deque


def get_value(calc_str):
    return value(calc_str, 0)[0]


def value(calc_str, i):
    # 记录待计算的公式
    deque = Deque()
    # 当前操作数
    pre = 0
    # 从左到右遍历calc_str
    while i < len(calc_str) and calc_str[i] != ')':
        if '0' <= calc_str[i] <= '9':
            # 处理数字
            pre = pre * 10 + int(calc_str[i])
            i += 1
        elif calc_str[i] != '(':
            # 计算*、/
            add_num(deque, pre)
            deque.append(calc_str[i])
            pre = 0
            i += 1
        else:
            # 遇到"("进入递归
            pre, i = value(calc_str, i + 1)
            i += 1
    # 计算*、/
    add_num(deque, pre)
    # 计算+、-
    # 返回当前递归处理的计算结果，以及当前遍历位置
    return get_num(deque), i


def add_num(deq, num):
    """
    计算*、/
    """
    if not deq.is_empty():
        top = deq.pop()
        if '+' == top or '-' == top:
            # +、-在get_num中计算
            deq.append(top)
        else:
            cur = int(deq.pop())
            num = cur * num if '*' == top else cur / num
    deq.append(num)


def get_num(deq):
    """
        计算+、-
    """
    res = 0
    add = True
    while not deq.is_empty():
        cur = deq.popleft()
        if '+' == cur:
            add = True
        elif '-' == cur:
            add = False
        else:
            num = int(cur)
            res += num if add else -num
    return res


class MyTestCase(unittest.TestCase):
    def test_get_value(self):
        self.assertEqual(7, get_value("3+1*4"))
        self.assertEqual(-1, get_value("3+(-1*4)"))
        self.assertEqual(-1816, get_value("48*((70-65)-43)+8*1"))


if __name__ == '__main__':
    unittest.main()
