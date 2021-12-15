from collections import defaultdict
from day14_data import seed, rules

currenGeneration = ['S','H']
size = len(currenGeneration)
runs = 10
for _ in range(runs):
    curr = []
    for i in range(size-1):
        key = currenGeneration[i:i+2]
        curr += key[0]
        curr += rules.get(''.join(key),'')
    currenGeneration = [*curr, currenGeneration[-1]]
    size = len(currenGeneration)

freq = defaultdict(lambda: 0)
for seg in currenGeneration:
    for l in seg:
        freq[l] += 1
sortedFreq = [v for k, v in sorted(freq.items(), key=lambda item: item[1])]
print(sortedFreq[-1] - sortedFreq[0])
