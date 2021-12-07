from day2_data import data2
import numpy as np

# Split as before
splitData = [data.split(' ') for data in data2]

# Have to do things the long way. 
pos = [0,0]
# Tracking aim separate from the position, to not mess the prod at the end
aim = 0

# iterate and reduce
for data in splitData:
    n = int(data[1])
    if data[0] == 'forward':
        pos[0] += n
        pos[1] += n * aim
    else:
        aim += n * (-1 if data[0] == 'up' else 1)

# Print final product
print(np.prod(pos))