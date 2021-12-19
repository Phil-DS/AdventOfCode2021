from day18_data import data
import math
import ast


def nestReduce(base):
    if type(base[0]) is list:
        l = nestReduce(base[0])
    else:
        l = base[0]
    if type(base[1]) is list:
        r = nestReduce(base[1])
    else:
        r = base[1]
    return 3*l + 2*r
     

current = data[0]
for d in data[1:]:
    current = f'[{current},{d}]'
    # print(current)
    changed = True
    while changed:
        changed = False
        depth = 0
        inNumber = False
        splitAction = None
        for i in range(len(current)):
            c = current[i]
            if c == '[':
                depth += 1
                inNumber = False
                if depth > 4:
                    changed = True
                    end = 0
                    for di in range(9):
                        if current[i+di] == ']':
                            end = di
                            break
                    n = [int(x) for x in current[(i+1):i+di].split(',')] # Slices off the brackets
                    onLeft = current[:i]
                    onRight = current[i+di+1:]
                    mostLeft = None
                    for dl in range(-1, -len(onLeft), -1):
                        if onLeft[dl] in '0123456789':
                            if onLeft[dl-1] in '0123456789':
                                mostLeft = (len(onLeft)+dl-2,len(onLeft)+dl)
                            else:
                                mostLeft = (len(onLeft)+dl-1,len(onLeft)+dl)
                            break
                    mostRight = None
                    for dr in range(len(onRight)):
                        if onRight[dr] in '0123456789':
                            if onRight[dr+1] in '0123456789':
                                mostRight = (dr,dr+2)
                            else:
                                mostRight = (dr,dr+1)
                            break
                    if mostLeft:
                        s = onLeft[mostLeft[0]+1:mostLeft[1]+1]
                        val = int(s)
                        val += n[0]
                        onLeft = f'{onLeft[:mostLeft[0]+1]}{val}{onLeft[mostLeft[1]+1:]}'
                    if mostRight:
                        s = onRight[mostRight[0]:mostRight[1]]
                        val = int(s)
                        val += n[1]
                        onRight = f'{onRight[:mostRight[0]]}{val}{onRight[mostRight[1]:]}'
                    current = f'{onLeft}0{onRight}'
                    # print('Boom @',i)
                    # print(current)
                    splitAction = None
                    break
            elif c == ']':
                depth -= 1
                inNumber = False
            elif c == ',':
                inNumber = False
            else:
                if inNumber:
                    # It should be more than 2
                    if splitAction:
                        continue
                    splitAction = i
                    # onLeft = current[:i-1]
                    # onRight = current[i+1:]
                    # val = int(current[i-1:i+1])
                    # print('Reduce - ',current[i-1:i+1], '@', i)
                    # current = f'{onLeft}[{math.floor(val/2)},{math.ceil(val/2)}]{onRight}'
                    # print(current)
                    # changed = True
                    # break
                else:
                    inNumber = True
        
        if splitAction is not None:
            i = splitAction
            onLeft = current[:i-1]
            onRight = current[i+1:]
            val = int(current[i-1:i+1])
            # print('Reduce - ',current[i-1:i+1], '@', i)
            current = f'{onLeft}[{math.floor(val/2)},{math.ceil(val/2)}]{onRight}'
            # print(current)
            changed = True
            
    # print(current)

print(current)
nested = ast.literal_eval(current)
print(nested)
print(nestReduce(nested))