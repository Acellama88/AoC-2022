import re

file = "./Day10/input.txt"
finalTotal = 0
crtOutput = []
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

def checkP1Results(cycle, value):
    global finalTotal
    if (cycle - 20) % 40 == 0 and cycle <= 220:
        finalTotal += value * cycle

def checkP2Results(cycle, value):
    global crtOutput
    if value - 1 <= ((cycle - 1) % 40) <= value + 1:
        crtOutput.append('#')
    else:
        crtOutput.append('.')

def part1():
    regX = 1
    cycle = 0
    for cmd in input:
        tokens = cmd.split(" ")
        if tokens[0] == 'addx':
            for i in range(0,2):
                cycle = cycle + 1
                checkP1Results(cycle, regX)
            regX += int(tokens[1])
        if tokens[0] == 'noop':
            cycle = cycle + 1
            checkP1Results(cycle, regX)
    print(finalTotal)

def part2():
    regX = 1
    cycle = 0
    for cmd in input:
        tokens = cmd.split(" ")
        if tokens[0] == 'addx':
            for i in range(0,2):
                cycle = cycle + 1
                checkP2Results(cycle, regX)
            regX += int(tokens[1])
        if tokens[0] == 'noop':
            cycle = cycle + 1
            checkP2Results(cycle, regX)
    for i in range(0,240, 40):
        print("".join(crtOutput[i:i+40]))

if __name__ == '__main__':
    parse()
    part1()
    part2()