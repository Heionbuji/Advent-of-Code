# https://adventofcode.com/2019/day/4

rangeStart = 145852
rangeEnd = 616942

def hasTwoEqualAdjacentDigits(number):
    hasAdjacentDigits = False
    for x in range(len(number) - 1):
        hasAdjacentDigits = True if number[x] == number[x + 1] else hasAdjacentDigits
    return hasAdjacentDigits

def hasOnlyIncreasingDigits(number):
    onlyIncreasingDigits = False
    for x in range(len(number) - 1):
        if number[x] > number[x + 1]:
            onlyIncreasingDigits = False
            break
        else:
            onlyIncreasingDigits = True
    return onlyIncreasingDigits

counter = 0
for x in range(rangeStart, rangeEnd):
    if hasTwoEqualAdjacentDigits(str(x)) and hasOnlyIncreasingDigits(str(x)):
        counter += 1

print(counter)