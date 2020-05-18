"""
    题目：0左边必有1的二进制字符串数量
        给定一个整数N，求由＂0＂字符与＂1＂字符组成的长度为N的所有字符串中，满足＂0＂字符的左边必有＂1＂字符的字符串数量
"""
import unittest


def get_num_1(n):
    """
        p(i):表示0~i-1位置上的字符已确定，符合要求且i-1位置为"1"时，
            i~n-1符合要求的字符串数量
        i < n-1:p(i) = p(i+1) + p(i+2)
        i = n-1:p(i) = 2
        i = n:p(i) = 1
        时间复杂度：O(n*2^n)
    """
    if n < 1:
        return 0
    return process(1, n)


def process(i, n):
    if i == n - 1:
        return 2
    if i == n:
        return 1
    return process(i + 1, n) + process(i + 2, n)


def get_num_2(n):
    """
    满足初始项为1，2的斐波那契数列
    用非递归版本实现
    时间复杂度：O(n)
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    pre = 1
    cur = 1
    for i in range(2, n + 1):
        tmp = cur
        cur += pre
        pre = tmp
    return cur


def get_num_3(n):
    """
    满足初始项为1，2的斐波那契数列
    TODO:矩阵乘法求解法
    :param n:
    :return:
    """
    pass


class MyTestCase(unittest.TestCase):
    def test_get_num_1(self):
        self.assertEqual(1, get_num_1(1))
        self.assertEqual(2, get_num_1(2))
        self.assertEqual(3, get_num_1(3))

    def test_get_num_2(self):
        self.assertEqual(1, get_num_2(1))
        self.assertEqual(2, get_num_2(2))
        self.assertEqual(3, get_num_2(3))


if __name__ == '__main__':
    unittest.main()
