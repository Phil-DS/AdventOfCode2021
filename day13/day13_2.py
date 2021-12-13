from numpy import sin
from day13_data import data,folds
# import numpy as np

def fold(paper,axis,line):
    rtn = set()
    for x,y in paper:
        if axis == 'x':
            dist = abs(line - abs(line - x))
            rtn.add((dist,y))
        else:
            dist = abs(line - abs(line - y))
            rtn.add((x,dist))
    
    return rtn

res = [*data]
for folding in folds:
    res = fold(res, *folding)

# my size is 40/13
scr = [[' ' for _ in range(40)] for _ in range(6)]
for x,y in res:
    scr[y][x] = '█'

for row in scr:
    print(*row,sep='')