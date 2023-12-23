import re
import math

Monkeys = []
GCF = 9699690
#GCF = 96577

def opMonkey0(value):
    return (value * 17)
def opMonkey1(value):
    return (value * value)
def opMonkey2(value):
    return (value + 7)
def opMonkey3(value):
    return (value + 4)
def opMonkey4(value):
    return (value + 5)
def opMonkey5(value):
    return (value + 6)
def opMonkey6(value):
    return (value * 13)
def opMonkey7(value):
    return (value + 2)
'''
def opMonkey0(value):
    return (value * 19)
def opMonkey1(value):
    return (value + 6)
def opMonkey2(value):
    return (value * value)
def opMonkey3(value):
    return (value + 3)
'''

class monkey:
    def __init__(self, Op, Test: int, TrueM: int, FalseM: int, Items: list):
        self.op = Op
        self.true = TrueM
        self.false = FalseM
        self.testVal = Test
        self.items = Items
        self.count = 0
    def test(self, value):
        self.count = self.count + 1
        value = value % GCF
        if (value % self.testVal) == 0:
            Monkeys[self.true].items.append(value)
        else:
            Monkeys[self.false].items.append(value)
    items:list = []
    testVal:int = 0
    op = opMonkey0
    true:int = 0
    false:int = 0
    count:int = 0

def parse():
    global Monkeys
    oMonkey0 = monkey(opMonkey0, 2, 2, 6, [85, 79, 63, 72])
    oMonkey1 = monkey(opMonkey1, 7, 0, 2, [53,94,65,81,93,73,57,92])
    oMonkey2 = monkey(opMonkey2, 13, 7, 6, [62,63])
    oMonkey3 = monkey(opMonkey3, 5, 4, 5, [57,92,56])
    oMonkey4 = monkey(opMonkey4, 3, 1, 5, [67])
    oMonkey5 = monkey(opMonkey5, 19, 1, 0, [85,56,66,72,57,99])
    oMonkey6 = monkey(opMonkey6, 11, 3, 7, [86,65,98,97,69])
    oMonkey7 = monkey(opMonkey7, 17, 4, 3, [87,68,92,66,91,50,68])
    Monkeys = [oMonkey0, oMonkey1, oMonkey2, oMonkey3, oMonkey4, oMonkey5, oMonkey6, oMonkey7]
    '''
    oMonkey0 = monkey(opMonkey0, 23, 2, 3, [79, 98])
    oMonkey1 = monkey(opMonkey1, 19, 2, 0, [54,65,75,74])
    oMonkey2 = monkey(opMonkey2, 13, 1, 3, [79,60,97])
    oMonkey3 = monkey(opMonkey3, 17, 0, 1, [74])
    Monkeys = [oMonkey0, oMonkey1, oMonkey2, oMonkey3]
    '''

def part1():
    global Monkeys
    for i in range(20):
        for m in Monkeys:
            while len(m.items) > 0:
                value = m.items[0]
                m.items.remove(value)
                value = m.op(value)
                value = math.floor(value / 3)
                m.test(value)
    vals = []
    for m in Monkeys:
        vals.append(m.count)
        vals.sort()
    print(f"{vals[-1]} * {vals[-2]} = {vals[-1] * vals[-2]}")

def part2():
    global Monkeys
    for i in range(10000):
        for m in Monkeys:
            while len(m.items) > 0:
                value = m.items[0]
                m.items.remove(value)
                value = m.op(value)
                m.test(value)
    vals = []
    for m in Monkeys:
        vals.append(m.count)
        vals.sort()
    print(f"{vals[-1]} * {vals[-2]} = {vals[-1] * vals[-2]}")

if __name__ == '__main__':
    parse()
    part1()
    parse()
    part2()