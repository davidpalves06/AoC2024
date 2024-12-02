file = open('input.txt','r')

reports = []
safes = 0
for line in file.readlines():
    report = []
    for level in line.split(" "):
        val = int(level)
        report.append(val)
    reports.append(report)

def isIncreasing(levels):
    lastLevel = levels[0]
    i = 1
    while i < len(levels):
        if levels[i] <= lastLevel or levels[i] > lastLevel + 3:
            return False
        lastLevel = levels[i]
        i+= 1
    return True


def isDecreasing(levels):
    lastLevel = levels[0]
    i = 1
    while i < len(levels):
        if levels[i] >= lastLevel or levels[i] < lastLevel - 3:
            return False
        else:
            lastLevel = levels[i]
            i+= 1
    return True

for report in reports:
    isSafe = False
    for j in range(len(report)):
        changedReport = report[:j] + report[j+1:]
        if (isIncreasing(changedReport) or isDecreasing(changedReport)):
            isSafe = True
            break
    if isSafe:
        safes += 1

print(safes)