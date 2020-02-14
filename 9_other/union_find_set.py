# -*- coding: utf-8 -*-
"""
题目：
    并查集的实现
"""

import unittest
from utils.stack import Stack


class Element(object):
    def __init__(self, value):
        self.value = value


class UnionFindSet(object):

    def __init__(self, values):
        # 记录集合中所有元素：key:元素值；value:元素
        self.element_map = {}
        # 记录每个元素的father元素：key:元素；value:father元素
        self.father_map = {}
        # 记录每个集合的秩：key:集合father元素；value:集合个数
        self.rank_map = {}
        for v in values:
            element = Element(v)
            self.element_map[v] = element
            # 初始化时，每个元素代表一个集合，father指向自己
            self.father_map[element] = element
            self.rank_map[element] = 1

    def find_head(self, element):
        """
            查找元素的父元素
            查找过程中将查找路径压缩：查找路径中元素均指向集合的顶层father
        """
        path = Stack()
        while element != self.father_map.get(element):
            path.push(element)
            element = self.father_map.get(element)
        while not path.is_empty():
            self.father_map[path.pop()] = element
        return element

    def is_same_set(self, a, b):
        """
            判断a、b是否属于同一个集合
        """
        if self.element_map.get(a) is None or self.element_map.get(b) is None:
            return False
        return self.find_head(self.element_map.get(a)) == self.find_head(self.element_map.get(b))

    def union(self, a, b):
        """
            合并a、b所在的集合
        """
        if self.element_map.get(a) is None or self.element_map.get(b) is None:
            return
        a_f = self.find_head(self.element_map.get(a))
        b_f = self.find_head(self.element_map.get(b))
        if a_f == b_f:
            return
        # 将元素个数少的集合合并到元素个数多的集合中
        big = a_f if self.rank_map.get(a_f) > self.rank_map.get(b_f) else b_f
        small = b_f if big == a_f else a_f
        self.father_map[small] = big
        self.rank_map[big] = self.rank_map[a_f] + self.rank_map[b_f]
        self.rank_map.pop(small)


class MyTestCase(unittest.TestCase):
    def test_num_trees(self):
        union_set = UnionFindSet([1, 2, 3, 4, 5])
        self.assertFalse(union_set.is_same_set(1, 2))
        union_set.union(1, 2)
        self.assertTrue(union_set.is_same_set(1, 2))
        self.assertFalse(union_set.is_same_set(2, 5))
        union_set.union(3, 5)
        union_set.union(3, 1)
        self.assertTrue(union_set.is_same_set(2, 5))


if __name__ == '__main__':
    unittest.main()
