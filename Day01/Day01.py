import re

file = "./Day1/input.txt"
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
    count = 0
    last = input[0]
    for x in input:
        if last < x:
            count = count + 1
        last = x

    print(count)

def part2():
    count = 0
    last = input[0]
    for x in range(0,len(input)-3):
        comp1 = input[x] + input[x+1] + input[x+2]
        comp2 = input[x+1] + input[x+2] + input[x+3]
        if(comp2 > comp1):
            count = count + 1
    print(count)

if __name__ == '__main__':
    parse()
    part1()
    part2()