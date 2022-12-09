import re

file = "./Day09/input.txt"
finalTotal = 0
input = []
hx = 0
hy = 0
tx = 0
ty = 0
locations = {}

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def checkDist(hx, hy, tx, ty):
    distX = abs(hx - tx)
    distY = abs(hy - ty)
    if (distX >= 2) or (distY >= 2):
        return True
    return False


def part1():
    global hx, hy, tx, ty
    locations[(tx,ty)] = 0
    for x in input:
        token = x.split(" ")
        for i in range(0,int(token[1])):
            lastx = hx
            lasty = hy
            if token[0] == 'L':
                hx = hx -1
            elif token[0] == 'R':
                hx = hx +1
            if token[0] == 'D':
                hy = hy -1
            elif token[0] == 'U':
                hy = hy +1
            if checkDist():
                tx = lastx
                ty = lasty
            locations[(tx,ty)] = 0
    print(len(locations))

def part2():
    knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    locations[(knots[9][0],knots[9][1])] = 0
    nextX = 0
    nextY = 0
    for x in input:
        token = x.split(" ")
        for i in range(0,int(token[1])):
                lastx = knots[0][0]
                lasty = knots[0][1]
                if token[0] == 'L':
                    knots[0][0] = knots[0][0] -1
                elif token[0] == 'R':
                    knots[0][0] = knots[0][0] +1
                elif token[0] == 'D':
                    knots[0][1] = knots[0][1] -1
                elif token[0] == 'U':
                    knots[0][1] = knots[0][1] +1
                for a in range(0,len(knots)):
                    if(a < len(knots) - 1):
                        nextX = knots[a+1][0]
                        nextY = knots[a+1][1]
                    else:
                        break
                    if checkDist(knots[a][0], knots[a][1], knots[a+1][0], knots[a+1][1]):
                        nextX = knots[a+1][0]
                        nextY = knots[a+1][1]
                        knots[a+1][0] = lastx
                        knots[a+1][1] = lasty
                        lastx = nextX
                        lasty = nextY
                locations[(knots[9][0],knots[9][1])] = 0
        print(knots)
    print(len(locations))

if __name__ == '__main__':
    parse()
    part2()