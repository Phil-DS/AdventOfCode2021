from day9_data import data
import numpy as np

top = 99

out = [['x' for _ in d] for d in data]

cnt = []
carry = 1
for i, row in enumerate(data):
    for j, n in enumerate(row):
        toTest = set()
        if i != 0 and data[i-1][j] <= n:
            continue
        if j != 0 and data[i][j-1] <= n:
            continue
        if i != top and data[i+1][j] <= n:
            continue
        if j != top and data[i][j+1] <= n:
            continue
        
        toTest = {(i, j),}
        added = set()
        while len(toTest):
            newToTest = set()
            for obj in toTest:
                ti, tj = obj
                if ti < 0 or ti > top or tj < 0 or tj > top:
                    continue
                tn = data[ti][tj]
                if tn != 9:
                    added.add(obj)
                    newToTest.add((ti-1, tj))
                    newToTest.add((ti+1, tj))
                    newToTest.add((ti, tj-1))
                    newToTest.add((ti, tj+1))
            toTest = newToTest - added

        for x,y in added:
            out[x][y] = carry
        cnt.append(len(added))
        carry += 1

print(np.prod(list(sorted(cnt,reverse=True))[:3]))
# For fun, here is a map
with open('o.txt','w') as f:
    for row in out:
        print(*row, sep='\t', file=f)
