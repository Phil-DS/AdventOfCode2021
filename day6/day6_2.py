from day6_data import data
import math

test_data = [3,4,3,1,2]
totalDays = 100000

def calcBabies(initialTimer, days_remaining):
    if days_remaining < initialTimer:
        return 0
    return 1 + max(0,math.floor((days_remaining - initialTimer)/7))


lut = [0 for i in range(totalDays + 1)]
for dates in range(totalDays + 1):
    baseBabies = calcBabies(9,dates)
    for d in range(dates-9,0,-7):
        baseBabies += lut[d]
    lut[dates] = baseBabies

index_lut = [0 for i in range(0,7)]

for i in range(1,8):
    base = calcBabies(i+1,totalDays) + 1
    for d in range(totalDays-i-1,-1,-7):
        base += lut[d]
    index_lut[i-1] = base

print(sum([index_lut[d-1] for d in data]))
