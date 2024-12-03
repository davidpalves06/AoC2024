import sys,re
inputName = sys.argv[1]

file = open(inputName,'r')

res = 0

def checkInputResult(input):
    sumOfMult = 0
    matches = re.findall(r'(mul\(\d+\,\d+\)|do\(\)|don\'t\(\))',input)
    enabled = True
    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True 
        elif enabled:
            numbers = list(map(lambda x: int(x),re.findall(r'\d+',match)))
            sumOfMult += numbers[0] * numbers[1]
    return sumOfMult

res += checkInputResult(file.read())

print(res)