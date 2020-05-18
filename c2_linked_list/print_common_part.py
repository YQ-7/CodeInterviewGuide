# -*- coding: utf-8 -*-

"""
题目：
    给定两个有序链表的头指针head1和head2，打印两个链表的公共部分。
"""

import unittest
from utils.linked_list import Node


def print_common_part(head1, head2):
    common_count = 0
    print(" Common Part:", end=' ')
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            print(str(head1.data), end=' ')
            head1 = head1.next
            head2 = head2.next
            common_count += 1
    return common_count


class MyTestCase(unittest.TestCase):
    def test_print_common_part(self):
        head1 = Node(1)
        node1_2 = Node(3)
        node1_3 = Node(5)
        node1_4 = Node(7)
        node1_5 = Node(10)
        head1.next = node1_2
        node1_2.next = node1_3
        node1_3.next = node1_4
        node1_4.next = node1_5

        head2 = Node(3)
        node2_2 = Node(4)
        node2_3 = Node(5)
        node2_4 = Node(7)
        node2_5 = Node(11)
        head2.next = node2_2
        node2_2.next = node2_3
        node2_3.next = node2_4
        node2_4.next = node2_5

        self.assertEqual(3, print_common_part(head1, head2))


if __name__ == '__main__':
    unittest.main()
