"""
题目：
    用一个栈实现另一个栈的排序，将该栈从顶到底按从大到小的顺序排序，只许申请一个栈。除此之外，可以申请新的变量，但不能申请额外的数据结构。
解答：
    将要排序的栈记为stack,辅助栈记为help。stack栈顶的元素为cur
        1.如果cur <= help栈顶元素，则将cur压入help
        2.如果cur > help栈顶元素，则将help栈元素依次弹出压入stack，直到cur <= help栈顶元素，再将cur压入help
    重复执行上述操作，直到stack栈所有元素压入到help栈，再将help元素依次弹出压入stack,及完成排序
"""
import unittest
from utils.stack import Stack


def sort_stack(stack):
    help_stack = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        while not help_stack.is_empty() and cur > help_stack.peek():
            stack.push(help_stack.pop())
        help_stack.push(cur)
    reverse(stack, help_stack)


def reverse(stack, help_stack):
    while not help_stack.is_empty():
        stack.push(help_stack.pop())


class MyTestCase(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        stack.push(12)
        stack.push(-2)
        stack.push(5)
        stack.push(1)
        stack.push(-100)
        sort_stack(stack)
        self.assertEqual(12, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(-2, stack.pop())
        self.assertEqual(-100, stack.pop())


if __name__ == '__main__':
    unittest.main()
