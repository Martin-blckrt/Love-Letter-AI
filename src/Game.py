# -----------------------------------
# la classe Game et ses methodes.
#
# -----------------------------------
import random
from src.Player import Player
from src.Card import Card


def initGame(name1, name2):
    """
    Initialize game
    :param name1: name of player 1
    :param name2: name of player 2
    :return: return the instance of the game that has been created.
    """
    # Initialize the game and the player's name and 'gender'

    game = Game(name1, "Human", name2, "AI")
    return game


def computePoints(player):
    """
    Computes how much points is getting at the end of a round
    :param player: player to whom we want to count points
    """

    player.points += player.hasWon + (player.isAlive and player.extraPoint)


def fillDeck(listOfCards):
    """
    Fills the deck and shuffles it
    :param listOfCards: list of all available cards (10 different cards)
    :return: return the shuffled deck
    """

    deck = []
    for i in listOfCards:
        for j in range(i.totalNumber):
            deck.append(i)

    random.shuffle(deck)

    return deck


class Game:

    def __init__(self, player1name, player1Gender, player2name, player2Gender):

        # Creation of the card's instances
        spy_card = Card("Spy", 0, 2)
        guard_card = Card("Guard", 1, 6)
        priest_card = Card("Priest", 2, 2)
        baron_card = Card("Baron", 3, 2)
        handmaid_card = Card("Handmaid", 4, 2)
        prince_card = Card("Prince", 5, 2)
        chancellor_card = Card("Chancellor", 6, 2)
        king_card = Card("King", 7, 1)
        countess_card = Card("Countess", 8, 1,)
        princess_card = Card("Princess", 9, 1)

        # List of cards we will put in the deck

        self.listOfCards = [spy_card,
                            guard_card,
                            priest_card,
                            baron_card,
                            handmaid_card,
                            prince_card,
                            chancellor_card,
                            king_card,
                            countess_card,
                            princess_card]

        # List of the card we will put on the side at the beginning of each round

        self.hiddenCard = None
        self.isolatedCards = []

        self.deck = []

        # Creation of the players
        self.player1 = Player(player1name, player1Gender, self.hiddenCard, self.isolatedCards, self.listOfCards)
        self.player2 = Player(player2name, player2Gender, self.hiddenCard, self.isolatedCards, self.listOfCards)

        # Assigns the opposite player
        self.player1.oppositePlayer(self.player2)
        self.player2.oppositePlayer(self.player1)

    def initRound(self):
        """
         Initializes a round by creating the deck, the isolated cards and players' properties.
        """

        if self.player1.points != 0 or self.player2.points != 0:

            for i in range(2):
                print('\n')

            print("\n*---------------- NEW ROUND ----------------*")

            print(f"\n\t\t\t***---Scores---***\n"
                  f"\t\t\t{self.player1.name} - {self.player1.points}\t{self.player2.name} - {self.player2.points}")
        else:
            print("\nYou will need 6 points to win, good luck !\n")
        self.deck = fillDeck(self.listOfCards)

        self.isolatedCards = self.player1.isolatedCards = self.player2.isolatedCards = []

        self.player1.hand = []
        self.player2.hand = []

        self.player1.playedCards = self.player2.playedCards = []

        self.player1.isAlive = self.player2.isAlive = True
        self.player1.deadpool = self.player2.deadpool = False
        self.player1.hasWon = self.player2.hasWon = False
        self.player1.extraPoint = self.player2.extraPoint = 0

        # fill Known cards.
        for i in range(3):
            card = self.deck.pop(0)
            self.isolatedCards.append(card)

        # remove hidden card from deck
        self.hiddenCard = self.deck.pop(0)

        self.player1.draw(self.deck)
        self.player2.draw(self.deck)

    def endRound(self):
        """
        Checks if the round has ended and give points to the winning player.
        :return: False or True
        """

        if not self.player1.isAlive:

            self.player2.hasWon = True
            computePoints(self.player2)
            print(f"{self.player2.name} wins the round ! He scores {1 + self.player2.extraPoint} point(s)\n")

            return False

        elif not self.player2.isAlive:

            self.player1.hasWon = True
            computePoints(self.player1)
            print(f"{self.player1.name} wins the round ! He scores {1 + self.player1.extraPoint} point(s)\n")

            return False

        else:
            return True
