# -*- coding: utf-8 -*-

"""
题目：
    给定一个不含有重复值的数组arr，找到每一个i位置左边和右边离i位置最近且值比arr[i]小的位置。返回所有位置相应的信息。
    进阶问题：数组arr可以包含重复值
解答：
    利用单调栈结构
"""
import unittest
from utils.stack import Stack


# arr不含重复值情况
def get_near_less_no_repeat(arr):
    # 以二维数组作为结果，-1表示不存在
    res = [None] * len(arr)
    # stack按照从栈顶到栈底严格递减顺序存放arr数组的下标
    stack = Stack()
    for i, val in enumerate(arr):
        while not stack.is_empty() and val < arr[stack.peek()]:
            x = stack.pop()
            left_first_min = -1 if stack.is_empty() else stack.peek()
            right_first_min = i
            x_res = [left_first_min, right_first_min]
            res[x] = x_res
        stack.push(i)

    while not stack.is_empty():
        x = stack.pop()
        left_first_min = -1 if stack.is_empty() else stack.peek()
        right_first_min = -1
        x_res = [left_first_min, right_first_min]
        res[x] = x_res
    return res


# arr含重复值情况
def get_near_less(arr):
    # 以二维数组作为结果，-1表示不存在
    res = [None] * len(arr)
    # stack按照从栈顶到栈底严格递减顺序存放arr数组的下标
    stack = Stack()
    for i, val in enumerate(arr):
        while not stack.is_empty() and val < arr[stack.peek()[0]]:
            x_list = stack.pop()
            left_first_min = -1 if stack.is_empty() else stack.peek()[len(stack.peek()) - 1]
            right_first_min = i
            for x in x_list:
                x_res = [left_first_min, right_first_min]
                res[x] = x_res
        if not stack.is_empty() and arr[stack.peek()[0]] == val:
            stack.peek().append(i)
        else:
            stack.push([i])

    while not stack.is_empty():
        x_list = stack.pop()
        left_first_min = -1 if stack.is_empty() else stack.peek()[len(stack.peek()) - 1]
        right_first_min = -1
        for x in x_list:
            x_res = [left_first_min, right_first_min]
            res[x] = x_res
    return res


class MyTestCase(unittest.TestCase):
    def test_get_near_less_no_repeat(self):
        arr = [3, 4, 1, 5, 6, 2, 7]
        res = get_near_less_no_repeat(arr)
        self.assertEqual(-1, res[0][0])
        self.assertEqual(2, res[0][1])
        self.assertEqual(0, res[1][0])
        self.assertEqual(2, res[1][1])
        self.assertEqual(-1, res[2][0])
        self.assertEqual(-1, res[2][1])
        self.assertEqual(2, res[3][0])
        self.assertEqual(5, res[3][1])
        self.assertEqual(3, res[4][0])
        self.assertEqual(5, res[4][1])
        self.assertEqual(2, res[5][0])
        self.assertEqual(-1, res[5][1])
        self.assertEqual(5, res[6][0])
        self.assertEqual(-1, res[6][1])

    def test_get_near_less(self):
        arr = [3, 1, 3, 4, 3, 5, 3, 2, 2]
        res = get_near_less(arr)
        self.assertEqual(-1, res[0][0])
        self.assertEqual(1, res[0][1])
        self.assertEqual(-1, res[1][0])
        self.assertEqual(-1, res[1][1])
        self.assertEqual(1, res[2][0])
        self.assertEqual(7, res[2][1])
        self.assertEqual(2, res[3][0])
        self.assertEqual(4, res[3][1])
        self.assertEqual(1, res[4][0])
        self.assertEqual(7, res[4][1])
        self.assertEqual(4, res[5][0])
        self.assertEqual(6, res[5][1])
        self.assertEqual(1, res[6][0])
        self.assertEqual(7, res[6][1])
        self.assertEqual(1, res[7][0])
        self.assertEqual(-1, res[7][1])
        self.assertEqual(1, res[8][0])
        self.assertEqual(-1, res[8][1])


if __name__ == '__main__':
    unittest.main()
