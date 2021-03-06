# And... back to python. C and I have parted ways for the time being...
with open('day3.txt') as f:
    data = [[int(c) for c in row.rstrip()] for row in f]

# Quick counter, and returning the not selected ones, because you want to check the most significant
def bitCount(d,i):
    count = 0
    for _d in d:
        count += _d[i]
    return count,len(d)-count

curr = [*data]
for i in range(12):
    # get the counts
    ones,zeros = bitCount(curr,i)
    # set the bit
    bit = 1 if ones==zeros else int(ones > zeros)
    # filter
    curr = [d for d in curr if d[i]==bit]
    # break clause
    if(len(curr) == 1):
        break
# Join the array of bits back as a number
val1 = int(''.join([str(b) for b in curr[0]]),2)

# And... Again!
curr = [*data]
for i in range(12):
    ones,zeros = bitCount(curr,i)
    bit = 0 if ones==zeros else int(ones < zeros) # New bit evaluation
    curr = [d for d in curr if d[i]==bit]
    if(len(curr) == 1):
        break
# Join the array of bits back as a number
val2 = int(''.join([str(b) for b in curr[0]]),2)

# And the final value
print(val1*val2)