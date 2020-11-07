class Player:
    def __init__(self, name, gender, id):

        self.type = gender
        self.deadpool = False  # utilisé quand une personne est protégée par la servante
        self.isAlive = True  # toujours vrai au début de round
        self.playedCards = []  # liste vide au depart
        self.hand = []  # liste vide au depart
        self.extraPoint = 0  # Points gagné grâce à l'espionne
        self.hasWon = 0
        self.points = 0  # Nombre de pts du joueur
        self.name = name  # Nom du jour
        self.id = id

    def oppositePlayer(self):
        return not self.id

    def discard(self):
        cardDiscarded = self.hand.pop(0)
        self.playedCards.insert(0, cardDiscarded)
        if cardDiscarded.value == 9:
            self.isAlive = False

    def playTurn(self, deck, opponent):
        self.deadpool = False
        self.draw(deck)
        for i in range(len(self.hand)):
            print(self.hand[i].title, "[", self.hand[i].value, "]\n")

        index = int(input("what card do you want to play ? O/1\n"))
        temp = int(input("who do you want to target ? 1/2\n"))

        if temp == 1:
            target = self
        else:
            target = opponent
        self.playCard(index, target)

    def playCard(self, index, target):
        cardPlayed = self.hand.pop(index)
        cardPlayed.power(target)
        self.playedCards.insert(0, cardPlayed)

    def draw(self, deck):  # doit prendre en parametre la liste deck pour manipuler les cartes du deck
        cardDrawn = deck.pop(0)
        self.hand.append(cardDrawn)

    def compare(self, opponent):
        if self.hand[0].value < opponent.hand[0].value:
            return 0
        elif self.hand[0].value > opponent.hand[0].value:
            return 1
        else:
            return 2

    def guess(self):
        cardGuessed = input("What card do you want to guess ? (0-9)")
        return cardGuessed

    def decide(self):
        # IA magic shit
        pass
