import networkx
import numpy as np
import math
import itertools
from day19_data import data
import matplotlib.pyplot as plt

rotLUT = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
]
rots = []
for yawS,yawC in rotLUT:
    for pitchS, pitchC in rotLUT:
        for rollS, rollC in rotLUT:
            r =  (
                    (yawC*pitchC, yawC*pitchS*rollS - yawS*rollC, yawC*pitchS*rollC + yawS*rollS),
                    (yawS*pitchC, yawS*pitchS*rollS + yawC*rollC, yawS*pitchS*rollC - yawC*rollS),
                    (-pitchS, pitchC*rollS, pitchC*rollC)
            )
            

            rots.append(r)
rots = list(set(rots))
rots = [[[np.array(el) for el in row] for row in rot] for rot in rots]


def calcDist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

g = networkx.DiGraph()
g.add_nodes_from(list(range(len(data))))

def figureOutStuff(match1,match2):
    trans1 = [np.array(v) for v in match1]
    for rot in rots:
        trans2 = [np.dot(rot,v) for v in match2]
        for v1 in trans1:
            for v2 in trans2:
                diff = v2-v1
                shifted = {tuple((v-diff).tolist()) for v in trans2}
                if len(match1.intersection(shifted)) >=12:
                    return (diff,rot)

for i in range(len(data)):
    for j in range(len(data)):
        if i==j: 
            continue
        data1 = data[i]
        data2 = data[j]
        data1_dist = [
            (p1,p2,calcDist(p1,p2)) for p1,p2 in itertools.combinations(data1,2)
        ]
        data2_dist = [
            (p1,p2,calcDist(p1,p2)) for p1,p2 in itertools.combinations(data2,2)
        ]

        match1 = set()
        match2 = set()
        for p11,p12,p1dist in data1_dist:
            for p21,p22,p2dist in data2_dist:
                if p1dist == p2dist:
                    match1.add(tuple(p11))
                    match1.add(tuple(p12))
                    match2.add(tuple(p21))
                    match2.add(tuple(p22))
        if len(match1) >= 12:
            print('matches',i,j)
            diff,rot = figureOutStuff(match1,match2)
            g.add_edge(j,i,diff=diff,rot=rot)

paths = dict(networkx.all_pairs_shortest_path(g))
points = {tuple(t) for t in data[0]}
for i in range(1,len(data)):
    vects = data[i]
    path = paths[i][0]
    for p in range(len(path)-1):
        edge = g.edges[path[p],path[p+1]]
        print(edge['diff'])
        vects = [np.dot(edge['rot'],v)-edge['diff'] for v in vects]
    for v in vects:
        points.add(tuple(v.tolist()))
    
print('Number of points:',len(points))     
networkx.draw_circular(g,with_labels=True)
plt.show()
print()