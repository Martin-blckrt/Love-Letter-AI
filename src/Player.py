class Player:
    def __init__(self, name, gender):

        self.gender = gender
        self.deadpool = False  # utilisé quand une personne est protégée par la servante
        self.isAlive = True  # toujours vrai au début de round
        self.playedCards = []  # liste vide au depart
        self.hand = []  # liste vide au depart
        self.extraPoint = 0  # Points gagné grâce à l'espionne
        self.hasWon = 0
        self.points = 0  # Nombre de pts du joueur
        self.name = name  # Nom du jour
        self.opponent = None

    def oppositePlayer(self, opponent):
        self.opponent = opponent

    def discard(self):
        cardDiscarded = self.hand.pop(0)
        self.playedCards.insert(0, cardDiscarded)

        if cardDiscarded.value == 9:
            self.isAlive = False

    def playTurn(self, deck):
        self.deadpool = False
        self.draw(deck)

        print(f"{self.name}'s hand is :")

        for i in range(len(self.hand)):
            print(f"{i+1}. {self.hand[i].title} [{self.hand[i].value}]")

        cardValues = []

        for j in range(len(self.hand)):
            cardValues.append(self.hand[j].value)

        if (8 and (5 or 7)) in cardValues:
            for i in range(len(self.hand)):
                if cardValues[i] == 8:
                    index = i+1
        else:
            index = int(input("\nWhat card do you want to play ? 1/2\n"))

        self.playCard(index-1, deck)

    def playCard(self, index, deck):

        cardPlayed = self.hand.pop(index)

        if not self.opponent.deadpool:
            cardPlayed.power(self, deck)

        self.playedCards.insert(0, cardPlayed)

        if cardPlayed.value == 9:
            self.isAlive = False

    def draw(self, deck):  # doit prendre en parametre la liste deck pour manipuler les cartes du deck
        if deck:
            cardDrawn = deck.pop(0)
            self.hand.append(cardDrawn)
        else:
            print("Deck is empty")

    def compare(self, opponent):
        if self.hand[0].value < opponent.hand[0].value:
            return 0
        elif self.hand[0].value > opponent.hand[0].value:
            return 1
        else:
            return 2

    def guess(self):
        cardGuessed = int(input("Which card do you want to guess ? (0-9)\n"))
        return cardGuessed

    def decide(self):
        # IA magic shit
        pass
