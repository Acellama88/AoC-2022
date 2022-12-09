import re

file = "./Day09/input.txt"
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

def performMove(head, tail):
    hx = head[0]
    hy = head[1]
    tx = tail[0]
    ty = tail[1]

    #They are already touching
    if (abs(hx-tx) <= 1 and abs(hy-ty) <= 1):
        return tail
    if (hx == tx): #same X axis
        move = (hy - ty) / 2
        ty = ty + move
    elif (hy == ty): #same Y axis
        move = (hx - tx) / 2
        tx = tx + move
    else: #Move Diagonal Closer
        moveX = (hx - tx) / abs((hx - tx))
        moveY = (hy - ty) / abs((hy - ty))
        tx = tx + moveX
        ty = ty + moveY
    return [tx, ty]

def part1():
    head = [0,0]
    tail = [0,0]
    locations = {}
    locations[(0,0)] = 0
    for x in input:
        token = x.split(" ")
        for i in range(0,int(token[1])):
            if token[0] == 'L':
                head[0] = head[0] -1
            elif token[0] == 'R':
                head[0] = head[0] +1
            if token[0] == 'D':
                head[1] = head[1] -1
            elif token[0] == 'U':
                head[1] = head[1] +1
            tail = performMove(head, tail)
            locations[(tail[0], tail[1])] = 0
    print(len(locations))

def part2():
    knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    locations = {}
    locations[(0,0)] = 0
    for x in input:
        token = x.split(" ")
        for i in range(0,int(token[1])):
            if token[0] == 'L':
                knots[0][0] = knots[0][0] -1
            elif token[0] == 'R':
                knots[0][0] = knots[0][0] +1
            elif token[0] == 'D':
                knots[0][1] = knots[0][1] -1
            elif token[0] == 'U':
                knots[0][1] = knots[0][1] +1
            for a in range(0,len(knots)-1):
                res = performMove(knots[a], knots[a+1])
                if (res != knots[a+1]):
                    knots[a+1] = res
                else:
                    break    
            locations[(knots[9][0], knots[9][1])] = 0
    print(len(locations))

if __name__ == '__main__':
    parse()
    part1()
    part2()