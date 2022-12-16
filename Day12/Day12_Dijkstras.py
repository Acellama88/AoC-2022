import re
import heapq

file = "./Day12/input.txt"
maxX = 0
maxY = 0
input = []
visited = {}
queue = []

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
    global maxX, maxY, input
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

def checkInQueue(x, y):
    global queue
    for val in queue:
        if val.x == x and val.y == y:
            return queue.index(val)
    return -1

def addNode(x, y, dist):
    global visited
    newNode = node(x, y, dist)
    key = newNode.getKey()
    if key in visited:
        return
    loc = checkInQueue(x, y)
    if loc >= 0:
        if queue[loc].dist > dist:
            queue[loc].dist = dist
    else:
        heapq.heappush(queue, newNode)

def getElev(value):
    value = ord(value) - 96
    if value < 0:
        value = 27 #found E
    return value

def start():
    global maxX, maxY, input, queue, visited
    while len(queue) > 0:
        queue.sort(key = sortQ)
        curNode = heapq.heappop(queue)
        if(curNode.x > 0) and (getElev(input[curNode.x-1][curNode.y]) <= curNode.elev + 1):
            addNode(curNode.x - 1, curNode.y, curNode.dist + 1)
        if(curNode.x < maxX - 1) and (getElev(input[curNode.x+1][curNode.y]) <= curNode.elev + 1):
            addNode(curNode.x + 1, curNode.y, curNode.dist + 1)
        if(curNode.y > 0) and (getElev(input[curNode.x][curNode.y-1]) <= curNode.elev + 1):
            addNode(curNode.x, curNode.y - 1, curNode.dist + 1)
        if(curNode.y < maxY - 1) and (getElev(input[curNode.x][curNode.y+1]) <= curNode.elev + 1):
            addNode(curNode.x, curNode.y + 1, curNode.dist + 1)
        visited[curNode.getKey()] = curNode.dist
        if (input[curNode.x][curNode.y] == 'E'):
            print(f"Distance: {curNode.dist}")

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