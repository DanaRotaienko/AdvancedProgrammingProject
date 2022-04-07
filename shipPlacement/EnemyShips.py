import random


class EnemyShips:

    def __init__(self):
        self.ships = self.falseShips()

    def falseShips(self):
        shps = []
        for x in range(0, 10):
            shps.insert(x, [])
            for y in range(0, 10):
                shps[x].insert(y, False)
        return shps

    def chooseRandomCoordinates(self, numOfDeck, ships):
        result = False
        while not result:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            result = self.checkCells(x, y, numOfDeck, ships)
        self.ships = result
        return result

    def checkCells(self, x, y, numOfDeck, ships):
        xOrY = ['x', 'y']
        fOrB = ['f', 'b']
        axis = xOrY[random.randint(0, 1)]
        direction = fOrB[random.randint(0, 1)]

        if x >= (10 - numOfDeck) and y >= (10 - numOfDeck):
            return self.chooseCoordinates(x, y, axis, 'b', 'b', numOfDeck, ships)
        elif x == 0 and y == 0:
            return self.chooseCoordinates(x, y, axis, 'f', 'f', numOfDeck, ships)
        elif x >= 10 - numOfDeck:
            return self.chooseCoordinates(x, y, axis, 'b', direction, numOfDeck, ships)
        elif y >= 10 - numOfDeck:
            return self.chooseCoordinates(x, y, axis, direction, 'b', numOfDeck, ships)
        elif x == 0:
            return self.chooseCoordinates(x, y, axis, 'f', direction, numOfDeck, ships)
        elif y == 0:
            return self.chooseCoordinates(x, y, axis, direction, 'f', numOfDeck, ships)
        else:
            return self.chooseCoordinates(x, y, axis, direction, direction, numOfDeck, ships)


    def chooseCoordinates(self, x, y, axis, direction1, direction2, numOfDeck, ships):
        if axis == 'x':
            if direction1 == 'f' and self.checkIfCellIsTaken(x, y, axis, direction1, direction2, numOfDeck, ships):
                for i in range(0, numOfDeck):
                    ships[x + i][y] = True
            elif direction1 == 'b' and self.checkIfCellIsTaken(x, y, axis, direction1, direction2, numOfDeck, ships):
                for i in range(0, numOfDeck):
                    ships[x - i][y] = True
            else:
                return False
        elif axis == 'y':
            if direction2 == 'f' and self.checkIfCellIsTaken(x, y, axis, direction1, direction2, numOfDeck, ships):
                for i in range(0, numOfDeck):
                    ships[x][y + i] = True
            elif direction2 == 'b' and self.checkIfCellIsTaken(x, y, axis, direction1, direction2, numOfDeck, ships):
                for i in range(0, numOfDeck):
                    ships[x][y - i] = True
            else:
                return False
        return ships


    def checkNeighbourCells(self, ships, x, y):
        isFree = True
        if x == 0:
            if y == 0:
                if ships[x + 1][y] or ships[x][y + 1]:
                    isFree = False
            elif y == 9:
                if ships[x + 1][y] or ships[x][y - 1]:
                    isFree = False
            else:
                if ships[x + 1][y] or ships[x][y + 1] or ships[x][y - 1]:
                    isFree = False
        elif x == 9:
            if y == 0:
                if ships[x - 1][y] or ships[x][y + 1]:
                    isFree = False
            elif y == 9:
                if ships[x - 1][y] or ships[x][y - 1]:
                    isFree = False
            else:
                if ships[x - 1][y] or ships[x][y + 1] or ships[x][y - 1]:
                    isFree = False
        elif y == 0:
            if ships[x][y + 1] or ships[x + 1][y] or ships[x - 1][y]:
                isFree = False
        elif y == 9:
            if ships[x][y - 1] or ships[x + 1][y] or ships[x - 1][y]:
                isFree = False
        else:
            if ships[x + 1][y] or ships[x - 1][y] or ships[x][y + 1] or ships[x][y - 1]:
                isFree = False
        return isFree

    def checkIfCellIsTaken(self, x, y, axis, direction1, direction2, numOfDeck, ships):
        isFree = self.checkNeighbourCells(ships, x, y)
        if not isFree:
            return isFree
        if axis == 'x':
            if direction1 == 'f':
                for i in range(0, numOfDeck):
                    if ships[x + i][y]:
                        isFree = False
            elif direction1 == 'b':
                for i in range(0, numOfDeck):
                    if ships[x - i][y]:
                        isFree = False
        elif axis == 'y':
            if direction2 == 'f':
                for i in range(0, numOfDeck):
                    if ships[x][y + i]:
                        isFree = False
            elif direction2 == 'b':
                for i in range(0, numOfDeck):
                    if ships[x][y - i]:
                        isFree = False
        return isFree

    def setComputerShips(self):
        for i in range(2):
            self.ships = self.chooseRandomCoordinates(3, self.ships)
        for i in range(3):
            self.ships = self.chooseRandomCoordinates(2, self.ships)
        for i in range(4):
            self.ships = self.chooseRandomCoordinates(1, self.ships)
        return self.ships
