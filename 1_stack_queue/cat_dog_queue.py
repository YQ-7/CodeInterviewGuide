# -*- coding: utf-8 -*-

"""
题目：
    实现一种狗猫队列的结构，要求如下：
    1.用户可以调用add方法将cat类或dog类的实例放入队列中；
    2.用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出；
    3.用户可以调用pollDog方法，将队列中dog类的实例按照进队列的先后顺序依次弹出；
    4.用户可以调用pollCat方法，将队列中cat类的实例按照进队列的先后顺序依次弹出；
    5.用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例；
    6.用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例；
    7.用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例。

解答：
    队列元素新增数据项，用来记录进入队列的时间。
    同时有2个队列，一个只存放dog实例，一个只存放cat实例
    通过比较dog队列和cat队列队首元素时间的大小来判断哪个元素先进入的队列
"""

import unittest
from utils.my_queue import Queue


class Pet(object):

    def __init__(self, p_type):
        self._p_type = p_type

    @property
    def p_type(self):
        return self._p_type


class Dog(Pet):

    def __init__(self):
        super().__init__("Dog")


class Cat(Pet):

    def __init__(self):
        super().__init__("Cat")


class PetEnterQueue(Pet):

    def __init__(self, pet, count):
        self._pet = pet
        self._count = count

    @property
    def pet(self):
        return self._pet

    @property
    def count(self):
        return self._count

    @property
    def p_type(self):
        return self._pet.p_type


class DogCatQueue(object):

    def __init__(self):
        self.dogQ = Queue()
        self.catQ = Queue()
        self._count = 0

    def add(self, pet):
        if "Dog" == pet.p_type:
            self.dogQ.enqueue(PetEnterQueue(pet, self._count))
        if "Cat" == pet.p_type:
            self.catQ.enqueue(PetEnterQueue(pet, self._count))

        self._count += 1

    def poll_all(self):
        if not self.dogQ.is_empty() and not self.catQ.is_empty():
            # count小的元素为先进入队列的元素
            if self.dogQ.peek().count < self.catQ.peek().count:
                return self.dogQ.dequeue().pet
            else:
                return self.catQ.dequeue().pet
        elif not self.dogQ.is_empty():
            return self.dogQ.dequeue().pet
        elif not self.catQ.is_empty():
            self.catQ.dequeue().pet
        else:
            raise Exception("Queue is empty")

    def poll_dog(self):
        if not self.dogQ.is_empty():
            return self.dogQ.dequeue().pet
        else:
            raise Exception("Dog queue is empty")

    def poll_cat(self):
        if not self.catQ.is_empty():
            return self.catQ.dequeue().pet
        else:
            raise Exception("Cat queue is empty")

    def is_empty(self):
        return self.dogQ.is_empty() and self.catQ.is_empty()

    def is_dog_queue_empty(self):
        return self.dogQ.is_empty()

    def is_cat_queue_empty(self):
        return self.catQ.is_empty()


class MyTestCase(unittest.TestCase):

    def test_cat_dog_queue(self):
        queue = DogCatQueue()
        self.assertTrue(queue.is_empty())
        queue.add(Dog())
        queue.add(Dog())
        self.assertTrue(queue.is_cat_queue_empty())
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_dog_queue_empty())
        queue.add(Cat())
        queue.add(Dog())
        queue.add(Cat())
        self.assertEqual("Cat", queue.poll_cat().p_type)
        self.assertEqual("Dog", queue.poll_all().p_type)
        self.assertEqual("Dog", queue.poll_all().p_type)
        self.assertEqual("Dog", queue.poll_dog().p_type)
        self.assertEqual("Cat", queue.poll_cat().p_type)


if __name__ == '__main__':
    unittest.main()
