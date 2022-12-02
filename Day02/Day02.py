import re

file = "./Day02/input.txt"
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
    count= 0
    #A X Rock
    #B Y Paper
    #C Z Scissors
    for x in input:
        if(x[0] == 'A' and x[2] == "X") or (x[0] == 'B' and x[2] == "Y") or (x[0] == 'C' and x[2] == "Z"):
            #draw
            count += 3
        if(x[0] == 'A' and x[2] == "Y") or (x[0] == 'B' and x[2] == "Z") or (x[0] == 'C' and x[2] == "X"):
            #win
            count += 6
        if(x[2] == 'X'):
            count += 1
        if(x[2] == 'Y'):
            count += 2
        if(x[2] == 'Z'):
            count += 3
    print(count)

def part2():
    count= 0
    #A Rock
    #B Paper
    #C Scissors

    #X Lose
    #Y Draw
    #Z Win
    for x in input:
        if(x[2] == 'X'):
            count += 0
            if(x[0] == 'A'):
                count += 3
            if(x[0] == 'B'):
                count += 1
            if(x[0] == 'C'):
                count += 2
        if(x[2] == 'Y'):
            count += 3
            if(x[0] == 'A'):
                count += 1
            if(x[0] == 'B'):
                count += 2
            if(x[0] == 'C'):
                count += 3
        if(x[2] == 'Z'):
            count += 6
            if(x[0] == 'A'):
                count += 2
            if(x[0] == 'B'):
                count += 3
            if(x[0] == 'C'):
                count += 1
    print(count)

if __name__ == '__main__':
    parse()
    part1()
    part2()