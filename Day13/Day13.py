import re

file = "./Day13/input.txt"
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
                if(line == "\n"):
                    continue
                input.append(line.strip())

def getValues(left, right):
    return [eval(left), eval(right)]

def compare(left, right):
    if(isinstance(left, int) and isinstance(right,int)):
        return right - left
    
    if(isinstance(left,int)):
        left = [left]
    if(isinstance(right,int)):
        right = [right]

    for x in range(min(len(left), len(right))):
        retVal = compare(left[x],right[x])
        if retVal != 0:
            return retVal
    
    return len(right) - len(left)

def part1():
    global finalTotal, input
    for x in range(0,len(input),2):
        values = getValues(input[x], input[x+1])
        if compare(values[0], values[1]) > 0:
            finalTotal = finalTotal + ((x / 2) + 1)
    print(f"Result Part1: {int(finalTotal)}")

def part2():
    global input
    input.append("[[2]]")
    input.append("[[6]]")
    didWork = True
    while(didWork):
        didWork = False
        sortArr = [input[0]]
        for x in range(1,len(input)):
            values = getValues(sortArr[x-1], input[x])
            if compare(values[0], values[1]) > 0:
                sortArr.append(input[x])
            else:
                didWork = True
                temp = sortArr[x-1]
                sortArr[x-1] = input[x]
                sortArr.append(temp)
        input = sortArr
    pack2 = 0
    pack6 = 0
    for x in range(len(input)):
        if input[x] == '[[2]]':
            pack2 = x+1
        if input[x] == '[[6]]':
            pack6 = x+1
    print(f"Result Part2: {pack2 * pack6}")
            

if __name__ == '__main__':
    parse()
    part1()
    part2()