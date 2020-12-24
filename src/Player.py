import time
from src.AI.Node import Node, State
from src.AI.NodeToolkit import getAncestorCardIndex
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

    def showdown(self, real=True):
        """
        :param real: check if the turn is virtual or real
        """

        print("\nThe deck is empty : highest card wins !\n")
        i = self.compare(self.opponent, real)

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
        """
        :param opponent: Define opponent of self (a player).
        """
        self.opponent = opponent

    def discard(self, real=True):
        """
        Drop card of the board.
        :param real: check if the turn is virtual or real
        """

        cardDiscarded = self.hand.pop(0)
        self.playedCards.insert(0, cardDiscarded)

        if cardDiscarded.value == 9:
            self.isAlive = False
            print(f"\n{self.name} discarded a Princess !\n" if real else "", end="")

    def playTurn(self, deck, *usedCardIndex, real=True):
        """
         Handles the player's turn & checks for Countess effect
        :param deck: Deck of cards
        :param usedCardIndex: Optional paramater that is used by the AI in a virtualTurn
        :param real: check if the turn is virtual or real
        """

        self.deadpool = False

        if real:
            # cas physique

            self.draw(deck)
            print(f"{self.name}'s hand is :\n" if self.gender == "Human" else "", end="")

            # prints the player's hand
            for i in range(len(self.hand)):
                print(f"{i}. {self.hand[i].title} [{self.hand[i].value}]\n" if self.gender == "Human" else "", end="")

        index = None
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
                    if self.gender == "AI" and real:
                        print("Just a sec ", end="")

                        for j in range(3):
                            print(".", end="")
                            time.sleep(1)

                        print("\n")

        else:

            if real:
                if self.gender == "Human":
                    playerInput = input("\nWhat card do you want to play ? (0/1)\n ")

                    while ((playerInput != '0') and (playerInput != '1')) or len(playerInput) != 1:
                        playerInput = input("\nWrong input ! What card do you want to play ? (0/1)\n")

                    index = int(playerInput)
                else:
                    index = self.playAiTurn(deck)

                    print("Just a sec ", end="")

                    for i in range(3):
                        print(".", end="")
                        time.sleep(1)

                    print("\n")
            else:
                # virtual turn
                index = usedCardIndex[0]

        self.playCard(index, deck, real=real)

    def playCard(self, index, deck, real=True):
        """
        Function : activate cardpower and check immunity.
        :param index: Index of the card in the hand of the player who wants to play
        :param deck: Deck of the game, needed to use the power of the card.
        :param real: Check if the round is virtual or real
        """

        cardPlayed = self.hand.pop(index)

        if real and self.gender == 'AI':
            print(f"The AI played a {cardPlayed.title} !")

        self.playedCards.insert(0, cardPlayed)

        if not self.opponent.deadpool:

            cardPlayed.power(self, deck, real)

        elif self.opponent.deadpool and cardPlayed.value in [1, 2, 3, 7]:

            print(" \nThe opponent is protected : your card has no effect !\n" if real else "", end="")

        elif self.opponent.deadpool and cardPlayed.value in [0, 4, 5, 6, 8, 9]:
            cardPlayed.power(self, deck, real)

        if cardPlayed.value == 9:
            self.isAlive = False

            if real:
                print(f"\n{self.name} played a Princess !")

    def draw(self, deck):
        """
        Makes a player draw a card. Need the game's deck as argument
        :param deck: Deck of the game.
        """

        if deck:

            cardDrawn = deck.pop(0)
            self.hand.append(cardDrawn)

        else:
            print("Deck is empty\n")

    def compare(self, opponent, real=True):
        """
        Function that evaluate which card has the higher value (used when bared is played)
        :param opponent: Opponent of the player who wants to compare hands.
        :param real: Define if the round is virtual or not
        :return: 0 when the value of the card of player is hight than the val. of the card of the opponent, else 1
        """

        print(f"{self.name} has a {self.hand[0].title} [{self.hand[0].value}]\n"
              f"{opponent.name} has a {opponent.hand[0].title} [{opponent.hand[0].value}]\n\n" if real else "", end="")

        if self.hand[0].value < opponent.hand[0].value:
            return 0
        elif self.hand[0].value > opponent.hand[0].value:
            return 1
        else:
            return 2

    def guess(self):
        """
        Function "player only"
        :return: The card that the player want to guess when a guard is played
        """

        playerGuess = input("Which card do you want to guess ? (0-9 but not 1)\n")

        while (playerGuess < '0') or (playerGuess > '9') or (playerGuess == '1') or len(playerGuess) != 1:
            playerGuess = input("Unauthorized input ! Which card do you want to guess ? (0-9 but not 1)\n")

        cardGuessed = int(playerGuess)

        return cardGuessed

    def decide(self):
        """
        Function AI only
        :return: The card that the AI wants to guess
        """

        knownCards = self.isolatedCards + self.hand + self.playedCards
        a = 21 - len(knownCards)
        probabilities = []

        cardToGuess = self.listOfCards[9]  # Default case : you decide to guess a princess

        for Card in self.listOfCards:

            if Card is not self.listOfCards[1]:  # can't guess a guard

                b = Card.totalNumber - knownCards.count(Card)
                value = b / a
                probabilities.append(value)

                if value > max(probabilities):
                    cardToGuess = Card

        if self.playedCards[0].value == 8:
            if (self.listOfCards.prince_card.totalNumber - knownCards.count(self.listOfCards.prince_card)) > 0:
                cardToGuess = self.listOfCards.prince_card
            elif knownCards.count(self.listOfCards.king_card) == 0:
                cardToGuess = self.listOfCards.king_card

        return cardToGuess

    def playAiTurn(self, deck):
        """
        :param deck: The AI need the deck to create a state.
        :return the index of the card that the AI choose to play
        """

        color = 1
        pos_inf = float('inf')
        neg_inf = float('-inf')

        state = State(deck, self.isolatedCards, self.listOfCards, self)
        node = Node(state, 0, None, 0)

        depth = 4

        # Gère l'aspect "iterative deepening" de l'algorithme
        # Permet de compter le nombre de tours passés et d'incrémenter en fonction

        if self.hand[0].value == 9:
            cardIndex = 1

        elif self.hand[1].value == 9:
            cardIndex = 0

        elif self.hand[0].value == self.hand[1].value:
            cardIndex = 0

        elif self.hand[0].value == 1 and self.playedCards[0].value == 8:
            cardIndex = 0

        elif self.hand[1].value == 1 and self.playedCards[0].value == 8:
            cardIndex = 1

        else:
            negaValue = negamax(node, depth, neg_inf, pos_inf, color)
            node.value = negaValue

            cardIndex = getAncestorCardIndex(node, negaValue)

        return cardIndex
