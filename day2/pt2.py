import copy
# https://adventofcode.com/2019/day/2
input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0]
def interpret(cmds):
    cmdscopy = copy.deepcopy(cmds)
    ISP = 0
    while cmdscopy[ISP] != 99:
        if cmdscopy[ISP] == 1:
            cmdscopy[cmdscopy[ISP + 3]] = cmdscopy[cmdscopy[ISP + 1]] + cmdscopy[cmdscopy[ISP + 2]]
        elif cmdscopy[ISP] == 2:
            cmdscopy[cmdscopy[ISP + 3]] = cmdscopy[cmdscopy[ISP + 1]] * cmdscopy[cmdscopy[ISP + 2]]
        else:
            print('something went wrong')
            break
        ISP += 4
    return cmdscopy

noun = 0
verb = 0
output = 0

while 'there is stuff to do':
    input[1] = noun
    input[2] = verb
    output = interpret(input)
    if output[0] == 19690720:
        break
    if verb == 99:
        verb = 0
        noun += 1
    else:
        verb += 1

print(100 * noun + verb)