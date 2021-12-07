# from day7_data import test_data as data
from day7_data import data
# from matplotlib import pyplot as plt

import numpy as np
import math

limits = 0,2000

data_np = np.array(data)
med = np.mean(data_np)
med_lower, med_higher = math.floor(med), math.ceil(med)

dists_lower = np.absolute(data_np - med_lower)
dists_higher = np.absolute(data_np - med_higher)
dist_lower = np.sum((dists_lower ** 2 + dists_lower)/2)
dist_higher = np.sum((dists_higher ** 2 + dists_higher)/2)


print(min(dist_higher, dist_lower))
