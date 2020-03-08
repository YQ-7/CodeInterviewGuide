# -*- coding: utf-8 -*-

"""
题目：
    给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让最终结果字符串的字典序最小
"""

import unittest


def remove_duplicate_letters(s):
    chas = list(s)
    # 统计字符频率
    chas_map = [0] * 26
    for c in chas:
        chas_map[ord(c) - ord('a')] += 1
    res = []
    left = 0
    right = 0
    # 遍历字符，依次选取ASCII码为最小字符为当前位置字符
    while right != len(chas):
        if chas_map[ord(chas[right]) - ord('a')] == -1:
            right += 1
            continue
        # 减少词频
        chas_map[ord(chas[right]) - ord('a')] -= 1
        if chas_map[ord(chas[right]) - ord('a')] > 0:
            right += 1
            continue
        # 出现词频==0时
        # s[l..r]中所需考虑的字符中，查找ASCII码最小的
        pick = -1
        for i in range(left, right + 1):
            if chas_map[ord(chas[i]) - ord('a')] != -1 and (pick == -1 or chas[i] < chas[pick]):
                pick = i
        res.append(chas[pick])
        # 将s[pick..r]词频还原
        for i in range(pick + 1, right + 1):
            if chas_map[ord(chas[i]) - ord('a')] != -1:
                chas_map[ord(chas[i]) - ord('a')] += 1
        # 将s[pick]后续不再考虑
        chas_map[ord(chas[pick]) - ord('a')] = -1
        # 继续在s[pick+1..N]中重复
        left = pick + 1
        right = left
    return ''.join(res)


class MyTestCase(unittest.TestCase):
    def test_remove_duplicate_letters(self):
        self.assertEqual("dabc", remove_duplicate_letters("dbcacbca"))


if __name__ == '__main__':
    unittest.main()
