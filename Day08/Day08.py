import re

file = "./Day08/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            newLine = []
            for x in line:
                if(x == '\n'):
                    break
                newLine.append(int(x))
            input.append(newLine)

def part1():
    count = 0
    for x in range(1,len(input)-1):
        for y in range(1,len(input[0])-1):
            found = False
            height = input[x][y]
            for locX in range(0,x):
                if input[locX][y] >= height:
                    found = True
                    break
            if not found:
                count = count + 1
                continue
            else:
                found = False
            for locX in range(x+1,len(input)):
                if input[locX][y] >= height:
                    found = True
                    break
            if not found:
                count = count + 1
                continue
            else:
                found = False
            for locY in range(0,y):
                if input[x][locY] >= height:
                    found = True
                    break
            if not found:
                count = count + 1
                continue
            else:
                found = False
            for locY in range(y+1,len(input[0])):
                if input[x][locY] >= height:
                    found = True
                    break
            if not found:
                count = count + 1
                continue
    print(count + len(input) * 2 + len(input[0]) * 2 - 4)

def part2():
    score = 0
    highscore = 0
    for x in range(1,len(input)-1):
        for y in range(1,len(input[0])-1):
            height = input[x][y]
            up = 0
            down = 0
            left = 0
            right = 0
            for locX in range(x-1,-1,-1): #up
                up = up + 1
                if input[locX][y] >= height:
                    break
            for locX in range(x+1,len(input)): #down
                down = down +1
                if input[locX][y] >= height:
                    break
            for locY in range(y-1,-1, -1): #left
                left = left +1
                if input[x][locY] >= height:
                    break
            for locY in range(y+1,len(input[0])): #right
                right = right +1
                if input[x][locY] >= height:
                    break
            score = up * down * left * right
            #print(f"[{x}][{y}] Up: {up} Down {down} Left {left} Right {right} Score {score}")
            if score > highscore:
                highscore = score
    print(highscore)

if __name__ == '__main__':
    parse()
    part1()
    part2()