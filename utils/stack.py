# -*- coding: utf-8 -*-

import unittest


class Stack(object):

    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return len(self.items) == 0

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        if self.is_empty():
            print("underflow")
            return
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("underflow")
            return
        else:
            return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


class TestStack(unittest.TestCase):

    def test_stack(self):
        my_stack = Stack()

        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        print(my_stack.size())
        print(my_stack.pop())
        print(my_stack.pop())
        my_stack.push(4)
        print(my_stack.pop())
        print(my_stack.pop())
        print(my_stack.size())
        print(my_stack.is_empty())
        print(my_stack.pop())


if __name__ == '__main__':
    unittest.main()
