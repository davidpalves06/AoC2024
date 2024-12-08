from collections import defaultdict
import sys

inputName = sys.argv[1]

file = open(inputName,'r')

cityMap = []
for line in file.readlines():
    cityMap.append(list(line.strip()))

#Part 1
resPart1 = 0
antennaMap = defaultdict(list)
for i in range(len(cityMap)):
    for j in range(len(cityMap[0])):
        if cityMap[i][j] == '.':
            continue
        antennaMap[cityMap[i][j]].append((i,j))

antinodesAdded = set() 
for key in antennaMap.keys():
    antennas = antennaMap[key]
    for i in range(len(antennas)):
        for j in range(i+1,len(antennas)):
            firstAntenna = antennas[i]
            secondAntenna = antennas[j]

            xDiff = secondAntenna[0] - firstAntenna[0]
            yDiff = secondAntenna[1] - firstAntenna[1]

            firstAntinodeX = firstAntenna[0] - xDiff 
            firstAntinodeY = firstAntenna[1] - yDiff

            if 0 <= firstAntinodeX < len(cityMap) and 0 <= firstAntinodeY < len(cityMap[0]) and (firstAntinodeX,firstAntinodeY) not in antinodesAdded:
                antinodesAdded.add((firstAntinodeX,firstAntinodeY))
                resPart1 += 1

            secondAntinodeX = secondAntenna[0] + xDiff
            secondAntinodeY = secondAntenna[1] + yDiff
            if 0 <= secondAntinodeX < len(cityMap) and 0 <= secondAntinodeY < len(cityMap[0]) and (secondAntinodeX,secondAntinodeY) not in antinodesAdded:
                antinodesAdded.add((secondAntinodeX,secondAntinodeY))
                resPart1 += 1

print("Part 1 Result:", resPart1)
#Part 2

antinodesAdded = set() 
resPart2 = 0
for key in antennaMap.keys():
    antennas = antennaMap[key]
    for i in range(len(antennas)):
        for j in range(i+1,len(antennas)):
            firstAntenna = antennas[i]
            secondAntenna = antennas[j]

            if firstAntenna not in antinodesAdded:
                antinodesAdded.add(firstAntenna)
                resPart2 += 1
            if secondAntenna not in antinodesAdded:
                antinodesAdded.add(secondAntenna)
                resPart2 += 1

            xDiff = secondAntenna[0] - firstAntenna[0]
            yDiff = secondAntenna[1] - firstAntenna[1]

            firstAntinodeX = firstAntenna[0] - xDiff 
            firstAntinodeY = firstAntenna[1] - yDiff

            while 0 <= firstAntinodeX < len(cityMap) and 0 <= firstAntinodeY < len(cityMap[0]):
                if  (firstAntinodeX,firstAntinodeY) not in antinodesAdded:
                    antinodesAdded.add((firstAntinodeX,firstAntinodeY))
                    resPart2 += 1
                firstAntinodeX = firstAntinodeX - xDiff 
                firstAntinodeY = firstAntinodeY - yDiff

            secondAntinodeX = secondAntenna[0] + xDiff
            secondAntinodeY = secondAntenna[1] + yDiff

            while 0 <= secondAntinodeX < len(cityMap) and 0 <= secondAntinodeY < len(cityMap[0]):
                if (secondAntinodeX,secondAntinodeY) not in antinodesAdded:
                    antinodesAdded.add((secondAntinodeX,secondAntinodeY))
                    resPart2 += 1
                secondAntinodeX = secondAntinodeX + xDiff
                secondAntinodeY = secondAntinodeY + yDiff

print("Part 2 Result:",resPart2)
