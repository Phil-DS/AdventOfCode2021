from day4_data import *
import sys

# Time to OOP the s*** of the problem. Board object

class Board:
    def __init__(self, board) -> None:
        self.board = board
        # Masks and counts.
        self.done = [[1 for _ in range(5)] for _ in range(5)]
        self.doneX = [0 for _ in range(5)]
        self.doneY = [0 for _ in range(5)]


    def fillNumber(self, n):
        for i in range(5):
            for j in range(5):
                if self.board[j][i] == n:
                    # Mask bit
                    self.done[j][i] = 0
                    
                    self.doneX[j] += 1
                    # Check X
                    if(self.doneX[j] == 5):
                        return self.board[j]
                    
                    self.doneY[i] += 1
                    # Check Y
                    if(self.doneY[i] == 5):
                        return [self.board[k][i] for k in range(5)]
        return None

madeBoards = {Board(b) for b in boards}
for x in run:
    for board in madeBoards:
        # If we have some return
        l = board.fillNumber(x)
        if l:
            c=0
            for i in range(5):
                for j in range(5):
                    # Mask the filled squares with magic and sum them
                    c+=board.board[j][i] * board.done[j][i]
            # and the final value
            print(c*x)
            sys.exit()