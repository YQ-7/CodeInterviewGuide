# -*- coding: utf-8 -*-
"""
题目：
    排队最大快乐值
"""

import unittest


class Employee(object):

    def __init__(self, happy):
        self.happy = happy  # 员工快乐值
        self.subordinates = []  # 员工直接下属


class ReturnData(object):

    def __init__(self, yes_head_max, no_head_max):
        self.yes_head_max = yes_head_max  # 树头结点来的情况下，树的最大收益
        self.no_head_max = no_head_max  # 树头结点不来的情况下，树的最大收益


def get_max_happy(boss):
    all_tree_info = process(boss)
    return max(all_tree_info.yes_head_max, all_tree_info.no_head_max)


def process(x):
    yes_x = x.happy  # x来情况下收益
    no_x = 0  # x不来情况下收益
    if len(x.subordinates) == 0:  # x没有直接下属
        return ReturnData(yes_x, no_x)
    for e in x.subordinates:
        sub_tree_info = process(e)
        yes_x += sub_tree_info.no_head_max
        no_x += max(sub_tree_info.yes_head_max,
                    sub_tree_info.no_head_max)
    return ReturnData(yes_x, no_x)


class MyTestCase(unittest.TestCase):
    def test_get_max_happy(self):
        boss = Employee(5)
        e1 = Employee(4)
        e2 = Employee(2)
        e3 = Employee(1)
        e4 = Employee(3)
        e5 = Employee(6)
        boss.subordinates.append(e1)
        boss.subordinates.append(e2)
        boss.subordinates.append(e3)
        e2.subordinates.append(e4)
        e3.subordinates.append(e5)
        self.assertEqual(14, get_max_happy(boss))


if __name__ == '__main__':
    unittest.main()
