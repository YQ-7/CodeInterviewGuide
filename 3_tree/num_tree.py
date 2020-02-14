# -*- coding: utf-8 -*-
"""
题目：
    给定一个整数N，如果N＜1，代表空树结构，否则代表中序遍历的结果为{1，2，3，…，N}。请返回可能的二叉树结构有多少
"""

import unittest
from utils.linked_list import TreeNode


def num_trees(n):
    # n = 0,1时，只会生成1课树
    if n < 2:
        return 1
    num = [0] * (n + 1)
    num[0] = 1

    for i in range(1, n + 1):
        # i个节点数据 = sum(分别以j为头结点的数据)
        for j in range(1, i + 1):
            num[i] += num[j - 1] * num[i - j]
    return num[n]


def generate_trees(n):
    """
        返回所能生成二叉树的所有头结点
    """
    return generate(1, n)


def generate(start, end):
    res = []
    if start > end:
        res.append(None)
        return res

    for i in range(start, end + 1):
        head = TreeNode(i)
        # 递归生成左子树所有可能结构
        l_subs = generate(start, i - 1)
        # 递归生成右子树所有可能结构
        r_subs = generate(i + 1, end)
        for l in l_subs:
            for r in r_subs:
                head.left = l
                head.right = r
                res.append(clone_tree(head))
    return res


def clone_tree(head):
    if head is None:
        return None
    res = TreeNode(head.data)
    res.left = clone_tree(head.left)
    res.right = clone_tree(head.right)
    return res


class MyTestCase(unittest.TestCase):
    def test_num_trees(self):
        self.assertEqual(1, num_trees(1))
        self.assertEqual(2, num_trees(2))
        self.assertEqual(5, num_trees(3))

    def test_generate_tree(self):
        res = generate_trees(3)

        self.assertTrue(5, len(res))

        self.assertTrue(1, res[0].data)
        self.assertTrue(2, res[0].right.data)
        self.assertTrue(3, res[0].right.right.data)

        self.assertTrue(2, res[2].data)
        self.assertTrue(1, res[2].left.data)
        self.assertTrue(3, res[2].right.data)


if __name__ == '__main__':
    unittest.main()
