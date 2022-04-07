
class DeckPlace:
    '''Algorythm to locate ships on the player's board'''
    def __init__(self, b, d, act, stg):
        self.board = b
        # 3-deck, 2-deck and 1-deck ships remaining
        self.placed = [2, 3, 4]
        # DeckLabel objects (array)
        self.decks = d
        # checks of 2- and 3- deck ships are allowed to locate at this turn
        self.oneDeck = True
        self.twoDeck = True
        self.threeDeck = True
        # checks if the location is not completed
        self.notEnd = True
        # To limit joining 2nd Deck to the 1st or 3d Deck to the 2nd (and not to any other ship on the board)
        self.TreeTwoDeckFirst = [100, 100]
        # 3-Deck can join both sides, therefore, the second instance
        self.TreeDeckSecond = [100, 100]
        self.action = act
        self.stage = stg

    #Manages in DeckLabel location of [] coursor
    def coursor(self):
        for i in range(3):
            self.decks[i].deckCheck.config(text="")
        if self.placed[0] > 0:
            self.decks[0].deckCheck.config(text="[ ]")
        elif self.placed[1] > 0:
            self.decks[1].deckCheck.config(text="[ ]")
        elif self.placed[2] > 0:
            self.decks[2].deckCheck.config(text="[ ]")

    # checks if the end of location and signs needs to be changed
    def counting(self):
        if self.placed[0] == 0 and self.placed[1] == 0 and self.placed[2] == 0:
            self.notEnd = False
            self.action.config(text="Your turn")
            self.stage.config(text="Battle is now ON")
            for i in range(3):
                self.decks[i].clear()

    # Checks how many surrounding fields at the board of the player are marked as located
    # with a deck. If zero, means the selected field has no surrounding decks already located.
    # Do not consider diagonal / artogonal locations subject to separate function
    def isNext(self, x, y):
        count = 0
        if x < 10 and self.board[x + 1][y].cget('bg') == 'blue':
            count += 1
        if y < 9 and self.board[x][y + 1].cget('bg') == 'blue':
            count += 1
        if x > 1 and self.board[x - 1][y].cget('bg') == 'blue':
            count += 1
        if y > 0 and self.board[x][y - 1].cget('bg') == 'blue':
            count += 1
        return count

    #Ensures 3d deck of 3-Deck ship or 2nd for 2-Deck are placed near the first two (one) and not close to another ship
    def isTreeTwoDeckNext(self, x, y):
        if abs(x - self.TreeTwoDeckFirst[0]) == 1 and y == self.TreeTwoDeckFirst[1]:
            return True
        if abs(y - self.TreeTwoDeckFirst[1]) == 1 and x == self.TreeTwoDeckFirst[0]:
            return True
        if abs(x - self.TreeDeckSecond[0]) == 1 and y == self.TreeDeckSecond[1]:
            return True
        if abs(y - self.TreeDeckSecond[1]) == 1 and x == self.TreeDeckSecond[0]:
            return True
        return False

    # Checks if by pressing the button the user can locate a ship-deck
    # Makes amendments to the respective counting if success
    def isShip(self, x, y):
        if self.isNext(x, y) > 1:
            return False
        if self.isNext(x, y) == 0:
            # 1-Deck
            if self.placed[2] > 0:
                # Actual 1-Deck and not 1st Deck of 2 or 3 Deck ship
                if self.placed[0] == 0 and self.placed[1] == 0:
                    self.placed[2] -= 1
                    self.decks[2].reduce()
                    self.coursor()
                    return True
                # 1st Deck of 2-Deck or 3-Deck ship
                elif self.oneDeck:
                    self.oneDeck = False
                    self.TreeTwoDeckFirst = [x, y]
                    # Allows 2-Deck ship for next time when 3-Deck is finished
                    if self.placed[0] > 0:
                        self.twoDeck = True
                    self.coursor()
                    return True
        # 2-Deck
        elif self.isNext(x, y) == 1 and self.placed[1] > 0 and not self.oneDeck and self.isTreeTwoDeckNext(x, y):
            # Actual 2-Deck and not 2nd Deck of 3-Deck ship
            if self.placed[0] == 0:
                self.placed[1] -= 1
                self.decks[1].reduce()
                self.coursor()
                self.oneDeck = True
                self.TreeTwoDeckFirst = [100, 100]
                return True
            # 2nd Deck of 3-Deck ship
            elif self.twoDeck:
                self.twoDeck = False
                self.coursor()
                self.threeDeck = True
                self.TreeDeckSecond = [x, y]
                return True
        # 3-Deck
        if self.placed[0] > 0 and self.isNext(x, y) == 1 and self.threeDeck and self.isTreeTwoDeckNext(x, y):
            self.placed[0] -= 1
            self.decks[0].reduce()
            self.coursor()
            self.oneDeck = True
            self.twoDeck = False
            self.threeDeck = False
            self.TreeTwoDeckFirst = [100, 100]
            self.TreeDeckSecond = [100, 100]
            return True
        return False

    # Checks if the prospective deck would not have diagonal / arthogonal interaction
    # with other decks on the board
    def isAngular(self, x, y):
        if y > 0 and x > 1 and self.board[x - 1][y - 1].cget('bg') == 'blue':
            return False
        if y < 9 and x < 10 and self.board[x + 1][y + 1].cget('bg') == 'blue':
            return False
        if y > 0 and x < 10 and self.board[x + 1][y - 1].cget('bg') == 'blue':
            return False
        if y < 9 and x > 1 and self.board[x - 1][y + 1].cget('bg') == 'blue':
            return False
        return True

    # main function after the user presses the button in his board
    def handle(self, x, y):
        if self.board[x][y].cget('bg') != 'blue' \
                and self.notEnd \
                and self.isAngular(x, y):
            if self.isShip(x, y):
                self.counting()
                self.board[x][y].config(bg='blue', highlightbackground='blue')

    def isComplete(self):
        return not self.notEnd
