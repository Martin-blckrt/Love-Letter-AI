class Player:
    def __init__(self, name, gender):

        self.type = gender
        self.deadpool = False  # utilisé quand une personne est protégée par la servante
        self.isAlive = True  # toujours vrai au début de round
        self.playedCards = []  # liste vide au depart
        self.hand = []  # liste vide au depart
        self.extraPoint = 0  # Points gagné grâce à l'espionne
        self.hasWon = 0
        self.points = 0  # Nombre de pts du joueur
        self.name = name  # Nom du jour

    def discard(self):
        cardDiscarded = self.hand.pop(0)
        cardDiscarded.insert(0, self.playedCards)
        if cardDiscarded.value == 9:
            self.isAlive = False
        self.draw(deck)

    def playCard(self, index, *target):
        cardPlayed = self.hand.pop(index)
        cardPlayed.power(*target)
        cardPlayed.insert(0, self.playedCards)

    def draw(self, deck):  # doit prendre en parametre la liste deck pour manipuler les cartes du deck
        cardDrawn = deck.pop(0)
        cardDrawn.append(self.hand)

    def compare(self, otherPlayer):
        if self.hand[0].value < otherPlayer.hand[0].value:
            return 0
        elif self.hand[0].value > otherPlayer.hand[0].value:
            return 1
        else:
            return 2


    def guess(self):
        cardGuessed = input("What card do you want to guess ? (0-9)")
        return cardGuessed

    def decide(self):
        # IA magic shit
        pass
