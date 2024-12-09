from collections import defaultdict
import sys

inputName = sys.argv[1]

file = open(inputName,'r')

input = file.readline().strip()

isBlock = True
blockIndex = 0
blockSizeMap = defaultdict(tuple)
freeSpaceMap = defaultdict(list)
diskMap = []
for i in range(len(input)):
    value = int(input[i])
    if isBlock:
        blockSizeMap[blockIndex] = (value,len(diskMap))
        while value > 0:
            diskMap.append(blockIndex)
            value -= 1
        blockIndex += 1
    else:
        while value > 0:
            diskMap.append('.')
            value -= 1
    isBlock = not isBlock

left,right = 0,len(diskMap) - 1

part1DiskMap = diskMap.copy()
while left < right:
    if part1DiskMap[left] != '.':
        left += 1
        continue
    if part1DiskMap[right] == '.':
        right -= 1
        continue
    part1DiskMap[left],part1DiskMap[right] = part1DiskMap[right],part1DiskMap[left]
    right -= 1
    left += 1

resPart1 = 0

for i,value in enumerate(part1DiskMap):
    if value != '.':
        resPart1 += i * value

print(resPart1)

#Part 2
def swapBlock(start,size,swapingIndex):
    while size > 0:
        diskMap[start],diskMap[swapingIndex] = diskMap[swapingIndex],diskMap[start]
        start += 1
        swapingIndex += 1
        size -= 1

blockIndex -= 1
while blockIndex > 0:
    left = 0
    blockSize = blockSizeMap[blockIndex]
    while left < blockSize[1]:
        if diskMap[left] == '.':
            start = left
            end = start
            while end < len(diskMap) and diskMap[end] == '.':
                end += 1
                left += 1
            if end - start >= blockSize[0]:
                swapBlock(start,blockSize[0],blockSize[1])
                break
        else:
            left += 1
    blockIndex -= 1

resPart2 = 0

for i,value in enumerate(diskMap):
    if value != '.':
        resPart2 += i * value

print(resPart2)


