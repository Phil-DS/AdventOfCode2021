from collections import defaultdict
from day14_data import seed , rules

# bin method
bins = {
    rule: 0 for rule in rules
}

mutate_rules = {
    rule: (rule[0]+rules[rule],rules[rule]+rule[1]) for rule in rules
}

for i in range(len(seed)-1):
    key = seed[i]+seed[i+1]
    bins[key] += 1

runs = 40

for _ in range(runs):
    currBins = {
        rule: 0 for rule in rules
    }
    for b in bins:
        if bins[b]:
            m0,m1 = mutate_rules[b]
            currBins[m0] += bins[b]
            currBins[m1] += bins[b]
    bins = {**currBins}

freq = defaultdict(lambda: 0)
for b in bins:
    freq[b[0]] += bins[b]
freq[seed[-1]] += 1

sortedFreq = [v for k, v in sorted(freq.items(), key=lambda item: item[1])]
print(sortedFreq[-1] - sortedFreq[0])