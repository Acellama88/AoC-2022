import re
import heapq

file = "./Day12/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if True:
                newLine = []
                newLine.extend(line.strip())
                input.append(newLine)
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def part1():
    print("")

def part2():
    print("")

if __name__ == '__main__':
    parse()
    part1()
    part2()