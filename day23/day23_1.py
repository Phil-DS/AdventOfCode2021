from day23_data import *
import itertools
import copy

# Analyse the problem.
# States at the start are:
#  - Wrong column
#  - Right but blocking
#  - In correct space

# minimum for the one to get to its right position
# Correct -> 0
# Right but blocking: 4x
# Incorrect -> posToGetOut + distToCol*2 + 1
# Then figure out swappings.

# for sortOrder in itertools.permutations(range(4),4):
#     hallways = copy.deepcopy(hallways)
#     corridor = [None for i in range(11)]
#     runningCost = 0
#     for colFirst in sortOrder:

distance = copy.deepcopy(hallways)
for h,hallway in enumerate(hallways):
    if hallway[-1] == chr(ord('A')+h):
        # It's complete, needs 0
        distance[h][-1] = 0
        if hallway[0] == chr(ord('A')+h):
            distance[h][0] = 0
        else:
            distance[h][0] = 2+(abs(ord(hallway[0])-h-ord('A'))*2)
    elif hallway[0] == chr(ord('A')+h):
        # it needs to move out of the way
        distance[h][0] = 4
        distance[h][-1] = 3+(abs(ord(hallway[-1])-h-ord('A'))*2)
    else:
        distance[h][0] = 2+(abs(ord(hallway[0])-h-ord('A'))*2)
        distance[h][-1] = 3+(abs(ord(hallway[-1])-h-ord('A'))*2)

total = {
    l:0 for l in 'ABCD'
}
for h,hallway in enumerate(hallways):
    for pos,fish in enumerate(hallway):
        total[fish] += distance[h][pos]

print(total)
state = copy.deepcopy(hallways)
main = [None for l in range(11)]
# Start with the smallest (For me, its B)
# Move the bad one to the closest point it can be to its final spot, without 
