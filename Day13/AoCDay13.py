import sys

file = open(sys.argv[1],'r')

buttonA,buttonB,prize = (0,0),(0,0),(0,0)
machines = []

def getButtonTuple(buttonDescription):
    x = int(buttonDescription.split(',')[0].split('+')[1])
    y = int(buttonDescription.split(',')[1].split('+')[1])

    return (x,y)

def getPrizeTuple(prizeDescription):
    x = int(prizeDescription.split(',')[0].split('=')[1])
    y = int(prizeDescription.split(',')[1].split('=')[1])

    return (x,y)

def readMachine():
    global buttonA,buttonB,prize
    buttonADescription = file.readline().strip().split(':')[1]
    buttonBDescription = file.readline().strip().split(':')[1]
    prizeDescription = file.readline().strip().split(':')[1]
    
    buttonA = getButtonTuple(buttonADescription)
    buttonB = getButtonTuple(buttonBDescription)
    prize = getPrizeTuple(prizeDescription)

readMachine()
machines.append([buttonA,buttonB,prize])

while file.readline() != '':
    readMachine()
    machines.append([buttonA,buttonB,prize])

#Part1
# resPart1 = 0
# for machine in machines:
#     buttonA = machine[0]
#     buttonB = machine[1]
#     prize = machine[2]
#     numberOfA = 0
#     res = -1
#     while buttonA[0] * numberOfA <= prize[0]:
#         xVal = buttonA[0] * numberOfA
#         prizeWithoutX = prize[0] - xVal
#         if (prizeWithoutX % buttonB[0] == 0):
#             numberOfB = prizeWithoutX // buttonB[0]
#             if (buttonA[1] * numberOfA) + (buttonB[1] * numberOfB) == prize[1]:
#                 if res == -1:
#                     res = numberOfA*3 + numberOfB * 1
#                 else:
#                     res = min(numberOfA*3 + numberOfB * 1,res)
#         numberOfA += 1
#     if res != -1:
#         resPart1 += res


# print(resPart1)

# Part 2

# b = (py - a*ay)/ by
# a = (px * by - bx * py) / (ax * by - bx * ay) 

resPart2 = 0

for machine in machines:
    buttonA = machine[0]
    buttonB = machine[1]
    prize = machine[2]
    prize = (prize[0] + 10000000000000,prize[1] + 10000000000000)

    print(prize)
    remainderA  = (prize[0] * buttonB[1] - buttonB[0] * prize[1]) % (buttonA[0] * buttonB[1] - buttonB[0] * buttonA[1])
    a = (prize[0] * buttonB[1] - buttonB[0] * prize[1]) // (buttonA[0] * buttonB[1] - buttonB[0] * buttonA[1])
    remainderB = (prize[1] - a*buttonA[1]) % buttonB[1]
    b = (prize[1] - a*buttonA[1]) // buttonB[1]

    if remainderA != 0 or  remainderB != 0:
        continue
    else:
        resPart2 += (3*a +1*b) 

print(resPart2)

