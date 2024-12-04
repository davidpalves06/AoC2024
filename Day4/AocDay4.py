import sys

inputName = sys.argv[1]

file = open(inputName,'r')

text = []
for line in file.readlines():
    text.append(list(line.strip()))

## Part 1
def find_xmas(input):
    results = 0
    directions = [
        (1, 0),   # Right
        (-1, 0),  # Left
        (0, 1),   # Down
        (0, -1),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right    
    ]
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == 'X':
                for dx,dy in directions:
                    word = ''
                    x,y = i,j
                    for _ in range(len("XMAS")):
                        if 0 <= x < len(text) and 0 <= y < len(text[0]):
                            word += text[x][y]
                            if word == 'XMAS':
                                results += 1
                                break
                            x,y = x + dx,y + dy
                        else:
                            break
    return results

print(find_xmas(text))

## Part 2

def findCrossMas(text):
    results = 0
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == 'A':
                x,y = i,j
                if 0 <= x-1 < x + 1 < len(text) and 0 <= y-1 < y + 1 < len(text[0]):
                    if ((text[x-1][y-1] == 'M' and text[x+1][y+1] == 'S') or (text[x-1][y-1] == 'S' and text[x+1][y+1] == 'M')) and ((text[x-1][y+1] == 'M' and text[x+1][y-1] == 'S') or (text[x-1][y+1] == 'S' and text[x+1][y-1] == 'M')):
                        results += 1
                    
    return results

print(findCrossMas(text))