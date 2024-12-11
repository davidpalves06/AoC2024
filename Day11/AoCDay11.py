from collections import defaultdict
import sys

file = open(sys.argv[1],'r')

stones = {int(n):1 for n in file.readline().strip().split(" ")}

def blink(stones):
    newStones = defaultdict(int)
    for stone,count in stones.items():
        if stone == 0:
            newStones[1] += count
        elif len(str(stone)) % 2 > 0:
            newStones[stone*2024] += count
        else:
            stoneString = str(stone)
            leftPart = stoneString[:len(stoneString) // 2]
            rightPart = stoneString[len(stoneString) // 2:]
            newStones[int(leftPart)] += count
            newStones[int(rightPart)] += count
    return newStones

#Part 1
blinks = 25

for _ in range(blinks):
    stones = blink(stones)

resPart1 = sum(stones.values())
print(resPart1)

#Part 2
blinks = 75

for _ in range(25,blinks):
    stones = blink(stones)

resPart2 = sum(stones.values())
print(resPart2)


