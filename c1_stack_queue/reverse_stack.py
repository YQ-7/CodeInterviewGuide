# -*- coding: utf-8 -*-

"""
题目：
    仅用递归函数和栈操作逆序一个栈
解答：
    通过2个递归函数实现
    递归函数1：获取并移除栈底元素
    递归函数2：将函数1中获取的栈底元素压入栈中
"""

import unittest
from utils.stack import Stack


class ReverseStack(object):

    # 获取并移除栈底元素
    def _get_and_remove_last_element(self, stack):
        result = stack.pop()
        if stack.is_empty():
            return result
        else:
            last = self._get_and_remove_last_element(stack)
            stack.push(result)
            return last

    # 逆序栈：将栈底元素递归压入栈中
    def reserve(self, stack):
        if stack.is_empty():
            return
        last = self._get_and_remove_last_element(stack)
        self.reserve(stack)
        stack.push(last)


class MyTestCase(unittest.TestCase):

    def test_reserve_stack(self):
        reverse_stack = ReverseStack()
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        reverse_stack.reserve(stack)

        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()
