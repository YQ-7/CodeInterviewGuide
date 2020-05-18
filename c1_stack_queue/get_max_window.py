# -*- coding: utf-8 -*-

"""
题目：
    生成窗口最大数组
    有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。
    如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值。
    请实现一个函数：
        输入：整型数组arr，窗口大小为w。
        输出：一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的最大值。
解答：
    生成一个双端队列qmax来存放数组arr中的下标
    遍历arr[i]，qmax的放入规则：
        1.qmax为空，i放进qmax
        2.qmax不为空
            arr[i] < qmax队尾元素，直接将i放进qmax队尾
            arr[i] >= qmax队尾元素，将qmax队尾元素弹出，重复qmax的放入规则
        也就是说，如果qmax是空的，就直接放入当前的位置。
        如果qmax不是空的，qmax队尾的位置所代表的值如果不比当前的值大，将一直弹出队尾的位置，直到qmax队尾的位置所代表的值比当前的值大，当前的位置才放入qmax的队尾。
    遍历arr[i]，qmax的弹出规则：
        如果qmax队头的下标等于i-w，说明当前qmax队头的下标已过期，弹出当前对头的下标即可。
    根据如上的放入和弹出规则，qmax便成了一个维护窗口为w的子数组的最大值更新的结构。
"""

import unittest
from utils.deque import Deque


def get_max_window(arr, w):
    q_max = Deque()
    res = []
    for i, val in enumerate(arr):
        while len(q_max) > 0 and val >= arr[q_max.peek_left()]:
            q_max.popleft()
        q_max.appendleft(i)

        # 移除超过窗口长度w的过期数据
        if q_max.peek() == i - w:
            q_max.pop()
        # 当遍历的数据个数 >= 1个窗口长度时，开始收集数据
        if i >= w - 1:
            res.append(arr[q_max.peek()])
    return res


class MyTestCase(unittest.TestCase):
    def test_get_max_window(self):
        arr = [4, 3, 5, 4, 3, 3, 6, 7]
        res = get_max_window(arr, 3)
        self.assertEqual(5, res[0])
        self.assertEqual(5, res[1])
        self.assertEqual(5, res[2])
        self.assertEqual(4, res[3])
        self.assertEqual(6, res[4])
        self.assertEqual(7, res[5])


if __name__ == '__main__':
    unittest.main()
