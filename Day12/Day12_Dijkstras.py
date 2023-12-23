import re
import heapq

file = "./Day12/input.txt"
maxX = 0
maxY = 0
input = []
visited = {}
queue = []
start = [0,0]

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
    global maxX, maxY, input, start
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
            if element == 'S':
                start = [x,y]
                return

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
        value = 26 #found E
    return value

def run():
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
            return curNode.dist

def genMap():
    global maxX, maxY, input
    output = [ [0]*maxY for i in range(maxX)]
    for x, line in enumerate(input):
        for y, element in enumerate(line):
            key = f'{x},{y},{element}'
            if key in visited:
                node = visited[key]
                output[x][y] = node
            else:
                output[x][y] = element
    for line in output:
        print(line)

def part1():
    newNode = node(start[0],start[1],0)
    heapq.heappush(queue, newNode)
    value = run()
    print(f"Distance: {value}")
    #genMap()

def part2():
    global queue, visited
    bestscore = 1000000
    for x, line in enumerate(input):
        for y, element in enumerate(line):
            if element == 'a':
                queue = []
                visited = {}
                newNode = node(x,y,0)
                heapq.heappush(queue,newNode)
                value = run()
                if value != None and value < bestscore:
                    bestscore = value
    print(f"Distance: {bestscore}")

if __name__ == '__main__':
    parse()
    part1()
    part2()