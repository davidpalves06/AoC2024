import sys

file = open(sys.argv[1],'r')

positions= []
velocity = []

for line in file.readlines():
    splitted = line.strip().split(" ")
    position = list(map(lambda x:int(x),splitted[0].split("=")[1].split(",")))
    vel = list(map(lambda x:int(x),splitted[1].split("=")[1].split(",")))
    positions.append(position)
    velocity.append(vel)

width = int(sys.argv[2])
height = int(sys.argv[3])

for i in range(100):
    for robot in range(len(positions)):
        robotPos = positions[robot]
        robotVel = velocity[robot]

        robotPos[0] = robotPos[0] + robotVel[0]
        robotPos[1] = robotPos[1] + robotVel[1]
        while robotPos[0] < 0:
            robotPos[0] += width
        while robotPos[0] >= width:
            robotPos[0] -= width
        while robotPos[1] < 0:
            robotPos[1] += height
        while robotPos[1] >= height:
            robotPos[1] -= height 

firstQuadrant = 0
secondQuadrant = 0
thirdQuadrant = 0
fourthQuadrant = 0

widthDivision = width // 2
heightDivision = height // 2

filteredPositions = positions
if width % 2 != 0:
    filteredPositions = [position for position in filteredPositions if position[0] != widthDivision]
if height % 2 != 0:
    filteredPositions = [position for position in filteredPositions if position[1] != heightDivision]

for position in filteredPositions:
    if position[0] <= widthDivision and position[1] <= heightDivision:
        firstQuadrant += 1
    if position[0] >= widthDivision and position[1] <= heightDivision:
        secondQuadrant += 1
    if position[0] <= widthDivision and position[1] >= heightDivision:
        thirdQuadrant += 1
    if position[0] >= widthDivision and position[1] >= heightDivision:
        fourthQuadrant += 1

resPart1 = firstQuadrant * secondQuadrant * thirdQuadrant * fourthQuadrant

print(resPart1)

#Part2

maxArea = 0
area = 0
time = 100

def dfs(i,j):
    global area
    if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
        return

    visited.add((i,j))
    area += 1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)

grid = [[0 for w in range(width)] for h in range(height)]

for position in positions:
    grid[position[1]][position[0]] += 1

for instant in range(101,10000):
    visited = set()
    for robot in range(len(positions)):
        robotPos = positions[robot]
        robotVel = velocity[robot]
        grid[robotPos[1]][robotPos[0]] -= 1
        robotPos[0] = robotPos[0] + robotVel[0]
        robotPos[1] = robotPos[1] + robotVel[1]
        while robotPos[0] < 0:
            robotPos[0] += width
        while robotPos[0] >= width:
            robotPos[0] -= width
        while robotPos[1] < 0:
            robotPos[1] += height
        while robotPos[1] >= height:
            robotPos[1] -= height 
        grid[robotPos[1]][robotPos[0]] += 1

    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0 and (i,j) not in visited:
                dfs(i,j)
                if area > maxArea:
                    print(area,maxArea,instant,time,i,j)
                    maxArea = area
                    time = instant
                area = 0

print(time,maxArea)




