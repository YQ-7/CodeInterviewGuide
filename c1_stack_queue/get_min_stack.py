# -*- coding: utf-8 -*-

"""
    题目：实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
    要求：
        1.pop、push、getMin操作的时间复杂度都是O（1）。
        2.设计的栈类型可以使用现成的栈结构。
"""

import unittest
from utils.stack import Stack


class GetMinStack1(object):
    """
    方案一
        push:stack_min动态添加最小值，item > stack_min栈顶元素时，stack_min保存不变
        pop:stack_data pop的元素 == stack_min栈顶元素时，stack_min栈顶元素出栈
        stack_min元素个数 <= stack_data元素个数
    """

    def __init__(self):
        # stack_data:数据栈保存所有数据
        self.stack_data = Stack()
        # stack_min:保存每一步最小值，栈顶元素为当前数据的最小值
        self.stack_min = Stack()

    def push(self, item):
        # 数据压入stack_data栈
        self.stack_data.push(item)
        # stack_min为空，当前元素即为最小值，压入stack_min栈
        if self.stack_min.is_empty():
            self.stack_min.push(item)
        # item <= 当前最小值，，压入stack_min栈
        elif item <= self.get_min():
            self.stack_min.push(item)

    def pop(self):
        item = self.stack_data.pop()
        # stack_data栈顶元素 <= stack_min栈顶元素，则stack_min栈顶元素出栈
        if item <= self.get_min():
            self.stack_min.pop()
        return item

    def get_min(self):
        # stack_min栈顶元素为当前栈的最小值
        return self.stack_min.peek()


class GetMinStack2(object):
    """
    方案二
        push:stack_min动态添加最小值，item > stack_min栈顶元素时，重复将stack_min栈顶元素加入栈
        pop:stack_data、stack_min同时出栈，不用作判断
        stack_min与stack_data元素个数保存一致
    """

    def __init__(self):
        # stack_data:数据栈保存所有数据
        self.stack_data = Stack()
        # stack_min:保存每一步最小值，栈顶元素为当前数据的最小值
        self.stack_min = Stack()

    def push(self, item):
        # 数据压入stack_data栈
        self.stack_data.push(item)
        # stack_min为空，当前元素即为最小值，压入stack_min栈
        if self.stack_min.is_empty():
            self.stack_min.push(item)
        # item <= 当前最小值，，压入stack_min栈
        elif item <= self.get_min():
            self.stack_min.push(item)
        else:
            # item > stack_min栈顶元素时重复将当前最小值入栈
            self.stack_min.push(self.get_min())

    def pop(self):
        item = self.stack_data.pop()
        self.stack_min.pop()
        return item

    def get_min(self):
        # stack_min栈顶元素为当前栈的最小值
        return self.stack_min.peek()


class MyTestCase(unittest.TestCase):

    def test_get_min1(self):
        min_stack = GetMinStack1()
        min_stack.push(3)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(4)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(5)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(1)
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.push(2)
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.push(1)
        self.assertEqual(min_stack.get_min(), 1)

        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.pop()
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 3)

    def test_get_min2(self):
        min_stack = GetMinStack2()
        min_stack.push(3)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(4)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(5)
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.push(1)
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.push(2)
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.push(1)
        self.assertEqual(min_stack.get_min(), 1)

        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 3)
        min_stack.pop()
        min_stack.pop()
        self.assertEqual(min_stack.get_min(), 3)


if __name__ == '__main__':
    unittest.main()
