# https://adventofcode.com/2019/day/4

rangeStart = 145852
rangeEnd = 616942

def hasOnlyTwoEqualAdjacentDigits(number):
    hasAdjacentDigits = False
    for x in range(len(number) - 2):
        if x != 0:
            hasAdjacentDigits = True if number[x] == number[x + 1] and number[x] != number[x + 2] and number[x] != number[x - 1] else hasAdjacentDigits
        else:
            hasAdjacentDigits = True if number[x] == number[x + 1] and number[x] != number[x + 2] else hasAdjacentDigits
        if number[-1] == number[-2] and number[-1] != number[-3]: # dumb but it works
            hasAdjacentDigits = True
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
    if hasOnlyTwoEqualAdjacentDigits(str(x)) and hasOnlyIncreasingDigits(str(x)):
        counter += 1

print(counter)