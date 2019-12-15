import math
# https://adventofcode.com/2019/day/1
input = [89122, 141123, 91549, 66506,
        53504, 56517, 77050, 92298,
        84853, 141828, 86739, 126125,
        82793, 113761, 68961, 132576,
        61718, 64498, 110415, 134867,
        102449, 107364, 88491, 120584,
        52192, 130494, 121583, 132166,
        111339, 68715, 104966, 117227,
        58921, 83909, 70626, 141637,
        95127, 72029, 136121, 136915,
        74312, 54863, 53547, 149493,
        78528, 132289, 148754, 133905,
        135357, 58483, 62214, 124684,
        118590, 107087, 95768, 86835,
        122277, 126183, 108546, 75212,
        62280, 76039, 135743, 86133,
        111613, 139477, 65930, 106225,
        101531, 96501, 66844, 114158,
        137091, 138143, 102083, 69857,
        59372, 137605, 108135, 96365,
        94851, 104414, 74194, 74188,
        131888, 75910, 78279, 93285,
        53597, 82705, 119360, 149274,
        92510, 95490, 54087, 97695,
        94753, 80493, 101173, 51906]

def calculateFuel(mass):
    return math.floor(mass / 3) - 2

def calculateFuelForFuel(mass):
    massfuel = 0
    fuelfuel = 0
    fuelfuel = massfuel = calculateFuel(mass)
    while fuelfuel > 0:
        fuelfuel = calculateFuel(fuelfuel)
        fuelfuel = 0 if fuelfuel < 0 else fuelfuel
        massfuel += fuelfuel

    return massfuel


totalmass = 0
for mass in input:
    totalmass += calculateFuelForFuel(mass)

print(totalmass)