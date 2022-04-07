import tkinter as tk


class DeckLabel:
    '''Labels of how many ships of diff decks are remained to located'''

    def __init__(self, win, d):
        # x-Deck ship sign
        self.deck = tk.Label(win, text="", font=("Herculanum", 15), fg="#0f0f99", bg='#fffcf2')
        # [] currently considering coursor
        self.deckCheck = tk.Label(win, text="", font=("Herculanum", 20), fg="red", bg='#fffcf2')
        self.text = str(d) + "-Deck ship: "
        self.qty = 5 - d
        self.deck.config(text=self.text + str(self.qty))

    # Reduces the number of ships of the certain decks if selected by the user
    def reduce(self):
        if self.qty == 0:
            return False
        self.qty -= 1
        self.deck.config(text=self.text + str(self.qty))
        return True

    # remove the ships with decks to locate signs after location is completed
    def clear(self):
        self.deck.config(text="")
