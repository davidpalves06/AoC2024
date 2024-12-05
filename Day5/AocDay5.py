from collections import defaultdict
import sys

inputName = sys.argv[1]

file = open(inputName,'r')
line = file.readline()

def have_duplicates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    return bool(set1 & set2)
#Part 1

def getResultForUpdate(update,dict):
    pagesSeen = []
    for page in update:
        if have_duplicates(dict[page],pagesSeen):
            return -1
        pagesSeen.append(page)

    return update[(len(update) - 1) // 2]

orderingDict = defaultdict(list)
while line != '\n':
    orderingRule = list(map(lambda x: int(x),line.strip().split("|")))
    orderingDict[orderingRule[0]].append(orderingRule[1])
    line = file.readline()

while line == '\n':
    line = file.readline()

resPart1 = 0
incorrectUpdates = []
while line not in ['','\n']:
    update = list(map(lambda x:int(x) , line.strip().split(',')))
    updateResult = getResultForUpdate(update,orderingDict)
    if updateResult == -1:
        incorrectUpdates.append(update)
    else:
        resPart1 += getResultForUpdate(update,orderingDict)
    line = file.readline()

print("Result Part 1:",resPart1)

## Part 2

resPart2 = 0
def fixIncorrectUpdate(update,orderingDict):
    pagesSeen = defaultdict(int)
    i = 0
    while i < len(update):
        page = update[i]
        pageRule = orderingDict[page]
        swapped = False
        pageIndex = 1000000
        for rule in pageRule:
            if rule in pagesSeen.keys():
                if pagesSeen[rule] < pageIndex:
                    pageIndex = pagesSeen[rule]
                del pagesSeen[rule]
                swapped = True
        if not swapped:
            pagesSeen[page] = i
            i += 1
        else:
            update[i],update[pageIndex] = update[pageIndex],update[i]
            pagesSeen[page] = i
            i = pageIndex

    
    return getResultForUpdate(update,orderingDict)
        
                
for update in incorrectUpdates:
    fixUpdateResult = fixIncorrectUpdate(update,orderingDict)
    if fixUpdateResult == -1:
        print(update)
    else:
        resPart2 += fixUpdateResult
print("Result Part 2:",resPart2)
