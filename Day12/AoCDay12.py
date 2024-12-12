from collections import defaultdict
import sys

file = open(sys.argv[1],'r')

grid = []

for line in file.readlines():
    grid.append(list(line.strip()))

#Part 1
visited = set()
area = 0
perimeter = 0

def dfs(i,j,plantType):
    global area,perimeter
    if (i,j) in visited:
        if grid[i][j] != plantType:
            perimeter += 1
        return
    if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] != plantType:
        perimeter += 1
    else:
        visited.add((i,j))
        area += 1
        dfs(i+1,j,plantType)
        dfs(i-1,j,plantType)
        dfs(i,j+1,plantType)
        dfs(i,j-1,plantType)

resPart1 = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in visited:
            plantType = grid[i][j]
            dfs(i,j,grid[i][j])
            resPart1 += (area * perimeter)
            area = 0
            perimeter = 0

print(resPart1)

# Part2

sides = 0

visited = set()

def dfsPart2(i,j,plantType):
    global area,sides
    if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] != plantType or (i,j) in visited:
        return
    else:
        visited.add((i,j))
        area += 1

        #TOP CORNER RIGHT AND LEFT SIDE
        if (i - 1 < 0 or grid[i-1][j] != plantType) and (j-1 < 0 or grid[i][j-1] != plantType):
            sides += 1
        if (i - 1 < 0 or grid[i-1][j] != plantType) and (j+1 >= len(grid[0]) or grid[i][j+1] != plantType):
            sides += 1

        #BOTTOM CORNER RIGHT AND LEFT SIDE
        if (i + 1 >= len(grid) or grid[i+1][j] != plantType) and (j-1 < 0 or grid[i][j-1] != plantType):
            sides += 1
        if (i + 1 >= len(grid) or grid[i+1][j] != plantType) and (j+1 >= len(grid[0]) or grid[i][j+1] != plantType):
            sides += 1

        #INTERIOR TOP CORNER RIGHT AND LEFT
        if (i-1 >= 0 and grid[i-1][j] == plantType and j-1 >= 0 and grid[i][j-1] == plantType and grid[i-1][j-1] != plantType):
            sides += 1
        if (i-1 >= 0 and grid[i-1][j] == plantType and j+1 < len(grid[0]) and grid[i][j+1] == plantType and grid[i-1][j+1] != plantType):
            sides += 1

    
        #INTERIOR BOTTOM CORNER RIGHT AND LEFT
        if (i+1 < len(grid) and grid[i+1][j] == plantType and j-1 >= 0 and grid[i][j-1] == plantType and grid[i+1][j-1] != plantType):
            sides += 1
        if (i+1 < len(grid) and grid[i+1][j] == plantType and j+1 < len(grid[0]) and grid[i][j+1] == plantType and grid[i+1][j+1] != plantType):
            sides += 1

        dfsPart2(i+1,j,plantType)
        dfsPart2(i-1,j,plantType)
        dfsPart2(i,j+1,plantType)
        dfsPart2(i,j-1,plantType)

resPart2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in visited:
            plantType = grid[i][j]
            dfsPart2(i,j,grid[i][j])
            resPart2 += (area * sides)
            area = 0
            sides = 0


print(resPart2)
