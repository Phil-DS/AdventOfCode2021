from day25_data import *

righters = []
downers = []
width = len(data[0])
height = len(data)
for j,row in enumerate(data):
    for i,obj in enumerate(row):
        if obj == '.':
            continue
        if obj == '>':
            righters.append((i,j))
        else:
            downers.append((i,j))

i = 0

while True:
    moved = False
    newRighters = []
    for righter in righters:
        newPos = ((righter[0]+1)%width, righter[1])
        if newPos in righters or newPos in downers:
            newRighters.append(righter)
        else:
            moved = True
            newRighters.append(newPos)
    righters = [*newRighters]
    newDowners = []
    for downer in downers:
        newPos = (downer[0], (downer[1]+1)%height)
        if newPos in righters or newPos in downers:
            newDowners.append(downer)
        else:
            moved = True
            newDowners.append(newPos)
    downers = [*newDowners]
    i += 1
    if not moved:
        break
print(i)
