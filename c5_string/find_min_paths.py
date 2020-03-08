# -*- coding: utf-8 -*-

"""
题目：
    给定两个字符串，记为start和to，再给定一个字符串列表list，list中一定包含to，list中没有重复字符串。
    所有的字符串都是小写的。规定start每次只能改变一个字符，最终的目标是彻底变成to，但是每次变成的新字符串必须在list中存在。
    请返回所有最短的变换路径。
"""
import unittest
from utils.queue import Queue


def find_min_paths(start, to, list_arr):
    # 将start加入list
    list_arr.append(start)
    # 根据list生成nexts图:改变一个字符，字符串可以到达哪些字符串
    nexts = get_nexts(list_arr)
    # 基于生成的nexts图，通过宽度优先遍历，求出每一个字符串到start的最短距离
    distances = get_distances(start, nexts)
    # 从start出发，通过深度优先算法，求出符号要求的最短路径结果集
    path_list = []
    res = []
    get_shortest_paths(start, to, nexts, distances, path_list, res)
    return res


def get_nexts(words):
    """
    生成每个字符串的nexts图，即邻接表
    """
    dict_set = set(words)
    nexts = {}
    for i in range(len(words)):
        nexts[words[i]] = get_word_next(words[i], dict_set)
    return nexts


def get_word_next(word, dict_set):
    """
    生成word字符串的nexts图：改变word的一个字符，字符串可以到达哪些字符串
    """
    res = []
    chs = list(word)
    for cur in range(ord('a'), ord('z') + 1):
        for i in range(len(chs)):
            if chs[i] == chr(cur):
                continue
            tmp = chs[i]
            chs[i] = chr(cur)
            if "".join(chs) in dict_set:
                res.append("".join(chs))
            chs[i] = tmp
    return res


def get_distances(start, nexts):
    """
    通过广度优先算法统计start到nexts图中每一个字符串的最短距离
    """
    distances = {}
    distances[start] = 0
    queue = Queue()
    queue.enqueue(start)
    record = set()
    record.add(start)
    while not queue.is_empty():
        cur = queue.dequeue()
        for w in nexts.get(cur, []):
            if w in record:
                continue
            distances[w] = distances[cur] + 1
            queue.enqueue(w)
            record.add(w)
    return distances


def get_shortest_paths(cur, to, nexts, distances, solution, res):
    solution.append(cur)
    if to == cur:
        res.append(solution.copy())
    else:
        for next_cur in nexts.get(cur, []):
            if distances.get(next_cur) == distances.get(cur) + 1:
                # 深度遍历直向距离+1的方向遍历
                get_shortest_paths(next_cur, to, nexts, distances, solution, res)
    solution.pop()


class MyTestCase(unittest.TestCase):
    def test_find_min_paths(self):
        start = 'abc'
        end = 'cab'
        words = ['cab', 'acc', 'cbc', 'ccc', 'cac', 'cbb', 'aab', 'abb']
        res = find_min_paths(start, end, words)
        self.assertEqual(4, len(res))
        self.assertEqual(start, res[0][0])
        self.assertEqual('abb', res[0][1])
        self.assertEqual('aab', res[0][2])
        self.assertEqual(end, res[0][3])


if __name__ == '__main__':
    unittest.main()
