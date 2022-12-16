import re
import heapq

file = "./Day12/input.txt"
maxX = 0
maxY = 0
input = []
visited = {}
queue = []
end = [0,0]

class node:
    def __init__(self, X, Y, Dist):
        self.x = X
        self.y = Y
        self.elev = getElev(input[self.x][self.y])
        self.dist = Dist
    def getKey(self):
        return f"{self.x},{self.y},{input[self.x][self.y]}"
    def __lt__(self, other):
        return self.dist < other.dist
    x = -1
    y = -1
    elev = -1
    dist = 10000000

def sortQ(value: node):
    return value.dist

def parse():
    global maxX, maxY, input, end
    with open(file) as f:
        for line in f:
            if True:
                newLine = []
                newLine.extend(line.strip())
                input.append(newLine)
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())
    maxX = len(input)
    maxY = len(input[0])
    for x, line in enumerate(input):
        for y, element in enumerate(line):
            if element == 'E':
                end = [x,y]
                return
                

def distance(x,y):
    return abs(end[0] - x) + abs(end[1]-y)

def isXFirst(x,y):
    return abs(end[0] - x) >= abs(end[1]-y)

def getElev(value):
    value = ord(value) - 96
    if value < 0:
        value = 26 #found E
    return value

def start():

def part1():
    newNode = node(0,0,0)
    heapq.heappush(queue, newNode)
    start()

def part2():
    print("")

if __name__ == '__main__':
    parse()
    part1()
    part2()