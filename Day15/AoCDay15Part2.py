import sys

file = open(sys.argv[1],'r')
 

grid = []

line = file.readline()

instructions = []
# Part2
while line != '\n':
    gridLine = []
    for obj in line.strip():
        if obj == '#':
            gridLine.append('#')
            gridLine.append('#')
        if obj == 'O':
            gridLine.append('[')
            gridLine.append(']')
        if obj == '.':
            gridLine.append('.')
            gridLine.append('.')
        if obj == '@':
            gridLine.append('@')
            gridLine.append('.')
    grid.append(gridLine)
    line = file.readline()

while line == '\n':
    line = file.readline()

while line not in ['','\n']:
    for instruction in line.strip():
        instructions.append(instruction)
    line = file.readline()

startingPosition = (0,0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            startingPosition = (i,j)

for line in grid:
    print(line)

def moveBoxRight(x,y):
    firstBoxPosition = (x,y)
    while grid[x][y] in ['[',']']:
        x,y = x + direction[0],y + direction[1]
    if grid[x][y] == '#':
        return False
    else:
        while (x,y) != firstBoxPosition:
            grid[x][y] = grid[x][y-1]
            y = y - direction[1]
    return True

def moveBoxLeft(x,y):
    firstBoxPosition = (x,y)
    while grid[x][y] in ['[',']']:
        x,y = x + direction[0],y + direction[1]
    if grid[x][y] == '#':
        return False
    else:
        while (x,y) != firstBoxPosition:
            grid[x][y] = grid[x][y+1]
            y = y - direction[1]
    return True

def checkIfBoxUp(x,leftWall,rightWall):
    if grid[x][leftWall] in ['[',']']:
        if grid[x][leftWall] == '[':
            if not checkIfBoxUp(x-1,leftWall,leftWall+1):
                return False
        else:
            if not checkIfBoxUp(x-1,leftWall-1,leftWall):
                return False
    if grid[x][rightWall] == '[':
        if not checkIfBoxUp(x-1,rightWall,rightWall+1):
            return False
    
    if grid[x][leftWall] == '#' or grid[x][rightWall] == '#':
        return False

    return True

def moveBoxUp(x,leftWall,rightWall):
    if grid[x][leftWall] in ['[',']']:
        if grid[x][leftWall] == '[':
            moveBoxUp(x-1,leftWall,leftWall + 1)
        else:
            moveBoxUp(x-1,leftWall-1,leftWall)
    if grid[x][rightWall] == '[':
        moveBoxUp(x-1,rightWall,rightWall + 1)
    
    grid[x+1][leftWall],grid[x+1][rightWall] = '.','.'
    grid[x][leftWall],grid[x][rightWall] = '[',']'
    return True

def checkIfBoxDown(x,leftWall,rightWall):
    if grid[x][leftWall] in ['[',']']:
        if grid[x][leftWall] == '[':
            if not checkIfBoxDown(x+1,leftWall,leftWall+1):
                return False
        else:
            if not checkIfBoxDown(x+1,leftWall-1,leftWall):
                return False
    if grid[x][rightWall] == '[':
        if not checkIfBoxDown(x+1,rightWall,rightWall+1):
            return False
    
    if grid[x][leftWall] == '#' or grid[x][rightWall] == '#':
        return False

    return True

def moveBoxDown(x,leftWall,rightWall):
    if grid[x][leftWall] in ['[',']']:
        if grid[x][leftWall] == '[':
            moveBoxDown(x+1,leftWall,leftWall + 1)
        else:
            moveBoxDown(x+1,leftWall-1,leftWall)
    if grid[x][rightWall] == '[':
        moveBoxDown(x+1,rightWall,rightWall + 1)
    
    grid[x-1][leftWall],grid[x-1][rightWall] = '.','.'
    grid[x][leftWall],grid[x][rightWall] = '[',']'
    return True


def moveRobot(position,direction):
    x,y = (position[0] + direction[0],position[1] + direction[1])
    if grid[x][y] == '#':
        return position
    
    if grid[x][y] == '[':
        if direction == (0,1):
            if not moveBoxRight(x,y):
                return position
        elif direction == (-1,0):
            rightWallState = grid[position[0]][position[1]+1]
            if checkIfBoxUp(x,y,y+1) and moveBoxUp(x,y,y+1):
                grid[x][y] = '@'
                grid[x][y+1] = '.'
                grid[position[0]][position[1]] = '.'
                grid[position[0]][position[1]+1] = rightWallState
                return (x,y)
            else:
                return position
        elif direction == (1,0):
            rightWallState = grid[position[0]][position[1]+1]
            if checkIfBoxDown(x,y,y+1) and moveBoxDown(x,y,y+1):
                grid[x][y] = '@'
                grid[x][y+1] = '.'
                grid[position[0]][position[1]] = '.'
                grid[position[0]][position[1] + 1] = rightWallState
                return (x,y)
            else:
                return position
    elif grid[x][y] == ']':
        if direction == (0,-1):
            if not moveBoxLeft(x,y):
                return position
        elif direction == (-1,0):
            leftWallState = grid[position[0]][position[1]-1]
            if checkIfBoxUp(x,y-1,y) and moveBoxUp(x,y-1,y):
                grid[x][y] = '@'
                grid[x][y-1] = '.'
                grid[position[0]][position[1]] = '.'
                grid[position[0]][position[1]-1] = leftWallState
                return (x,y)
            else:
                return position
        elif direction == (1,0):
            leftWallState = grid[position[0]][position[1]-1]
            if checkIfBoxDown(x,y-1,y) and moveBoxDown(x,y-1,y):
                grid[x][y] = '@'
                grid[x][y-1] = '.'
                grid[position[0]][position[1]] = '.'
                grid[position[0]][position[1]-1] = leftWallState
                return (x,y)
            else:
                return position
        else:
            return position

    grid[position[0]][position[1]] = '.'
    grid[x][y] = '@'
    return (x,y)

currentPosition = startingPosition

for instruction in instructions:
    direction = (1,0)
    if instruction == '^':
        direction = (-1,0)
    if instruction == '>':
        direction = (0,1)
    if instruction == 'v':
        direction = (1,0)
    if instruction == '<':
        direction = (0,-1)

    currentPosition = moveRobot(currentPosition,direction)

for line in grid:
    print(line)

resPart2 = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[' and grid[i][j+1] == ']':
            gpsCoord = 100 * i + j
            resPart2 += gpsCoord

print(resPart2)        
