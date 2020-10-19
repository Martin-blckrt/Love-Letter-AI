import Card


class Player:
    def __init__(self, type, deadpool, isAlive, hand, deck, extraPoint, hasWon, points):

        self.type = type
        self.deadpool = deadpool  # utilisé quand une personne est protégée par la servante
        self.isAlive = isAlive
        self.playedCards = None
        self.hand = None
        # self.hand[3] = hand[3]  # le maximum est 3 avec le chancellier
        self.deck[15] = deck[15]  # il y a 15 cartes au start (21-4-1-1)
        # TODO.  deck[] à deplacer dans le main car il ne faut pas que chaque joueur ai un deck

        self.extraPoint = extraPoint
        self.hasWon = hasWon
        self.points = points

    def endRound(self):
        self.points += self.hasWon + (self.isAlive and self.extraPoint)

    def discard(self):
        self.hand[0].insert(0, self.playedCards)
        del self.hand[0]

    def draw(self, **drawTwice):
        self.deck[0].insert(1, self.hand)

    def compare(self, otherCard):
        if self.hand[0].value < otherCard.hand[0].value:
            return 0
        elif self.hand[0].value > otherCard.hand[0].value:
            return 1
        else:
            self.hand[0].value == otherCard.hand[0].value


# TODO. créer les instances dans le main, pas besoin de le faire ici


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
