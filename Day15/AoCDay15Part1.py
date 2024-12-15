import sys

file = open(sys.argv[1],'r')
 

grid = []

line = file.readline()

instructions = []
# Part1
while line != '\n':
    grid.append(list(line.strip()))
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

def moveRobot(position,direction):
    x,y = (position[0] + direction[0],position[1] + direction[1])
    if grid[x][y] == '#':
        return position
    
    if grid[x][y] == 'O':
        firstBoxPosition = (x,y)
        while grid[x][y] == 'O':
            x,y = x + direction[0],y + direction[1]
        if grid[x][y] == '#':
            return position
        else:
            while (x,y) != firstBoxPosition:
                grid[x][y] = 'O'
                x,y = x - direction[0],y - direction[1]
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

resPart1 = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            gpsCoord = 100 * i + j
            resPart1 += gpsCoord

print(resPart1)        
