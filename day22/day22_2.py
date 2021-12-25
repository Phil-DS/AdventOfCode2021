from day22_data import data,data2

def unpackCube(cube):
    val,x,y,z = cube
    x1,x2 = x
    y1,y2 = y
    z1,z2 = z
    return val, (x1,y1,z1), (x2,y2,z2)

def AABB(box1min,box1max,box2min,box2max):
    return box1min[0] <= box2max[0] and box2min[0] <= box1max[0] \
       and box1min[1] <= box2max[1] and box2min[1] <= box1max[1] \
       and box1min[2] <= box2max[2] and box2min[2] <= box1max[2]

def getOverlap(box1min,box1max,box2min,box2max):
    return (
        max(box1min[0],box2min[0]),
        max(box1min[1],box2min[1]),
        max(box1min[2],box2min[2])
    ),(
        min(box1max[0],box2max[0]),
        min(box1max[1],box2max[1]),
        min(box1max[2],box2max[2])
    )

def getVol(cube):
    _,p1,p2 = cube
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return abs(x2 - x1 + 1) * abs(y2 - y1 + 1) * abs(z2 - z1 + 1)

cubeList = []

for d in data2:
    curr = unpackCube(d)
    cubesToAdd = []
    if curr[0]:
        cubesToAdd.append(curr)
    for cube in cubeList:
        if AABB(curr[1],curr[2],cube[1],cube[2]):
            newCube = getOverlap(curr[1],curr[2],cube[1],cube[2])
            cubesToAdd.append((int(not cube[0]),*newCube))

    cubeList = [*cubeList,*cubesToAdd]

res = [(2*c[0] - 1)*getVol(c) for c in cubeList]

print(sum(res))
