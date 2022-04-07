import tkinter as tk
from tkinter import *
from tkinter import ttk

from shipPlacement import DeckPlace as dp
from moves import Turns as t
from visualisation import DeckLabel as dl

class View:
    """Main class"""
    def __init__(self):
        self.player = [[]]
        self.enemy = [[]]
        self.win = tk.Tk()
        self.win.geometry("790x640+200+0")
        self.win.title("BattleShip from Dana and Eduard")
        self.win.config(bg='#fffcf2')
        self.decks = []
        self.action = tk.Label(self.win, text="Locate Your Ships: ", font=("Marker Felt", 18), fg="#0f0f99", bg='#fffcf2')
        self.stage = tk.Label(self.win, text="Please, place your ships", font=("Marker Felt", 30), fg="#0f0f99", justify=CENTER, bg='#fffcf2')
        self.dPlace = dp.DeckPlace(self.player, self.decks, self.action, self.stage)
        self.turns = t.Turns(self.enemy, self.player, self.action, self.stage)
        self.restart = ttk.Button(self.win, text="Restart", style='button.TButton', width=7) # restart the game

    # checks if the button on any board is pressed and trigger actions
    def placeDeck(self, buttn, i, j, board):
        # for game turns after the user placed his ships
        if self.dPlace.isComplete() and not self.enemy[i + 1] [j].cget("text") == "X":
            self.turns.playerTurn(i, j)

        # for the user setting ships on the board
        elif buttn.cget('fg')=='black':
            self.dPlace.handle(i + 1, j)

    # returns the pre-configured button object
    def getButton(self, x, y, board, b):
        button = Button(self.win, text="", bg="lightblue", fg=b, highlightbackground='lightblue',
                        activeforeground="grey", height="1", width="3")
        button.config(command=lambda buttn = button, b=board: self.placeDeck(buttn, y, x, b))
        return button

    # locate buttons on both boards
    def set(self, board, xMargin, b):
        yMargin = 130
        for y in range(10):
            plX = []
            for i in range(10):
                b1 = self.getButton(i, y, board, b)
                b1.place(x=str(xMargin + 30*i), y=str(yMargin + 25*y))
                plX.append(b1)
            board.append(plX)

    def setAll(self):
        self.set(self.player, 50, 'black')
        self.set(self.enemy, 435, 'blue')

    ## To center window, but doesn't work on Mac screen
    ## win.eval('tk::PlaceWindow . center')

    # Styles

    # Functions
    def quit(self):
        self.win.destroy()

    def setBackground(self):
        ttk.Style().configure('button.TButton', foreground='#0f0f99', background='#0f0f99', font=("Herculanum", 20), bg='#fffcf2') # doesn't change background colour

        ## Stage label

        self.stage.grid(row=0, column=1, columnspan=4, pady=10)

        ## Frames

        userBoard = tk.LabelFrame(self.win, text="Your ships", font=("Herculanum", 15), fg="#0f0f99", height=320, width=380, labelanchor='n', bg='#fffcf2')
        # labelanchor - to specify label position
        enemyBoard = tk.LabelFrame(self.win, text="Enemy's ships", font=("Herculanum", 15), fg="#0f0f99", height=320, width=380, labelanchor='n', bg='#fffcf2')
        userBoard.grid(row=1, column=1, columnspan=2, pady=20, padx=10)
        enemyBoard.grid(row=1, column=3, columnspan=2, pady=20)

        # Actions labels (ships to place)
        self.action.grid(row=3, column=1)

        for i in range(3):
            self.decks.append(dl.DeckLabel(self.win, 3 - i))
            self.decks[i].deck.grid(row=4 + i, column=1)
            self.decks[i].deckCheck.grid(row=4 + i, column=2)

        # Bottom (restart && quit button)

        self.restart.grid(row=7, column=3)
        quit = ttk.Button(self.win, text="Quit", style='button.TButton', width=7, command=self.quit)
        quit.grid(row=7, column=4)

    def start(self):
        self.setBackground()
        self.setAll()
        self.win.mainloop()
