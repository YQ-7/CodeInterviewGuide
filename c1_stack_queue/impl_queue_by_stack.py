# -*- coding: utf-8 -*-

"""
    题目：
        编写一个类，用两个栈实现队列，支持队列的基本操作（add、poll、peek）。
    解答：
        栈的特点是先进后出，而队列的特点是先进先出。用两个栈正好能把顺序反过来实现类似队列的操作。
        stackPush：作为数据压入栈
        stackPop：作为数据弹出栈
        需满足以下2点：
            1.如果stackPush要往stackPop中压入数据，那么必须一次性把stackPush中的数据全部压入。
            2.如果stackPop不为空，stackPush绝对不能向stackPop中压入数据。
"""

from utils.stack import Stack
import unittest


class ImplQueueByStack(object):

    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()

    # 将stackPush数据导入stackPop中。以保持出栈顺序为先进先出
    def _push_to_pop(self):
        # 仅当stackPops为空，且stackPush数据不为空时，进行数据导入操作
        if self.stackPop.is_empty() and (not self.stackPush.is_empty()):
            while not self.stackPush.is_empty():
                item = self.stackPush.pop()
                self.stackPop.push(item)

    # 向队列压入数据
    def add(self, item):
        self.stackPush.push(item)
        self._push_to_pop()

    # 返回并弹出队首数据
    def poll(self):
        if self.stackPop.is_empty() and self.stackPush.is_empty():
            raise Exception("Queue is emtpy.")
        self._push_to_pop()
        return self.stackPop.pop()

    # 返回队首数据
    def peek(self):
        if self.stackPop.is_empty() and self.stackPush.is_empty():
            raise Exception("Queue is emtpy.")
        self._push_to_pop()
        return self.stackPop.peek()


class MyTestCase(unittest.TestCase):

    def test_queue(self):
        queue = ImplQueueByStack()
        queue.add(1)
        queue.add(2)
        self.assertEqual(queue.peek(), 1)
        queue.add(3)
        queue.add(4)
        self.assertEqual(queue.poll(), 1)
        queue.add(5)
        self.assertEqual(queue.poll(), 2)
        self.assertEqual(queue.poll(), 3)
        self.assertEqual(queue.poll(), 4)
        queue.add(6)
        queue.add(7)
        self.assertEqual(queue.poll(), 5)
        self.assertEqual(queue.peek(), 6)
        self.assertEqual(queue.poll(), 6)
        self.assertEqual(queue.poll(), 7)


if __name__ == '__main__':
    unittest.main()
