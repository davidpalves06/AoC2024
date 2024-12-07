import sys

inputName = sys.argv[1]

file = open(inputName,'r')

results = []
operands = []
for line in file.readlines():
    result,operand = line.strip().split(":")
    results.append(int(result))
    operands.append(list(map(lambda x:int(x),operand.strip().split(" "))))

#Part 1

def checkIfOperandsMakeResult(result,operands):
    res = False

    def backtrack(result,i,total):
        nonlocal res
        if total == result and i >= len(operands):
            res = True
            return

        if total > result or i >= len(operands):
            return
        
        tmp = operands[i] * total
        backtrack(result,i+1,tmp)

        tmp = operands[i] + total
        backtrack(result,i+1,tmp)

    backtrack(result,1,operands[0])
    return res

resPart1 = 0
for i in range(len(results)):
    result = results[i]

    if (checkIfOperandsMakeResult(result,operands[i])):
        resPart1 += result

print(resPart1)

## Part 2

def checkIfOperandsWithConcatMakeResult(result,operands):
    res = False

    def backtrack(result,i,total):
        nonlocal res
        if total == result and i >= len(operands):
            res = True
            return

        if total > result or i >= len(operands):
            return
        
        tmp = operands[i] * total
        backtrack(result,i+1,tmp)

        tmp = operands[i] + total
        backtrack(result,i+1,tmp)

        tmp = int((str(total) + str(operands[i])))
        backtrack(result,i+1,tmp)

    backtrack(result,1,operands[0])
    return res

resPart2 = 0
for i in range(len(results)):
    result = results[i]

    if (checkIfOperandsWithConcatMakeResult(result,operands[i])):
        resPart2 += result

print(resPart2)
