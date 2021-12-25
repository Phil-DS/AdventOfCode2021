from day22_data import data2
import itertools

points = set()

for val,x,y,z in data2:
    x1,x2 = x
    y1,y2 = y
    z1,z2 = z
    newPoints = {p for p in itertools.product(range(x1,x2+1),range(y1,y2+1),range(z1,z2+1))}
    if val:
        points = points.union(newPoints)
    else:
        points = points - newPoints

print(len(points))