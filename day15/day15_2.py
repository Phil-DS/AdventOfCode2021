from collections import defaultdict
from day15_data import data as base_data
import numpy as np

tmp = [
    [[[((r+i+j-1)%9)+1  for r in row] for row in base_data] for i in range(0,5)] for j in range(0,5)
]
tmp2 = [np.concatenate(row, axis=1).tolist() for row in tmp]
data = []
for d in tmp2:
    for row in d:
        data.append(row)

def h(x, y):
    return -y + 198 - x

def g(x, y):
    return data[y][x]

top = 500
toTest = [(0,0)]

cameFrom = {}

gScore = defaultdict(lambda: 1000000000)
gScore[(0,0)] = 0


fScore = {
    (0,0): h(0,0)
}

def retraceStep(x):
    curr = x
    while curr is not None:
        yield curr
        curr = cameFrom.get(curr, None)

while len(toTest) != 0:
    curr = toTest.pop(0)
    if curr == (top-1,top-1):
        print(gScore[curr])
        break
    x,y = curr
    if x-1 > -1: 
        score = gScore[curr] + g(x-1,y)
        if score < gScore[(x-1,y)]:
            cameFrom[ (x-1,y)] = curr
            gScore[(x-1,y)] = score
            fScore[(x-1,y)] = score + h(x-1,y)
            if (x-1,y) not in toTest:
                toTest.append((x-1,y))
    if x+1 < top: 
        score = gScore[curr] + g(x+1,y)
        if score < gScore[(x+1,y)]:
            cameFrom[ (x+1,y)] = curr
            gScore[(x+1,y)] = score
            fScore[(x+1,y)] = score + h(x+1,y)
            if (x+1,y) not in toTest:
                toTest.append((x+1,y))
    if y-1 > -1: 
        score = gScore[curr] + g(x,y-1)
        if score < gScore[(x,y-1)]:
            cameFrom[ (x,y-1)] = curr
            gScore[(x,y-1)] = score
            fScore[(x,y-1)] = score + h(x,y-1)
            if (x,y-1) not in toTest:
                toTest.append((x,y-1))
    if y+1 < top: 
        score = gScore[curr] + g(x,y+1)
        if score < gScore[(x,y+1)]:
            cameFrom[ (x,y+1)] = curr
            gScore[(x,y+1)] = score
            fScore[(x,y+1)] = score + h(x,y+1)
            if (x,y+1) not in toTest:
                toTest.append((x,y+1))


    toTest.sort(key = lambda x: fScore[x])
