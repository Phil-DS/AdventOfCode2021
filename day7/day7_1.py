# from day7_data import test_data as data
from day7_data import data
# from matplotlib import pyplot as plt

import numpy as np
import math

limits = 0,2000

data_np = np.array(data)
med = np.median(data_np)
med_lower, med_higher = math.floor(med), math.ceil(med)
dist_lower = np.sum(np.absolute(data_np - med_lower))
dist_higher = np.sum(np.absolute(data_np - med_higher))

print(dist_higher, dist_lower)
