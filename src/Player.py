# -------------------------
#  Defini template de Player.
# -------------------------

from src.AI.Node import Node, State
from src.AI.negamax import negamax


class Player:

    def __init__(self, name, gender, hiddenCard, isolatedCards, listOfCards):

        self.gender = gender
        self.deadpool = False  # Activates immunity when the Handmaid is played
        self.isAlive = True  # Always True at the start. Tells us if the player is alive
        self.playedCards = []  # List of the card that have been played. Empty at the start
        self.hand = []  # Player's hand. Empty at the beginning
        self.extraPoint = 0  # Extra point given by the Spy
        self.hasWon = 0  # Always False at the start. Tells us if the player has won
        self.points = 0  # Player's total points
        self.name = name  # Player's name
        self.opponent = None  # Contains the player's opponent
        self.hiddenCard = hiddenCard
        self.isolatedCards = isolatedCards
        self.listOfCards = listOfCards

    def deckEmpty(self):
        # Activates when they are no more card left

        print("\nThe deck is empty : highest card wins !")
        i = self.compare(self.opponent)

        if i == 0:

            self.opponent.hasWon = True
            print(f"{self.opponent.name} wins !")

        elif i == 1:

            self.hasWon = True
            print(f"{self.name} wins !")

        else:
            self.hasWon = self.opponent.hasWon = True
            print("Tie")

    def oppositePlayer(self, opponent):
        # Assign the opponent of the player

        self.opponent = opponent

    def discard(self, caption=True):
        # Drops a player's card on the board

        cardDiscarded = self.hand.pop(0)
        self.playedCards.insert(0, cardDiscarded)

        if cardDiscarded.value == 9:
            self.isAlive = False
            print(f"\n{self.name} discarded a Princess !\n" if caption else None)

    def playTurn(self, deck, *usedCardIndex, caption=True):
        # Handles the player's turn. Checks for Countess effect

        self.deadpool = False
        self.draw(deck)

        if caption:
            print(f"{self.name}'s hand is :")

            for i in range(len(self.hand)):
                print(f"{i}. {self.hand[i].title} [{self.hand[i].value}]")  # prints the player's hand

        index = 0
        cardValues = []

        for j in range(len(self.hand)):
            cardValues.append(self.hand[j].value)

        cond5 = 5 in cardValues  # detects a Prince
        cond7 = 7 in cardValues  # detects a King
        cond8 = 8 in cardValues  # detects a Countess

        if cond8 and (cond5 or cond7):

            for i in range(len(self.hand)):

                if cardValues[i] == 8:
                    index = i

                    print("\nThe countess was discarded !\n" if caption else None)
        else:

            if caption and self.gender == "Human":

                index = int(input("\nWhat card do you want to play ? (0/1)\n "))

                while (index != 0) and (index != 1):
                    index = int(input("\nWrong input ! What card do you want to play ? (0/1)\n"))

            elif caption and self.gender == "IA":

                index = self.playAiTurn(deck)

            else:
                index = usedCardIndex[0]

        self.playCard(index, deck, caption=caption)

    def playCard(self, index, deck, caption=True):
        # Activates the card's power. Checks for immunity

        cardPlayed = self.hand.pop(index)

        if not self.opponent.deadpool:

            cardPlayed.power(self, deck)

        elif self.opponent.deadpool and cardPlayed.value in [1, 2, 3, 7]:

            if caption:
                print(" \nThe opponent is protected : your card has no effect !\n")

        elif self.opponent.deadpool and cardPlayed.value in [0, 4, 5, 6, 8, 9]:
            cardPlayed.power(self, deck)

        self.playedCards.insert(0, cardPlayed)

        if cardPlayed.value == 9:
            self.isAlive = False

            if caption:
                print(f"\n{self.name} played a Princess !\n")

    def draw(self, deck):

        # Pas besoin de caption parce que draw dans nextstate.

        # Makes a player draw a card. Need the game's deck as argument
        if deck:

            cardDrawn = deck.pop(0)
            self.hand.append(cardDrawn)

            if self.gender == 'AI':
                cardDrawn.leftNumber -= 1

        else:
            print("Deck is empty\n")

    def compare(self, opponent, caption=True):
        # Function who evaluates which card has greater value

        print(f"{self.name} has a {self.hand[0].title} [{self.hand[0].value}]\n"
              f"{opponent.name} has a {opponent.hand[0].title} [{opponent.hand[0].value}]\n" if caption else None)

        if self.hand[0].value < opponent.hand[0].value:
            return 0
        elif self.hand[0].value > opponent.hand[0].value:
            return 1
        else:
            return 2

    def guess(self):
        # Function who makes the player guess a card (Guard effect - Player only)

        cardGuessed = int(input("Which card do you want to guess ? (0-9 but not 1)\n"))

        while (cardGuessed < 0) or (cardGuessed > 9) or (cardGuessed == 1):
            cardGuessed = int(input("Unauthorized value ! Which card do you want to guess ? (0-9 but not 1)\n"))

        return cardGuessed

    def playAiTurn(self, deck):

        color = 1
        pos_inf = float('inf')
        neg_inf = float('-inf')

        state = State(deck, self.isolatedCards, self.listOfCards, self)
        node = Node(state, 0, None)

        depth = len(self.playedCards)+2
        #Permet de compter le nombre de tours passés et d'incrémenter en fonction
        index = negamax(node, depth, neg_inf, pos_inf, color)
        return index

    def decide(self):
        # TODO. ecrire decide pour guess pour guard
        pass
