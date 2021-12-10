from day10_data import data
import numpy as np
import itertools

pointMap = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

bracketMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

missing = []
for row in data:
    stack = []
    missingRow = []
    for bracket in row:
        if bracket in ']}>)':
            test = stack.pop()
            if test != bracketMap[bracket]:
                missingRow.append(bracket)
            continue
            
        stack.append(bracket)
    if len(missingRow):
        continue
    missing.append(stack)
remaining = [m for m in missing if len(m)]
scores = []
for remains in remaining:
    runningTotal = 0
    for bracket in remains[::-1]:
        runningTotal *= 5
        runningTotal += pointMap[bracketMap[bracket]]
    scores.append(runningTotal)
print(np.median(scores))