import re

inputfile = "./Day07/input.txt"
finalTotal = 0
smallest = 100000000000
smallestName = ''
largerThan = 0
input = []

allDirs = []

class dir:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.size = 0
        self.dirs = []
        self.files = []
    parent = []
    name = 'Name'
    size = 0
    dirs = []
    files = []

class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    name = 'Name'
    size = 0

filesystem = dir("/")

def parse():
    with open(inputfile) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def buildFilesystem():
    for x in input:
        tokens = re.split(" ",x)
        if tokens[1] == 'cd':
            if x == '$ cd /':
                location = filesystem
            elif '..' in x:
                location = location.parent
            else:
                tokens = x.split(" ")
                for y in location.dirs:
                    if tokens[2] == y.name:
                        location = y
                        break
        elif tokens[1] == 'ls':
            continue
        elif tokens[0] == 'dir':
            tokens = re.split(" ", x)
            newLoc = dir(tokens[1])
            newLoc.parent = location
            location.dirs.append(newLoc)
        else:
            tokens = re.split(" ", x)
            location.files.append(file(tokens[1], tokens[0]))
            tempLoc = location
            while(tempLoc.name != '/'):
                tempLoc.size += int(tokens[0])
                tempLoc = tempLoc.parent
            filesystem.size += int(tokens[0])
    
def calcSize(directory):
    global finalTotal
    for x in directory.dirs:
        calcSize(x)
    if directory.size <= 100000:
        finalTotal += directory.size

def findSmallest(directory):
    global smallest, smallestName
    for x in directory.dirs:
        findSmallest(x)
    if directory.size <= smallest and directory.size >= largerThan:
        smallest = directory.size
        smallestName = directory.name

def part1():
    calcSize(filesystem)
    print(finalTotal)

def part2():
    global largerThan
    freeTotal = 70000000 - filesystem.size
    largerThan = 30000000 - freeTotal
    findSmallest(filesystem)
    print(f"Smallest: {smallestName} {smallest}")

if __name__ == '__main__':
    parse()
    buildFilesystem()
    part1()
    part2()
