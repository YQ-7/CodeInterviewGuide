# -*- coding: utf-8 -*-

"""
题目：
    给定一个字符串数组strs，再给定两个单字符str1和str2，返回在strs中str1与str2的最小距离，如果str1或str2为null，或不在strs中，返回-1。
    要求当查询发生很多次，使每次的查询复制度为O(1)
"""

import unittest


class RecordMinDistance(object):

    def __init__(self, s):
        # (key: (key:value))结构，记录每一个字符，离其它字符的最近距离
        self.record = {}
        # 存放已遍历过，且离当前位置最近字符串的索引
        index_map = {}
        for i in range(len(s)):
            cur_str = s[i]
            # 更新记录
            self._update(index_map, cur_str, i)
            index_map[cur_str] = i

    def _update(self, index_map, cur_str, i):
        if self.record.get(cur_str) is None:
            self.record[cur_str] = {}
        cur_str_map = self.record.get(cur_str)
        for key, index in index_map.items():
            if key == cur_str:
                continue
            cur_min = i - index
            key_str_map = self.record.get(key)
            if key in cur_str:
                pre_min = cur_str_map.get(key)
                if cur_min < pre_min:
                    cur_str_map[key] = cur_min
                    key_str_map[cur_str] = cur_min
            else:
                cur_str_map[key] = cur_min
                key_str_map[cur_str] = cur_min

    def min_distance(self, s1, s2):
        if s1 is None or s2 is None:
            return
        if s1 == s2:
            return 0
        return self.record.get(s1, {}).get(s2, -1)


class MyTestCase(unittest.TestCase):
    def test_record_min_distance(self):
        record_min_distance = RecordMinDistance("1333231")
        self.assertEqual(2, record_min_distance.min_distance("1", "2"))
        self.assertEqual(-1, record_min_distance.min_distance("9", "2"))


if __name__ == '__main__':
    unittest.main()
