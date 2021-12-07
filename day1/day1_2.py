from multiprocessing import Pool
from day1_data import data1, testData
from functools import reduce

batch = 20
threads = 5

def slideDataGenerator(data):
    return [sum(data[i:i+3]) for i in range(len(data)-2)]

def dataGenerator(data):
    i=0
    curr = data[i:i+batch+1]
    yield curr
    while len(curr) == batch+1:
        i+=batch
        curr = data[i:i+batch+1]
        yield curr

def reduceIncDec(data):
    rtn = [0,0,0] # dec, same, inc
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        index = 1 if diff == 0 else (1 + int(diff/abs(diff)))
        rtn[index] += 1
    return rtn


def combine(a,b):
    return [a[0]+b[0],a[1]+b[1], a[2]+b[2]]

if __name__ == '__main__':
    with Pool(threads) as p:
        data2 = list(slideDataGenerator(data1))
        current = p.map(reduceIncDec, dataGenerator(data2))
        result = reduce(combine,current)
        print(f'{result[0]} decreasing, {result[1]} the same, {result[2]} increasing')
        print(sum(result))