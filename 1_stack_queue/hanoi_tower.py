# -*- coding: utf-8 -*-

"""
题目：
    用栈来求解汉诺塔问题。
    限制不能从最左侧的塔直接移动到最右侧，也不能从最右侧直接移动到最左侧，而是必须经过中间。求当塔有N层的时候，打印最优移动过程和最优移动总步数。
解答：
"""
import unittest
from utils.stack import Stack
from enum import Enum


# 返回移动的步数
def hanoi_problem_1(num, from_lab, to_lab):
    if num < 1:
        return 0
    return process(num, from_lab, to_lab)


def process(num, from_lab, to_lab):
    """
    递归的方法
    """
    left_lab = "left"
    mid_lab = "mid"
    right_lab = "right"
    # 只剩底层未移动
    if num == 1:
        if from_lab == mid_lab or to_lab == mid_lab:
            print("Move 1 from %s to %s" % (from_lab, to_lab))
            return 1
        else:
            print("Move 1 from %s to %s" % (from_lab, mid_lab))
            print("Move 1 from %s to %s" % (mid_lab, to_lab))
            return 2
    # 将N层从“中”移动到”左“/”右“，或从”左“/”右“移动到”中“
    # 需3个步骤
    # 例如：从”左“ -> “中”
    # 1）1 ~ N-1: "左" -> "右"
    # 2）第N层: "左" -> "中"
    # 3）1 ~ N-1: "右" -> "中"
    if from_lab == mid_lab or to_lab == mid_lab:
        another_lab = right_lab if from_lab == left_lab or to_lab == left_lab else left_lab
        part1 = process(num - 1, from_lab, another_lab)
        part2 = 1
        print("Move %d from %s to %s" % (num, from_lab, to_lab))
        part3 = process(num - 1, another_lab, to_lab)
        return part1 + part2 + part3
    else:
        # 将N层从“左”移动到”右“或从”右“移动到”左“
        # 需5个步骤
        # 例如：从”左“ -> “右”
        # 1）1 ~ N-1: "左" -> "右"
        # 2）第N层: "左" -> "中"
        # 3）1 ~ N-1: "右" -> "左"
        # 4）第N层: "中" -> "右"
        # 5）1 ~ N-1: "左" -> "右"
        part1 = process(num - 1, from_lab, to_lab)
        part2 = 1
        print("Move %d from %s to %s" % (num, from_lab, mid_lab))
        part3 = process(num - 1, to_lab, from_lab)
        part4 = 1
        print("Move %d from %s to %s" % (num, mid_lab, to_lab))
        part5 = process(num - 1, from_lab, to_lab)
        return part1 + part2 + part3 + part4 + part5


def hanoi_problem_2(num):
    """
        非递归方法，用栈来模拟整个过程
        把左、中、右三个地点抽象成栈，依次记为LS、MS和RS。
        最初所有的塔都在LS上。移动的动作看成：某一个栈（from）把栈顶元素弹出，然后压入到另一个栈里（to），作为这一个栈（to）的栈顶
        移动过程中需满足2个原则：
            1）小压大：from栈弹出的元素一定要小于to栈底元素
            2）相邻不可逆：想走出最少步数，任何两个相邻的动作都不是互为逆过程
        每一步只会有一个动作达标。那么只要每走一步都根据这两个原则考查所有的动作就可以，
        哪个动作达标就走哪个动作，反正每次都只有一个动作满足要求，按顺序走下来即可
    """
    left_lab = "left"
    mid_lab = "mid"
    right_lab = "right"
    left_stack = Stack()
    mid_stack = Stack()
    right_stack = Stack()
    # 将数据压入栈中
    for i in range(num, 0, -1):
        left_stack.push(i)
    record = [Action.No]
    step = 0
    while right_stack.size() != num:
        step += f_stack_to_t_stack(record, Action.MToL, Action.LToM,
                                   left_stack, mid_stack, left_lab, mid_lab)
        step += f_stack_to_t_stack(record, Action.LToM, Action.MToL,
                                   mid_stack, left_stack, mid_lab, left_lab)
        step += f_stack_to_t_stack(record, Action.RToM, Action.MToR,
                                   mid_stack, right_stack, mid_lab, right_lab)
        step += f_stack_to_t_stack(record, Action.MToR, Action.RToM,
                                   right_stack, mid_stack, right_lab, mid_lab)
    return step


class Action(Enum):
    No = 0
    LToM = 1
    MToL = 2
    MToR = 3
    RToM = 4


def f_stack_to_t_stack(record, pre_no_act, now_act,
                       f_stack, t_stack,
                       from_lab, to_lab):
    if record[0] != pre_no_act and not f_stack.is_empty() and (t_stack.is_empty() or f_stack.peek() < t_stack.peek()):
        print("Move %d from %s to %s" % (f_stack.peek(), from_lab, to_lab))
        t_stack.push(f_stack.pop())
        record[0] = now_act
        return 1
    return 0


class MyTestCase(unittest.TestCase):
    def test_hanoi_problem_1(self):
        self.assertEqual(2, hanoi_problem_1(1, "left", "right"))
        self.assertEqual(8, hanoi_problem_1(2, "left", "right"))

    def test_hanoi_problem_2(self):
        self.assertEqual(2, hanoi_problem_2(1))
        self.assertEqual(8, hanoi_problem_2(2))


if __name__ == '__main__':
    unittest.main()
