from day4_data import *
import sys
import numpy as np

# Same as day 1, but with some extras

class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.done = [[1 for _ in range(5)] for _ in range(5)]
        self.doneX = [0 for _ in range(5)]
        self.doneY = [0 for _ in range(5)]
        # New - Added finish flag
        self.isFinished = False


    def fillNumber(self, n):
        for i in range(5):
            for j in range(5):
                if self.board[j][i] == n:
                    self.done[j][i] = 0
                    self.doneX[j] += 1
                    if(self.doneX[j] == 5):
                        self.isFinished = True
                        return self.board[j]
                        
                    self.doneY[i] += 1
                    if(self.doneY[i] == 5):
                        self.isFinished = True
                        return [self.board[k][i] for k in range(5)]
        return None

madeBoards = [Board(b) for b in boards]

for x in run:
    for board in madeBoards:
        board.fillNumber(x)
    # With the boards now keeping themselves finished or not by the bit, new logic
    # Check if its not the last board
    if len(madeBoards) > 1:
        # Filter the finished boards
        madeBoards = [m for m in madeBoards if not m.isFinished]
        
    # only do this if the last board is complete
    elif madeBoards[0].isFinished:
        # Same summation as the first board.
        c=0
        for i in range(5):
            for j in range(5):
                c+=madeBoards[0].board[j][i] * madeBoards[0].done[j][i]

        # And the final value
        print(c*x)
        sys.exit()