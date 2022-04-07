import random

class ComputerStrategy:
    '''Specifies Computer's Turns'''

    #b and board = player's board
    def __init__(self, b):
        self.board = b

    #MAKE WIN STRATEGY OF THE ENEMY COMPUTER HERE
    def turn(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.board[x + 1][y].cget("text") != "X" and self.board[x + 1][y].cget("bg") != "red":
                if self.board[x + 1][y].cget("bg") == "blue":
                    self.board[x + 1][y].config(bg="red")
                    return 1
                else:
                    self.board[x + 1][y].config(text="X")
                    return 0
