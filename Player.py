import Card

class Player:
    def __init__(self):
        self.type
        self.deadpool
        self.isAlive
        self.playedCards[None]
        self.hand[3] #le maximum est 3 avec le chancellier
        self.deck[15] #il y a 15 cartes au start (21-4-1-1)
        #ATTENTION ! DECK DOIT PAS ETRE COLLECTIF
        self.extraPoint
        self.hasWon
        self.points

    def endRound(self):
        self.points += self.hasWon + (self.isAlive and self.extraPoint)

    def discard(self):
        self.hand[0].insert(0, self.playedCards)
        del self.hand[0]

    def draw(self, **drawTwice):
        self.deck[0].insert(1, self.hand)

    def compare(self, otherCard):
        if self.hand[0].value < otherCard.hand[0].value
            return 0
        elif self.hand[0].value > otherCard.hand[0].value
            return 1
        else:
            self.hand[0].value == otherCard.hand[0].value


class Player1(Player):
    def __init__(self):
        self.type = "human"
        self.deadpool = False
        self.isAlive = True
        self.playedCards = []
        self.hand = ["une carte"]
        self.extraPoint = False
        self.hasWon = False
        self.points = 0


Player1 = Player1()


class Player2(Player):
    def __init__(self):
        self.type = "human"
        self.deadpool = False
        self.isAlive = True
        self.playedCards = []
        self.hand = ["une carte"]
        self.extraPoint = False
        self.hasWon = False
        self.points = 0


Player2 = Player2()