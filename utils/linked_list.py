# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class DoubleNode(object):

    def __init__(self, data):
        self._data = data
        self._last = None
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        self._last = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class TreeNode(object):

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
