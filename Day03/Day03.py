import re

file = "./Day03/input.txt"
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

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def part1():
    count = 0
    for x in input:
        length = len(x)
        half = int(length / 2)
        p1 = x[0:half]
        p2 = x[half:length]
        for y in p1:
            if(y in p2):
                count += alphabet.index(y) + 1
                break
    print(count)

def part2():
    count = 0
    for x in range(0,len(input),3):
        Elf1 = input[x]
        Elf2 = input[x+1]
        Elf3 = input[x+2]
        for y in Elf1:
            if(y in Elf2 and y in Elf3):
                count += alphabet.index(y) + 1
                break
    print(count)
    print("")

if __name__ == '__main__':
    parse()
    part1()
    part2()