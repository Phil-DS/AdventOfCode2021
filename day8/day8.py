from collections import defaultdict
from day8_data import data

seven = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg'
]

class SevenSeg:
    def __init__(self, segs):
        self.bitMapping = {}
        self.determine_segs(segs)

    def determine_segs(self,segs):
        self.bitMapping = {}
        # map indexes
        # First, get frequency
        freq = defaultdict(lambda: 0)
        for seg in segs:
            for l in seg:
                freq[l] += 1
        sortedFreq = [k for k, v in sorted(freq.items(), key=lambda item: item[1])]
        self.bitMapping[sortedFreq[1]] = 'b'
        self.bitMapping[sortedFreq[0]] = 'e'
        self.bitMapping[sortedFreq[-1]] = 'f'

        # We know 1 and 7, so, the difference between them is a
        sortedSegs = sorted(segs,key=len)
        self.bitMapping[list(set(sortedSegs[1]) - set(sortedSegs[0]))[0]] = 'a'
        # 1 is obvs CF, so we need to determine which is C and which is F
        self.bitMapping[sortedSegs[0][0] if sortedSegs[0][1] == sortedFreq[-1] else sortedSegs[0][1]] = 'c'

        is2d = sortedFreq[2] in sortedSegs[2]
        self.bitMapping[sortedFreq[2] if is2d else sortedFreq[3]] = 'd'
        self.bitMapping[sortedFreq[2] if not is2d else sortedFreq[3]] = 'g'


    def getNum(self, code):
        return seven.index(''.join(sorted(self.bitMapping[c] for c in code)))
    
# Part 1

cnt = [0 for _ in range(10)]
for codex, ns in data:
    dis = SevenSeg(codex)
    for n in ns:
        cnt[dis.getNum(n)] += 1

print(cnt)
print(cnt[1]+cnt[4]+cnt[7]+cnt[8])

# Part 2
total = 0
for codex, ns in data:
    dis = SevenSeg(codex)
    curr = 0
    for n in ns:
        curr = dis.getNum(n) + curr*10
    total += curr

print(total)