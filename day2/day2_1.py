from day2_data import data2
import numpy as np

# Its a simple co-ordinate system, so can use unit vectors with speed.
# Using a unit vector dictionary to easily map the direction to a unit vector
dirs = {
    'forward': np.array([1,0]),
    'down': np.array([0,1]),
    'up': np.array([0,-1])
}

# Split on the space
splitData = [data.split(' ') for data in data2]

# Funky list comp+vertical sum
# Iterating over the data, convert line to vector, and create a 2xN Matrix
# Then sum the vectors together along the y axis for the final position vector
pos = np.sum([int(data[1]) * dirs[data[0]] for data in splitData], axis=0)

# Prod the values for the final result
print(np.prod(pos))