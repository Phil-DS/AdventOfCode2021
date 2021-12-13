from numpy import sin
from day13_data import data,folds
# import numpy as np

def fold(data,axis,line):
    rtn = set()
    for x,y in data:
        if axis == 'x':
            dist = line - abs(line - x)
            rtn.add((dist,y))
        else:
            dist = line - abs(line - y)
            rtn.add((y,dist))
    
    return rtn

single = fold(data, *folds[0])
print(len(single))
print(len(data))
