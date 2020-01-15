# -*- coding: utf-8 -*-

from collections import deque


class Deque(deque):

    def peek_left(self):
        value = self.popleft()
        self.appendleft(value)
        return value

    def peek(self):
        value = self.pop()
        self.append(value)
        return value

    def is_empty(self):
        return len(self) == 0
