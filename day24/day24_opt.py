from collections import defaultdict
from day24_data import instructions

def sliceItUp():
    sliced = []
    curr = [instructions[0]]
    for i in range(1,len(instructions)):
        if instructions[i][0] == 'inp':
            sliced.append(curr)
            curr = []
        curr.append(instructions[i])

    sliced.append(curr)
    return sliced  

possibleWs = list(range(1,10))

def doTask(tasks):
    # If it has a (div,z,26) => its a range limiter 
    zs = [(0,0)] 
    maxVal = 1
    for i,taskSet in enumerate(tasks):
        currPass = []
        if taskSet[4] == ('div','z','26'):
            # its a limit
            values = defaultdict(lambda: [])
            for w in possibleWs:
                for wLong,z in zs:
                    val = z//26
                    if ((z % 26) + int(taskSet[5][2])) != w:
                        # x will be 0 here
                        val = val * 26 + w + int(taskSet[15][2])
                    values[val].append(wLong * 10 + w)
            # do a prune here. Heap it, then 
            currPass = [(max(v),k) for k,v in values.items()]
            maxVal /= 26
        else:
            # standard pass
            for w in possibleWs:
                for wLong,z in zs:
                    currPass.append((wLong * 10 + w, 26*z + w + int(taskSet[15][2])))
            maxVal *= 26
        zs = [c for c in currPass if c[1]<maxVal]
        # maxVal /= 26
    return zs

slicedInstr = sliceItUp()
potential = doTask(slicedInstr)
possible = []

for wLong,z in potential:
    if z:
        continue
    possible.append(wLong)

# print(possible)
print(max(possible))