import re

file = "./Day01/input.txt"
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
    total = 0
    for x in input:
        if(x == ''):
            if(total > count):
                count = total
            total = 0
        else:
            total = total + int(x)
    print(count)

def part2():
    input.append('')
    count = [0,0,0]
    total = 0
    for x in input:
        if(x == ''):
            count.append(total)
            count.sort(reverse=True)
            count.pop()
            total = 0
        else:
            total = total + int(x)
    print(count[0] + count[1] + count[2])

if __name__ == '__main__':
    parse()
    part1()
    part2()