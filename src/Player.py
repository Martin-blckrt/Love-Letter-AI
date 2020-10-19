class Player:
    def __init__(self, gender, deadpool, isAlive, hand, extraPoint, hasWon, points):

        self.type = gender
        self.deadpool = deadpool  # utilisé quand une personne est protégée par la servante
        self.isAlive = isAlive
        self.playedCards = None
        self.hand = hand
        # self.hand[3] = hand[3]  # le maximum est 3 avec le chancellier
        self.extraPoint = extraPoint
        self.hasWon = hasWon
        self.points = points

    def endRound(self):
        self.points += self.hasWon + (self.isAlive and self.extraPoint)

    def discard(self):
        self.hand[0].insert(0, self.playedCards)
        del self.hand[0]

    def draw(self, **drawTwice):
        cardDrawn = self.deck.pop(0)
        cardDrawn.insert(1, self.hand)

    def compare(self, otherCard):
        if self.hand[0].value < otherCard.hand[0].value:
            return 0
        elif self.hand[0].value > otherCard.hand[0].value:
            return 1
        else:
            result = self.hand[0].value == otherCard.hand[0].value
