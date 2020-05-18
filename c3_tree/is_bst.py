# -*- coding: utf-8 -*-
"""
题目：
    给定二叉树的一个头节点head，已知其中没有重复值的节点，判断是否是搜索二叉树
解答:
    判断一棵二叉树是否为搜索二叉树，只要改写一个二叉树中序遍历，在遍历的过程中看节点值是否都是递增的即可
"""

import unittest
from utils.linked_list import TreeNode


def is_bst(head):
    """
        通过Morris遍历实现二叉树中序遍历
        遍历过程中，判断值是否递增
    """
    if head is None:
        return True
    cur = head
    pre = None
    while cur is not None:
        # cur有左子树
        most_right = cur.left
        if most_right is not None:
            # 找到cur左子树上最右节点
            while most_right.right is not None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                # mon_right.right指向cur
                # 以便遍历完左子树后，可以通过此索引返回
                most_right.right = cur
                # cur 相左移动
                cur = cur.left
                continue
            else:
                # 若过most_right.right == cur,将其还原为null
                most_right.right = None
        # 判断按中序遍历值是否递增
        if pre is not None and pre.data > cur.data:
            return False
        pre = cur
        # cur没有左子树，cur向右移动
        # 或cur左子树最右节点右指针指向cur，cur向右移动
        cur = cur.right
    return True


class MyTestCase(unittest.TestCase):

    @staticmethod
    def make_data():
        node_1 = TreeNode(4)
        node_2 = TreeNode(2)
        node_3 = TreeNode(5)
        node_4 = TreeNode(1)
        node_5 = TreeNode(3)
        head = node_1
        head.left = node_2
        head.right = node_3
        node_2.left = node_4
        node_2.right = node_5
        return head

    def test_is_bst(self):
        self.assertTrue(is_bst(self.make_data()))


if __name__ == '__main__':
    unittest.main()
