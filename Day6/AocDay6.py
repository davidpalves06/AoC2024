import sys

inputName = sys.argv[1]

file = open(inputName,'r')

map = []
row = 0
startingPosition = (0,0)
for line in file.readlines():
    currentRow = []
    for i in range(len(line.strip())):
        if line[i] not in ['.','#']:
            startingPosition = (row,i)
        currentRow.append(line[i])
    row += 1
    map.append(currentRow)

directionMap = {
    '^':(-1,0),
    '>':(0,1),
    'v':(1,0),
    '<':(0,-1)
}

inMap = True
resPart1 = 1

def rotate(position):
    if position == '^':
        return '>'
    if position == '>':
        return 'v'
    if position == 'v':
        return '<'
    if position == '<':
        return '^'
    
x,y = startingPosition
while inMap:
    dx,dy = directionMap[map[x][y]]
    if x + dx < 0 or x + dx >= len(map) or y + dy < 0 or y + dy >= len(map[0]):
        map[x][y] = 'X'
        inMap = False
    elif map[x+dx][y+dy] == '#':
        map[x][y] = rotate(map[x][y])
    else:
        if map[x+dx][y+dy] != 'X':
            resPart1 += 1
        map[x + dx][y + dy] = map[x][y]
        map[x][y] = 'X'
        x,y = x+dx,y+dy

print(resPart1)

## Part 2
resPart2 = 0


def checkForLoops(i,j):
    map[i][j] = '#'
    visited = set()
    x,y = startingPosition
    checking = True
    res = True
    while checking:
        dx,dy = directionMap[map[x][y]]
        if x + dx < 0 or x + dx >= len(map) or y + dy < 0 or y + dy >= len(map[0]):
            map[x][y] = 'X'
            checking = False
            res = False
        elif (x,y,dx,dy) in visited:
            map[x][y] = 'X'
            checking = False
            res = True
        elif map[x+dx][y+dy] == '#':
            map[x][y] = rotate(map[x][y])
        else:
            visited.add((x,y,dx,dy))
            map[x + dx][y + dy] = map[x][y]
            map[x][y] = 'X'
            x,y = x+dx,y+dy

    map[i][j] = 'X'
    return res

for i in range(len(map)):
    for j in range(len(map[0])):
        map[startingPosition[0]][startingPosition[1]] = '^'
        if map[i][j] != 'X' or (i,j) == startingPosition:
            continue
        elif checkForLoops(i,j):
            resPart2 += 1
            
print(resPart2)
    
