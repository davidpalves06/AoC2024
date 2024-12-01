import heapq
from typing import Counter

file = open('input.txt','r')
firstList = []
secondList = []

for line in file.readlines():
    input = line.strip().split("   ")
    heapq.heappush(firstList,int(input[0]))
    heapq.heappush(secondList,int(input[1]))

counterFirst = Counter(firstList)
counterSecond = Counter(secondList)

res = 0
while firstList and secondList:
    res += abs(heapq.heappop(firstList) - heapq.heappop(secondList))

print(res) 

# Part Two

res = 0
for key in counterFirst.keys():
    res += counterFirst[key] * (key * counterSecond[key])

print(res)