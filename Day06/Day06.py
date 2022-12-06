import re

file = "./Day06/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def part1():
    start = 0
    size = 4
    for x in range(0,len(input[0])-size):
        chars = []
        found = True
        end = start + size
        val = input[0][start:end]
        for x in range(0,len(val)):
            char = val[x]
            if char in chars:
                found = False
                break
            else:
                chars.append(char)
        if found:
            break
        else:
            start = start + 1
    print(f"Answer is: {start + size}")

def part2():
    start = 0
    size = 14
    for x in range(0,len(input[0])-size):
        chars = []
        found = True
        end = start + size
        val = input[0][start:end]
        for x in range(0,len(val)):
            char = val[x]
            if char in chars:
                found = False
                break
            else:
                chars.append(char)
        if found:
            break
        else:
            start = start + 1
    print(f"Answer is: {start + size}")

if __name__ == '__main__':
    parse()
    part1()
    part2()