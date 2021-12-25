from day21_data import *
import itertools

state = [player1,player2]
score = [0,0]
turn = False

def rollDice():
    gen = itertools.cycle(range(1,101))
    while True:
        yield [next(gen) for _ in range(3)]

count = 0
for roll in rollDice():
    count += 3
    state[int(turn)] = 1+((state[int(turn)]+sum(roll)-1)%10)
    score[int(turn)] += state[int(turn)]
    if score[int(turn)] >= 1000:
        print(score[int(not turn)])
        print(count)
        print(count*score[int(not turn)])
        break

    turn = not turn
