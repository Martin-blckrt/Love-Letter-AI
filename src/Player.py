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

    def deckEmpty(self, opponent):
        self.opponent = opponent
        print("\nThe deck is empty : highest card wins !")
        if self.compare(opponent) == 0:
            opponent.hasWon = True
            print(f"{opponent.name} wins !")
        elif self.compare(opponent) == 1:
            self.hasWon = True
            print(f"{self.name} wins !")
        else:
            self.hasWon = opponent.hasWon = True
            print("Tie")

    def oppositePlayer(self, opponent):
        self.opponent = opponent

    def discard(self):
        cardDiscarded = self.hand.pop(0)
        self.playedCards.insert(0, cardDiscarded)

        if cardDiscarded.value == 9:
            self.isAlive = False
            print(f"\n{self.name} discarded a Princess !\n")

    def playTurn(self, deck):
        self.deadpool = False
        self.draw(deck)

        print(f"{self.name}'s hand is :")

        for i in range(len(self.hand)):
            print(f"{i+1}. {self.hand[i].title} [{self.hand[i].value}]")

        index =0

        cardValues = []

        for j in range(len(self.hand)):
            cardValues.append(self.hand[j].value)

        cond5 = 5 in cardValues
        cond7 = 7 in cardValues
        cond8 = 8 in cardValues

        if cond8 and (cond5 or cond7):
            for i in range(len(self.hand)):
                if cardValues[i] == 8:
                    index = i+1
                    print("\nThe countess was discarded !\n")
        else:
            index = int(input("\nWhat card do you want to play ? 1/2\n"))
            while (index != 1) and (index != 2):
                index = int(input("\nWrong input ! What card do you want to play ? 1/2\n"))

        self.playCard(index-1, deck)

    def playCard(self, index, deck):

        cardPlayed = self.hand.pop(index)

        if not self.opponent.deadpool:
            if cardPlayed.value == 5 and not deck:#TODO. check si y a besoin de cette ligne
                pass
            else:
                cardPlayed.power(self, deck)
        else:
            print("\nThe opponent is protected : your card has no effect !\n")

        self.playedCards.insert(0, cardPlayed)



        if cardPlayed.value == 9:
            self.isAlive = False
            print(f"\n{self.name} played a Princess !\n")

    def draw(self, deck):  # doit prendre en parametre la liste deck pour manipuler les cartes du deck
        if deck:
            cardDrawn = deck.pop(0)
            self.hand.append(cardDrawn)
        else:
            print("Deck is empty\n")

    def compare(self, opponent):
        print(f"{self.name} has a {self.hand[0].title} [{self.hand[0].value}]\n"
              f"{opponent.name} has a {opponent.hand[0].title} [{opponent.hand[0].value}]")
        if self.hand[0].value < opponent.hand[0].value:
            return 0
        elif self.hand[0].value > opponent.hand[0].value:
            return 1
        else:
            return 2

    def guess(self):
        cardGuessed = int(input("Which card do you want to guess ? (0-9 but not 1)\n"))
        while(cardGuessed < 0) or (cardGuessed > 9) or (cardGuessed == 1):
            cardGuessed = int(input("Unauthroized value ! Which card do you want to guess ? (0-9 but not 1)\n"))
        return cardGuessed

    def decide(self):
        # IA magic shit
        pass
