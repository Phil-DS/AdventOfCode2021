from multiprocessing import Pool
from day1_data import data1
from functools import reduce

batch = 20
threads = 5

def dataGenerator(data):
    i=0
    curr = data[i:i+batch+1]
    yield curr
    while len(curr) == batch+1:
        i+=batch
        curr = data[i:i+batch+1]
        yield curr

def reduceIncDec(data):
    rtn = [0,0] # dec, inc
    for i in range(len(data)-1):
        rtn[int(data[i+1] > data[i])] += 1
    return rtn


def combine(a,b):
    return [a[0]+b[0],a[1]+b[1]]

if __name__ == '__main__':
    with Pool(threads) as p:
        current = p.map(reduceIncDec, dataGenerator(data1))
        result = reduce(combine,current)
        print(f'{result[0]} decreasing, {result[1]} increasing')
        print(sum(result))