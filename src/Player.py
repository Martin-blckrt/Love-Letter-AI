class Player:
    def __init__(self, gender, hasWon, points):

        self.type = gender
        self.deadpool = False           # utilisé quand une personne est protégée par la servante
        self.isAlive = 1                # toujours vrai au début de round
        self.playedCards = []           # liste vide au depart
        self.hand = []                  # liste vide au depart
        self.extraPoint = 0             # Points gagné grâce à l'espionne
        self.hasWon = hasWon
        self.points = points            # Nombre de pts du joueur

    def endRound(self):
        self.points += self.hasWon + (self.isAlive and self.extraPoint)
#TODO. mettre endRound() dans Game

    def discard(self):
        cardDiscarded = self.hand.pop(0)
        cardDiscarded.insert(0, self.playedCards)
        self.draw()

    def playCard(self):
        cardPlayed = self.hand.pop(0)
        cardPlayed.insert(0, self.playedCards)
        # cardPlayed.power(target) qui est la target la?

    def draw(self, deck, **drawTwice):  # doit prendre en parametre la liste deck pour manipuler les cartes du deck
        cardDrawn = deck.pop(0)
        cardDrawn.insert(1, self.hand)

    def compare(self, otherCard):
        if self.hand[0].value < otherCard.hand[0].value:
            return 0
        elif self.hand[0].value > otherCard.hand[0].value:
            return 1
        else:
            result = self.hand[0].value == otherCard.hand[0].value
