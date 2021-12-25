from day21_data import *
import itertools
import functools

@functools.cache
def rollMultiverse(score, otherScore, state, otherState):
    if score >= 21:
        return 1,0
    if otherScore >= 21:
        return 0,1
        
    thisWins = (0,0)
    for roll in itertools.product([1,2,3],repeat=3):
        newState = 1+((state+sum(roll)-1)%10)
        newScore = score+newState

        w2,w1 = rollMultiverse(otherScore,newScore,otherState, newState)
        thisWins = (thisWins[0]+w1, thisWins[1]+w2)
    return thisWins

res = rollMultiverse(0,0,player1,player2)
print(res)
print(max(res))
