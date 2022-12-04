import re

file = "./Day04/input.txt"
finalTotal = 0
input = []

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

def part1():
    count = 0
    for pair in input:
        tokens = re.split(",|-",pair.strip())
        a1 = int(tokens[0])
        a2 = int(tokens[1])
        b1 = int(tokens[2])
        b2 = int(tokens[3])
        if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
            count += 1
    print(count)

def part2():
    count = 0
    for pair in input:
        tokens = re.split(",|-",pair.strip())
        a1 = int(tokens[0])
        a2 = int(tokens[1])
        b1 = int(tokens[2])
        b2 = int(tokens[3])
        if (a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2) or (a2 >= b1 and a2 <= b2) or (b2 >= a1 and b2 <= a2):
            count += 1
    print(count)

if __name__ == '__main__':
    parse()
    part1()
    part2()