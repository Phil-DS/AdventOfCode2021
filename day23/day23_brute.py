from day23_data import *
import functools

size = 4 # Set to 2 for part 2
lens = [1,1]
state = ['.','.']
for room in hallways:
    state.append(''.join(room))
    state.append('.')
    lens.append(len(room))
    lens.append(1)
state.append('.')
lens.append(1)

# Comment out for part 1
for i in range(2,10,2):
    l = list(state[i])
    l.insert(1,hallwaysExt[int(i/2)-1][0])
    l.insert(2,hallwaysExt[int(i/2)-1][1])
    state[i] = ''.join(l)

req = ['.','.']
for room in [l*size for l in 'ABCD']:
    req.append(''.join(room))
    req.append('.')
req.append('.')

@functools.cache
def getNextMoves(state):
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
                            yield (tuple(makeState),cost)
                            continue
        else:
            # It's in a bigger room. 
            for j,pos in enumerate(room):
                if pos == '.':
                    continue
                for ranges in [range(i-1,-1,-1),range(i+1,len(state))]:
                    for newPos in ranges:
                        if state[newPos][0] != '.' and lens[newPos] == 1:
                            # Can't go further down the corridor
                            break
                        else:
                            if desired[pos] == i and all(desired[d]== i for d in room if d != '.'):
                                continue
                            makeState = [*state]
                            oldRoom = list(makeState[i])
                            oldRoom[j] = '.'
                            makeState[i] = ''.join(oldRoom)
                            if lens[newPos] == 1:
                                makeState[newPos] = pos
                                cost = (abs(newPos-i)+j+1) * costs[pos]
                                yield (tuple(makeState),cost)
                                continue
                break

def prune(states):
    costs = {}
    for curr,cost in states:
        if curr in costs:
            if costs[curr] > cost:
                costs[curr] = cost
        else:
            costs[curr] = cost
    return costs.items()

def quick(start,wanted):
    done_states = []
    states = [(start,0)]
    while states:
        new_states = []
        for state,cost in states:
            for new_state in getNextMoves(state):
                out,new_cost  = new_state
                toAdd = (out,new_cost+cost)
                if out == wanted:
                    done_states.append(toAdd)
                else:
                    new_states.append(toAdd)
        states = prune(new_states)
    return sorted(done_states, key=lambda x: x[1])[0]

print(quick(tuple(state),tuple(req)))
