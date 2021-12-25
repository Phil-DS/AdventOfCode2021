from day23_data import *
import functools
import heapq
from collections import defaultdict
import itertools

size = 2
lens = [1,1]
state = ['.','.']
for room in hallways:
    state.append(''.join(room))
    state.append('.')
    lens.append(len(room))
    lens.append(1)
state.append('.')
lens.append(1)

infinity= float('inf')

@functools.cache
def getNextMoves(state):
    newState = []
    # stateAsList = [*state]
    for i,room in enumerate(state):
        if lens[i] == 1:
            if room == '.':
                continue
            else:
                for ranges in [range(i-1,-1,-1),range(i+1,len(state))]:
                    for newPos in ranges:
                        if state[newPos][0] != '.' and lens[newPos] == 1:
                            # Can't go further down the corridor
                            break
                        else:
                            makeState = [*state]
                            if lens[newPos] == 1:
                                continue
                            if state[newPos][0] != '.':
                                #Cannot enter room
                                continue
                            # find the first non . in the room
                            if desired[room] != newPos:
                                continue
                            if any(desired[d]!= newPos for d in state[newPos] if d != '.'):
                                continue
                            for r in range(size):
                                if state[newPos][r] != '.':
                                    r = r-1
                                    break
                            # The ones to swap are 
                            newRoom = list(makeState[newPos])
                            newRoom[r] = room
                            makeState[newPos] = ''.join(newRoom)
                            makeState[i] = '.'
                            cost = (abs(newPos-i)+r+1) * costs[room] 
                            # newState.append((tuple(makeState),cost))
                            yield (cost,tuple(makeState))
                            continue
        else:
            # It's in a bigger room. 
            # doneFirst = False
            for j,pos in enumerate(room):
                if pos == '.':
                    continue
                # if not doneFirst:
                #     doneFirst = True
                for ranges in [range(i-1,-1,-1),range(i+1,len(state))]:
                    for newPos in ranges:
                        if state[newPos][0] != '.' and lens[newPos] == 1:
                            # Can't go further down the corridor
                            break
                        else:
                            makeState = [*state]
                            oldRoom = list(makeState[i])
                            oldRoom[j] = '.'
                            makeState[i] = ''.join(oldRoom)
                            if lens[newPos] == 1:
                                makeState[newPos] = pos
                                # makeState[i] = '.'
                                cost = (abs(newPos-i)+j+1) * costs[pos]
                                # newState.append((tuple(makeState),cost))
                                yield (cost,tuple(makeState))
                                continue
                break
                                # if state[newPos][0] != '.':
                                #     #Cannot enter room
                                #     continue
                                # # find the first non . in the room
                                # for r in range(size):
                                #     if state[newPos][r] != '.':
                                #         r = r-1
                                #         break
                                # # The ones to swap are 
                                # newRoom = list(makeState[newPos])
                                # newRoom[r] = pos
                                # makeState[newPos] = ''.join(newRoom)
                                
                                
                                # cost = (abs(newPos-i)+r+j+2) * costs[pos] 
                                # newState.append((cost,tuple(makeState)))
                                # continue

    # return newState

def doneness(state):
    dist = 0
    for i,space in enumerate(state):
        for j in range(lens[i]):
            if space[j] == '.':
                continue
            dist += abs(j-i) 
    return dist

def prune(states):
    costs = {}
    for cost,curr in states:
        if curr in costs:
            if costs[curr] > cost:
                costs[curr] = cost
        else:
            costs[curr] = cost
    return [(v,k) for k,v in costs.items()]

def dijkstra(initial, wanted):
    tested = defaultdict(lambda: infinity)
    tested[initial] = 0
    queue = [(0,initial)]
    visited = set()

    while len(queue):
        cost,state = heapq.heappop(queue)
        if state in visited:
            continue
        if state == wanted:
            return cost
        visited.add(state)
        if tested[state] < cost:
            continue

        for moveCost,newState in getNextMoves(tuple(state)):
            newCost = moveCost+cost

            if tested[newState] <= newCost:
                continue
            heapq.heappush(queue,(newCost,newState))
            tested[newState] = newCost
        queue = prune(queue)

# def quick(start,wanted):
#     done_states = []
#     states = [(start,0)]
#     while states:
#         new_states = []
#         for state,cost in states:
#             for new_state in getNextMoves(state):
#                 out,new_cost  = new_state
#                 toAdd = (out,new_cost+cost)
#                 if out == wanted:
#                     done_states.append(toAdd)
#                 else:
#                     new_states.append(toAdd)
#         states = prune(new_states)
#     return sorted(done_states, key=lambda x: x[1])[0]

req = ['.','.']
for room in [l*size for l in 'ABCD']:
    req.append(''.join(room))
    req.append('.')
req.append('.')

print(dijkstra(tuple(state),tuple(req)))
