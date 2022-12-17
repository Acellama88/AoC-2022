import re
from PIL import Image
#py -m pip install pillow

file = "./Day14/input.txt"
input = []
minX = 10000
maxX = 0
maxY = 0
numSand = 0
array = []
images = []

def parse1():
    global minX, maxX, maxY, array, input
    with open(file) as f:
        for line in f:
            tokens = list(filter(None, re.split(" |->|\n",line)))
            for x,token in enumerate(tokens):
                temp = re.split(",",token)
                tokens[x] = [int(temp[0]),int(temp[1])]
            input.append(tokens)
    for line in input:
        for node in line:
            if node[0] < minX:
                minX = node[0]
            if node[0] > maxX:
                maxX = node[0]
            if node[1] > maxY:
                maxY = node[1]
    array = [ [' ']*(maxX - minX + 1) for i in range(maxY + 1)]
    for line in input:
        for loc in range(0,len(line)-1):
            start = line[loc]
            end = line[loc+1]
            if(start[0] > end[0]):
                y = start[1]
                for x in range(start[0] - end[0] + 1):
                    loc = x + end[0] - minX
                    array[y][loc] = '#'
            elif(start[0] < end[0]):
                y = start[1]
                for x in range(end[0] - start[0] + 1):
                    loc = x + start[0] - minX
                    array[y][loc] = '#'
            elif(start[1] > end[1]):
                x = start[0] - minX
                for y in range(start[1] - end[1] + 1):
                    loc = y + end[1]
                    array[loc][x] = '#'
            elif(start[1] < end[1]):
                x = start[0] - minX
                for y in range(end[1] - start[1] + 1):
                    loc = y + start[1]
                    array[loc][x] = '#'


def parse2():
    global minX, maxX, maxY, array, input
    with open(file) as f:
        for line in f:
            tokens = list(filter(None, re.split(" |->|\n",line)))
            for x,token in enumerate(tokens):
                temp = re.split(",",token)
                tokens[x] = [int(temp[0]),int(temp[1])]
            input.append(tokens)
    for line in input:
        for node in line:
            if node[0] < minX:
                minX = node[0]
            if node[0] > maxX:
                maxX = node[0]
            if node[1] > maxY:
                maxY = node[1]
    input.append([[0,maxY + 2],[(maxX * 2) - 5,maxY+2]])
    array = [ [' ']*(maxX * 2) for i in range(maxY + 4)]
    for line in input:
        for loc in range(0,len(line)-1):
            start = line[loc]
            end = line[loc+1]
            if(start[0] > end[0]):
                y = start[1]
                for x in range(start[0] - end[0] + 1):
                    loc = x + end[0]
                    array[y][loc] = '#'
            elif(start[0] < end[0]):
                y = start[1]
                for x in range(end[0] - start[0] + 1):
                    loc = x + start[0]
                    array[y][loc] = '#'
            elif(start[1] > end[1]):
                x = start[0]
                for y in range(start[1] - end[1] + 1):
                    loc = y + end[1]
                    array[loc][x] = '#'
            elif(start[1] < end[1]):
                x = start[0]
                for y in range(end[1] - start[1] + 1):
                    loc = y + start[1]
                    array[loc][x] = '#'

def printArr():
    global array
    for line in array:
        print(line)
    print("\n")

def imageGen():
    global maxX, maxY, array, numSand
    if ((numSand % 10) == 0 and numSand < 1000) or ((numSand % 200) == 0 and numSand >= 1000):
        totalX = maxY * 2 + 30
        offset = 500 - (maxY + 15)
        img = Image.new('RGB',(totalX, maxY), "black")
        pixels=img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if(array[y][x+offset] == "#"):
                    pixels[x,y] = (255, 255, 255)
                elif(array[y][x+offset] == "o"):
                    pixels[x,y] = (129,89,1)
        img = img.resize((maxX * 2, maxY * 2), Image.Resampling.BILINEAR)
        images.append(img)
    if(numSand % 1000) == 0:
        print (f"{numSand} Complete")

def imageCreate():    
    images[0].save('image2x_2.gif', save_all=True, append_images=images[1:], optimize=False, duration=1, loop=0)

def part1():
    global array, numSand
    startX = 500 - minX
    startY = 0
    sand = [startX, startY]
    while(sand[1] < maxY):
        down = array[sand[1]+1][sand[0]]
        downLeft = array[sand[1]+1][sand[0]-1]
        downRight = array[sand[1]+1][sand[0]+1]

        if down == '#' or down == 'o':
            if downLeft == '#' or downLeft == 'o':
                if downRight == '#' or downRight == 'o':
                    array[sand[1]][sand[0]] = 'o'
                    sand = [startX, startY]
                    numSand = numSand + 1
                else:
                    sand[1] = sand[1] + 1
                    sand[0] = sand[0] + 1
            else:
                sand[1] = sand[1] + 1
                sand[0] = sand[0] - 1
        else:
            sand[1] = sand[1] + 1 
    print(numSand)

def part2():
    global array, numSand
    numSand = 0
    startX = 500
    startY = 0
    sand = [startX, startY]
    while True:
        down = array[sand[1]+1][sand[0]]
        downLeft = array[sand[1]+1][sand[0]-1]
        downRight = array[sand[1]+1][sand[0]+1]

        if sand[0] == startX and sand[1] == startY and down == 'o' and downLeft == 'o' and downRight == 'o':
            numSand = numSand + 1
            break
        if down == '#' or down == 'o':
            if downLeft == '#' or downLeft == 'o':
                if downRight == '#' or downRight == 'o':
                    array[sand[1]][sand[0]] = 'o'
                    sand = [startX, startY]
                    numSand = numSand + 1
                    imageGen()
                else:
                    sand[1] = sand[1] + 1
                    sand[0] = sand[0] + 1
            else:
                sand[1] = sand[1] + 1
                sand[0] = sand[0] - 1
        else:
            sand[1] = sand[1] + 1 
    imageCreate()
    print(numSand)

if __name__ == '__main__':
    parse1()
    part1()
    parse2()
    part2()