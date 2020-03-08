# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符串数组strs[]，在strs中有些位置为null，但在不为null的位置上，其字符串是按照字典顺序由小到大依次出现的。
    再给定一个字符串str，请返回str在strs中出现的最左的位置。
"""
import unittest


def get_index(strs, s):
    """
        通过二分查找法擦查询，需注意处理Null值
    """
    if strs is None or len(strs) == 0 or s is None:
        return -1
    res = -1
    left = 0
    right = len(strs) - 1
    while left <= right:
        mid = (left + right) // 2
        if strs[mid] is not None and strs[mid] == s:
            res = mid
            right = mid - 1
        elif strs[mid] is not None:
            if strs[mid] < s:
                left = mid + 1
            else:
                right = mid - 1
        else:
            i = mid
            # 跳过None值
            while strs[i] is None and i >= left:
                i -= 1
            if i < left or strs[i] < s:
                left = mid + 1
            else:
                res = i if strs[i] == s else res
                right = i - 1
    return res


class MyTestCase(unittest.TestCase):
    def test_get_index(self):
        self.assertEqual(1, get_index([None, "a", None, "a", None, "b", None, "c"], "a"))
        self.assertEqual(-1, get_index([None, "a", None, "a", None, "b", None, "c"], None))
        self.assertEqual(-1, get_index([None, "a", None, "a", None, "b", None, "c"], "d"))


if __name__ == '__main__':
    unittest.main()

