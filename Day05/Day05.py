import re

file = "./Day05/input.txt"
finalTotal = 0
input = []

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []
a9 = []
stacks = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
                input.remove("")
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def init():
    global stacks, a1, a2, a3, a4, a5, a6, a7, a8, a9
    a1 = ['F', 'C', 'P', 'G', 'Q', 'R']
    a2 = ['W', 'T', 'C', 'P']
    a3 = ['B', 'H', 'P', 'M', 'C']
    a4 = ['L', 'T', 'Q', 'S', 'M', 'P', 'R']
    a5 = ['P', 'H', 'J', 'Z', 'V', 'G', 'N']
    a6 = ['D', 'P', 'J']
    a7 = ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R']
    a8 = ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J']
    a9 = ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']
    stacks = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

def part1():
    for x in input:
        tokens = re.split(" ",x)
        for i in range(0,int(tokens[1])):
            val = stacks[int(tokens[3])-1].pop()
            stacks[int(tokens[5])-1].append(val)
    ret = ""
    for x in stacks:
        ret += x[-1]
    print(ret)

def part2():
    temp = []
    for x in input:
        tokens = re.split(" ",x)
        for i in range(0,int(tokens[1])):
            temp.append(stacks[int(tokens[3])-1].pop())
        for i in range(0,int(tokens[1])):
            stacks[int(tokens[5])-1].append(temp.pop())
    ret = ""
    for x in stacks:
        ret += x[-1]
    print(ret)

if __name__ == '__main__':
    parse()
    init()
    part1()
    init()
    part2()