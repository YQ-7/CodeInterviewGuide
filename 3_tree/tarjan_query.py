# -*- coding: utf-8 -*-
"""
题目：
    Tarjan算法与并查集解决二叉树节点间最近公共祖先的批量查询问题
"""

import unittest
from utils.linked_list import TreeNode
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

    def find_head(self, value):
        return self._find_head(self.element_map.get(value)) if self.element_map.get(value) is not None else None

    def _find_head(self, element):
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
        return self._find_head(self.element_map.get(a)) == self._find_head(self.element_map.get(b))

    def union(self, a, b):
        """
            合并a、b所在的集合
        """
        if self.element_map.get(a) is None or self.element_map.get(b) is None:
            return
        a_f = self._find_head(self.element_map.get(a))
        b_f = self._find_head(self.element_map.get(b))
        if a_f == b_f:
            return
        # 将元素个数少的集合合并到元素个数多的集合中
        big = a_f if self.rank_map.get(a_f) > self.rank_map.get(b_f) else b_f
        small = b_f if big == a_f else a_f
        self.father_map[small] = big
        self.rank_map[big] = self.rank_map[a_f] + self.rank_map[b_f]
        self.rank_map.pop(small)


class Query(object):

    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2


def tarjan_query(head, queries):
    query_map = {}
    index_map = {}
    ancestor_map = {}
    sets = UnionFindSet(get_all_nodes(head))
    ans = [None] * len(queries)
    set_queries_and_easy_answers(queries, ans, query_map, index_map)
    set_answers(head, ans, query_map, index_map, ancestor_map, sets)
    return ans


def get_all_nodes(head):
    res = []
    process(head, res)
    return res


def process(head, res):
    if head is None:
        return
    res.append(head)
    process(head.left, res)
    process(head.right, res)


def set_queries_and_easy_answers(ques, ans, query_map, index_map):
    for i in range(len(ans)):
        o1 = ques[i].o1
        o2 = ques[i].o2
        if o1 == o2 or o1 is None or o2 is None:
            ans[i] = o1 if o1 is not None else o2
        else:
            if query_map.get(o1) is None:
                query_map[o1] = []
                index_map[o1] = []
            if query_map.get(o2) is None:
                query_map[o2] = []
                index_map[o2] = []
            query_map.get(o1).append(o2)
            index_map.get(o1).append(i)
            query_map.get(o2).append(o1)
            index_map.get(o2).append(i)


def set_answers(head, ans, query_map, index_map, ancestor_map, sets):
    if head is None:
        return
    set_answers(head.left, ans, query_map, index_map, ancestor_map, sets)
    sets.union(head.left, head)
    ancestor_map[sets.find_head(head)] = head
    set_answers(head.right, ans, query_map, index_map, ancestor_map, sets)
    sets.union(head.right, head)
    ancestor_map[sets.find_head(head)] = head
    n_list = query_map.get(head)
    i_list = index_map.get(head)
    if n_list is not None:
        n_list.reverse()
    if i_list is not None:
        i_list.reverse()
    while n_list is not None and not len(n_list) == 0:
        node = n_list.pop()
        index = i_list.pop()
        node_father = sets.find_head(node)
        if ancestor_map.get(node_father) is not None:
            ans[index] = ancestor_map.get(node_father)


class MyTestCase(unittest.TestCase):
    def test_tarjan_query(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)
        node_4 = TreeNode(4)
        node_5 = TreeNode(5)
        node_6 = TreeNode(6)
        node_7 = TreeNode(7)
        node_8 = TreeNode(8)
        node_9 = TreeNode(9)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        node_3.right = node_6
        node_5.left = node_7
        node_5.right = node_8
        node_6.left = node_9

        queries = []
        queries.append(Query(node_4, node_7))
        queries.append(Query(node_7, node_8))
        queries.append(Query(node_8, node_9))
        queries.append(Query(node_9, node_3))
        queries.append(Query(node_6, node_6))
        queries.append(Query(None, node_5))
        queries.append(Query(None, None))

        ans = tarjan_query(head, queries)
        self.assertEqual(node_2, ans[0])
        self.assertEqual(node_5, ans[1])
        self.assertEqual(node_1, ans[2])
        self.assertEqual(node_3, ans[3])
        self.assertEqual(node_6, ans[4])
        self.assertEqual(node_5, ans[5])
        self.assertIsNone(ans[6])


if __name__ == '__main__':
    unittest.main()
