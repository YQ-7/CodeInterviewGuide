# -*- coding: utf-8 -*-

import unittest


class Queue(object):

    def __init__(self, length=10):
        self.items = [None] * length
        self.length = length
        self.head = None
        self.tail = 0

    def enqueue(self, item):
        if self.tail == self.head:
            print("Queue overflow")
            return
        self.items[self.tail] = item
        if self.head is None:
            self.head = self.tail
        self.tail = (self.tail + 1) % self.length

    def dequeue(self):
        if self.head is None:
            print("Queue underflow")
            return
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.length

        if self.head == self.tail:
            self.head = None
        return item

    def peek(self):
        if self.head is None:
            print("Queue underflow")
            return
        item = self.items[self.head]
        return item

    def size(self):
        if self.head is None:
            return 0
        if self.tail > self.head:
            return self.tail - self.head
        else:
            return self.length - self.head + self.tail

    def is_empty(self):
        return self.head is None


class TestQueue(unittest.TestCase):

    def test_queue(self):
        my_queue = Queue(length=3)
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        print(my_queue.is_empty())
        print(my_queue.size())
        my_queue.enqueue(4)
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.is_empty())


if __name__ == '__main__':
    unittest.main()
