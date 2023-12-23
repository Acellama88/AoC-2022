import re

file = "./Day15/input.txt"
finalTotal = 0
part1Row = 2000000
input = []
result = {}
result2 = []

def parse():
    with open(file) as f:
        for line in f:
            if True:
                tokens = re.split(" |=|,|:",line.strip())
                input.append([[int(tokens[3]),int(tokens[6])],[int(tokens[13]),int(tokens[16])]])
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def calcManhatten(x1, y1, x2, y2):
    xCount = abs(x1 - x2)
    yCount = abs(y1 - y2)
    return xCount + yCount

def part1():
    global result
    for pair in input:
        sX = pair[0][0]
        sY = pair[0][1]
        bX = pair[1][0]
        bY = pair[1][1]
        radius = calcManhatten(sX, sY, bX, bY)

        if abs(sY - part1Row) > radius:
            continue #Not close enough to target
        rowDiff = abs(sY - part1Row)
        startX = sX - radius + rowDiff
        endX = sX + radius - rowDiff
        for x in range(startX, endX):
            result[(x)] = 0
    print(len(result))

def sortRow(value):
    return value[0]

def calcRow(xStart, xEnd, y):
    global result2
    if(y >= 4000000) or y < 0:
        return
    rowData = result2[y]
    xS = max(xStart, 0)
    xE = min(xEnd,4000000)
    if rowData == []:
        rowData.append([xStart,xEnd])
        return
    temp = []
    for set in rowData:
        if set[1] < xS: #ends before we begin
            temp.append(set)
        elif xE < set[0]: #starts after we end
            temp.append(set)
        elif xS <= set[0] <= set[1] <= xE: #the set is completely included, remove
            continue
        elif xS <= set[0] <= xE: #only start of set is inside our range
            xE = set[1]
        elif xS <= set[1] <= xE: #only end of set is inside our range
            xS = set[0]
    temp.append([xS,xE])
    temp.sort(key = sortRow)
    i = 0
    while i < len(temp) - 1:
        if temp[i][1] == (temp[i+1][0] - 1): #side by side elements
            temp[i][1] = temp[i+1][1]
            temp.pop(i+1)
        else:
            i = i + 1
    result2[y] = temp

def part2():
    global result2
    result2 = [ [] ] * 4000000
    for count,pair in enumerate(input):
        print(f"Completed: {count}")
        sX = pair[0][0]
        sY = pair[0][1]
        bX = pair[1][0]
        bY = pair[1][1]
        radius = calcManhatten(sX, sY, bX, bY)

        for yRow in range(sY - radius, sY + radius):
            rowDiff = abs(sY - yRow)
            startX = sX - radius + rowDiff
            endX = sX + radius - rowDiff
            calcRow(startX, endX, yRow)

    for row,item in enumerate(result2):
        if len(item) >= 2 and item[0][0] == 0 and item[-1][1] == 4000000 and item[0][1] + 5 > item[-1][0]:
            print(f"Row: {row} - {item}")

if __name__ == '__main__':
    parse()
    part1()
    part2()