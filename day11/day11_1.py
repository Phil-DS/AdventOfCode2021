from day11_data import data
from copy import deepcopy

size = 10

newState = deepcopy(data)
days = 100
flashes = 0


for day in range(days):
    for i in range(size):
        for j in range(size):
            newState[j][i] += 1

    flashed = set()
    while True:
        delayed = 0
        for i in range(size):
            for j in range(size):
                if newState[j][i] >= 10 and (i,j) not in flashed:
                    delayed += 1
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            
                            if di == 0 and dj == 0:
                                continue
                            if (i+di) < 0 or (j+dj) < 0:
                                continue
                            try:
                                newState[j+dj][i+di] += 1
                            except:
                                pass
                    flashed.add((i,j))
        
        flashes += delayed
        if delayed == 0:
            break
    for i,j in flashed:
        newState[j][i] = 0

print(flashes)