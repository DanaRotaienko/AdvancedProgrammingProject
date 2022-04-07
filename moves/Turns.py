from moves import ComputerStrategy as cs
from shipPlacement import EnemyShips as es


class Turns:
    '''Handle user's and computer turns'''
    def __init__(self, eb, b, act, stg):
        # The issue in late Turns init that results in broken functions and empty enemyBoard
        self.enemyBoard = eb
        self.computerTurn = cs.ComputerStrategy(b)
        #LOCATE ENEMY SHIPS HERE
        self.enemyBool = es.EnemyShips().setComputerShips()
        self.playersVictory = 16
        self.enemysVictory = 16
        #Top sign (Game stage)
        self.action = act
        #Buttom sign (Game result)
        self.stage = stg

    def checkTheWinner(self):
        if self.playersVictory == 0 or self.enemysVictory == 0:
            self.stage.config(text="Game is Over")
            if self.playersVictory == 0:
                self.action.config(text="You are the Winner, CONGRATS!")
            else:
                self.action.config(text="You loose, GET BETTER NEXT TIME!")

    # main logic after the user makes a turn
    def playerTurn(self, x, y):
        if self.enemyBoard[x + 1][y].cget("text") != "X" and self.enemyBoard[x + 1][y].cget("bg") != "red" \
                and self.playersVictory > 0 and self.enemysVictory > 0:
            if self.enemyBool[x][y]:
                self.enemyBoard[x + 1][y].config(bg="red", highlightbackground="red")
                self.playersVictory -= 1
                self.action.config(text="Lucky, your turn again!")
            else:
                self.enemyBoard[x + 1][y].config(text="X")
                self.enemysVictory -= self.computerTurn.turn()
                self.action.config(text="Your Turn")
        self.checkTheWinner()
