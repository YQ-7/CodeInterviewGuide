"""
题目：
    可见的山峰对数量
    一个不含有负数的数组可以代表一圈环形山，每个位置的值代表山的高度。
    山峰A和山峰B能够相互看见的条件为：
        1.如果A和B是同一座山，认为不能相互看见。
        2.如果A和B是不同的山，并且在环中相邻，认为可以相互看见。
        3.如果A和B是不同的山，并且在环中不相邻，假设两座山高度的最小值为min。
          如果A通过next方向到B的途中没有高度比min大的山峰，
          或者A通过last方向到B的途中没有高度比min大的山峰，认为A和B可以相互看见。
"""

import unittest
from utils.stack import Stack


# 数组没有重复值情况
def get_visible_num_no_repeat(arr):
    if arr is None or len(arr) <= 1:
        return 0
    return len(arr) * 2 - 3


# 数组包含重复值情况
def get_visible_num(arr):
    if arr is None or len(arr) <= 1:
        return 0
    # 找到任一最大值
    max_i = 0
    for i, val in enumerate(arr):
        max_i = i if val > arr[max_i] else max_i
    # 从最大值开始遍历数组，用"小找大"方式统计可见山峰对
    # 构建单调栈：栈顶到栈底数据依次增大。数据结构：(值，出现次数)
    res = 0
    stack = Stack()
    stack.push(Record(arr[max_i], 1))
    arr_len = len(arr)
    index = next_index(max_i, arr_len)
    while index != max_i:
        # 当前值 > 栈顶数据值：弹出栈顶数据，统计出栈数据的山峰对数量
        while arr[index] > stack.peek().value:
            k = stack.pop().times
            res += 2 * k + get_internal_sum(k)
        # 当前值 = 栈顶数据值：栈顶数据，次数+1
        if arr[index] == stack.peek().value:
            stack.peek().times += 1
        # 当前值 < 栈顶数据值：将（值， 1）压入栈中
        else:
            stack.push(Record(arr[index], 1))
        index = next_index(index, arr_len)

    # 清理阶段
    # 弹出的数据不是栈中后2个元素
    while stack.size() > 2:
        times = stack.pop().times
        res += 2 * times + get_internal_sum(times)

    # 弹出的数据是栈中的倒数第2个元素
    if stack.size() == 2:
        times = stack.pop().times
        res += get_internal_sum(times) + (times if stack.peek().times == 1 else 2 * times)
    # 弹出的数据是栈中的最后1个元素
    res += get_internal_sum(stack.pop().times)
    return res


class Record(object):

    def __init__(self, value, times):
        self.value = value
        self.times = times


# 环形数组，当前位置为cur_index, 数组长度为size,返回下一个位置
def next_index(cur_index, size):
    return (cur_index + 1) % size


# 如果k==1, 返回0，如果k > 1,返回 C(2, k)
def get_internal_sum(k):
    return 0 if k == 1 else (k * (k - 1) / 2)


class MyTestCase(unittest.TestCase):
    def test_get_visible_num_no_repeat(self):
        arr = []
        self.assertEqual(0, get_visible_num_no_repeat(arr))
        arr = [1]
        self.assertEqual(0, get_visible_num_no_repeat(arr))
        arr = [3, 1, 2, 4, 5]
        self.assertEqual(7, get_visible_num_no_repeat(arr))

    def test_get_visible_num(self):
        arr = [4, 4, 5, 3, 2, 5, 4, 3, 5, 4, 2]
        self.assertEqual(22, get_visible_num(arr))


if __name__ == '__main__':
    unittest.main()
