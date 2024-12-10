import sys

file = open(sys.argv[1],'r')

topoMap = []
for line in file.readlines():
    topoMap.append(list(map(lambda x:int(x),line.strip())))

#Part1

visited = set()
resultSet = set()
def calculateRatingForTrailHead(i,j,expected):
    global resPart1
    if 0 <= i < len(topoMap) and 0 <= j < len(topoMap[0]) and (i,j) not in visited and topoMap[i][j] == expected:
        visited.add((i,j))
        if expected != 9 or (i,j) in resultSet:
            calculateRatingForTrailHead(i+1,j,expected + 1)
            calculateRatingForTrailHead(i-1,j,expected + 1)
            calculateRatingForTrailHead(i,j+1,expected + 1)
            calculateRatingForTrailHead(i,j-1,expected + 1)
        else:
            resultSet.add((i,j))
            resPart1 += 1
        visited.remove((i,j))
    else:
        return


resPart1 = 0
for i in range(len(topoMap)):
    for j in range(len(topoMap[0])):
        resultSet = set()
        if topoMap[i][j] == 0:
            calculateRatingForTrailHead(i,j,0)
            print(i,j,resPart1)


print(resPart1)

# Part2

def calculateRatingForTrailHead(i,j,expected):
    global resPart2
    if 0 <= i < len(topoMap) and 0 <= j < len(topoMap[0]) and (i,j) not in visited and topoMap[i][j] == expected:
        visited.add((i,j))
        if expected != 9:
            calculateRatingForTrailHead(i+1,j,expected + 1)
            calculateRatingForTrailHead(i-1,j,expected + 1)
            calculateRatingForTrailHead(i,j+1,expected + 1)
            calculateRatingForTrailHead(i,j-1,expected + 1)
        else:
            resPart2 += 1
        visited.remove((i,j))
    else:
        return

resPart2 = 0
for i in range(len(topoMap)):
    for j in range(len(topoMap[0])):
        resultSet = set()
        if topoMap[i][j] == 0:
            calculateRatingForTrailHead(i,j,0)
            print(i,j,resPart2)


print(resPart2)