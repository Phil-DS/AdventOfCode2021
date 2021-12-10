from day10_data import data

pointMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

bracketMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
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
    
    missing.append(missingRow)
print(sum(pointMap[m[0]] for m in missing if len(m)))