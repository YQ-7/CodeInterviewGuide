# -*- coding: utf-8 -*-

"""
    题目：
        给定一个字符类型的数组chas和一个整数size，请把大小为size的左半区整体移到右半区，右半区整体移到左边
"""
import unittest


def rotate_part_1(chas, size):
    """
        方法一
    """
    if chas is None or size <= 0 or size >= len(chas):
        return
    # chas[0..size-1]逆序
    reverse(chas, 0, size - 1)
    # chas[size..n]逆序
    reverse(chas, size, len(chas) - 1)
    # chas[0..n]逆序
    reverse(chas, 0, len(chas) - 1)


def reverse(chas, start, end):
    while start < end:
        tmp = chas[start]
        chas[start] = chas[end]
        chas[end] = tmp
        start += 1
        end -= 1


def rotate_part_2(chas, size):
    """
        方法二
    """
    if chas is None or size <= 0 or size >= len(chas):
        return
    start = 0
    end = len(chas) - 1
    part_l = size
    part_r = len(chas) - size
    s = min(part_l, part_r)
    d = part_l - part_r
    while True:
        # 每次交换个数少的分组
        exchange(chas, start, end, s)
        if d == 0:
            break
        elif d > 0:
            start += s
            part_l = d
        else:
            end -= s
            part_r = -d
        s = min(part_l, part_r)
        d = part_l - part_r


def exchange(chas, start, end, size):
    i = end - size + 1
    while size != 0:
        size -= 1
        tmp = chas[start]
        chas[start] = chas[i]
        chas[i] = tmp
        start += 1
        i += 1


class MyTestCase(unittest.TestCase):
    def test_rotate_part_1(self):
        chas = list("ABCDE")
        rotate_part_1(chas, 3)
        self.assertEqual("DEABC", "".join(chas))

    def test_rotate_part_2(self):
        chas = list("1234567ABCD")
        rotate_part_2(chas, 7)
        self.assertEqual("ABCD1234567", "".join(chas))


if __name__ == '__main__':
    unittest.main()
