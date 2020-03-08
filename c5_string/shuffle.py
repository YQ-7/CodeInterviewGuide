# -*- coding: utf-8 -*-

"""
    题目：
       给定一个长度为偶数的数组arr，长度记为2×N。前N个为左部分，后N个为右部分。
       arr就可以表示为{L1，L2，..，Ln，R1，R2，..，Rn}，请将数组调整成{R1，L1，R2，L2，..，Rn，Ln}的样子。
"""
import unittest


def shuffle_main(arr):
    """
        时间复杂度为O(N)
        额外空间复杂度为O(1)
    """
    # 数组不为空，且长度为偶数
    if arr is not None and len(arr) > 0 and len(arr) & 1 == 0:
        shuffle(arr, 0, len(arr) - 1)


def shuffle(arr, l, r):
    # 切成一块一块解决，每一块长度满足(3^k) - 1
    while r - l + 1 > 0:
        length = r - l + 1
        base = 3
        k = 1
        # 找到<= length且最近的，满足(3^k) - 1的数
        # 即3^k <= length + 1
        while base <= (length + 1) // 3:
            base *= 3
            k += 1
        # 当前要解决长度为base - 1
        half = (base - 1) // 2
        # [L..R]中点
        mid = (l + r) // 2
        # 旋转的左半部分[L+half..mid]，右半部分[mid+1..mid+half]
        rotate_part(arr, l + half, mid, mid + half)

        # [L..base-1]进行下标连续推
        cycles(arr, l, base - 1, k)
        # 处理剩下部分[L+base-1..N]
        l = l + base - 1


def cycles(arr, start, length, k):
    """
    下标连续推过程，出发位置依次为：1，3，9....
    :param start: 位置开始
    :param length: 长度
    :param k: 出发位置个数
    """
    trigger = 1  # 出发位置
    for i in range(k):
        pre_value = arr[trigger + start - 1]
        cur = modify_index(trigger, length)
        # 循环遍历回到起点结束
        while cur != trigger:
            tmp = arr[cur + start - 1]
            arr[cur + start - 1] = pre_value
            pre_value = tmp
            cur = modify_index(cur, length)
        arr[cur + start - 1] = pre_value


def rotate_part(arr, l, m, r):
    """
        交换左右两部分：左半部分[l..m]，右半部分[m..r]
    """
    reverse(arr, l, m)
    reverse(arr, m + 1, r)
    reverse(arr, l, r)


def reverse(chas, start, end):
    while start < end:
        tmp = chas[start]
        chas[start] = chas[end]
        chas[end] = tmp
        start += 1
        end -= 1


def modify_index(i, length):
    """
    获取位置i调整后的位置
    """
    return (2 * i) % (length + 1)


class MyTestCase(unittest.TestCase):
    def test_shuffle_main(self):
        arr = [1, 2, 3, 4, 5, 6]
        shuffle_main(arr)
        self.assertEqual(4, arr[0])
        self.assertEqual(1, arr[1])
        self.assertEqual(5, arr[2])
        self.assertEqual(2, arr[3])
        self.assertEqual(6, arr[4])
        self.assertEqual(3, arr[5])


if __name__ == '__main__':
    unittest.main()
