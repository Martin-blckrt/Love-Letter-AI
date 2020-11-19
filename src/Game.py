from src.Player import Player
from src.Card import *
import random


def initGame(name1, name2):
    # Initialize the game and the player's name and 'gender'

    game = Game(name1, "Human", name2, "Human")
    return game


def computePoints(player):
    # Computes how much points is getting at the end of a round

    player.points += player.hasWon + (player.isAlive and player.extraPoint)


def fillDeck(listOfCards):
    # Fills the deck and shuffles it

    deck = []
    for i in listOfCards:
        for j in range(i.totalNumber):
            deck.append(i)
    #random.shuffle(deck)

    return deck


class Game:
    def __init__(self, player1name, player1Gender, player2name, player2Gender):

        # Creation of the players
        self.player1 = Player(player1name, player1Gender)
        self.player2 = Player(player2name, player2Gender)

        # Assigns the opposite player
        self.player1.oppositePlayer(self.player2)
        self.player2.oppositePlayer(self.player1)

        # Creation of the card's instances

        spy_card = Spy("Spy", 0, 2, "Gardez un pion Faveur si personne ne joue ou défausse une carte Espionne.")
        guard_card = Guard("Guard", 1, 6, "Devinez la main d'un autre joueur.")
        priest_card = Priest("Priest", 2, 2, "Regardez la main d'un autre jouer.")
        baron_card = Baron("Baron", 3, 2, "Comparez votre main avec celle d'un autre joueur.")
        handmaid_card = Handmaid("Handmaid", 4, 2,
                                 "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour.")
        prince_card = Prince("Prince", 5, 2, "Défaussez votre main et piochez à nouveau.")
        chancellor_card = Chancellor("Chancellor", 6, 2, "Piochez et remettez deux cartes sous le paquet.")
        king_card = King("King", 7, 1, "Échangez votre main contre celle d'un autre joueur.")
        countess_card = Countess("Countess", 8, 1,
                                 "Vous devez impérativement la jouer si vous avez le Roi ou un Prince.")
        princess_card = Princess("Princess", 9, 1, "Quittez la manche si vous devez la jouer.")

        # List of cards we will put in the deck
        self.listOfCards = [spy_card,
                            guard_card,
                            priest_card,
                            baron_card,
                            handmaid_card,
                            prince_card,
                            #chancellor_card,
                            king_card,
                            countess_card,
                            #princess_card,
                            chancellor_card]

        # List of the card we will put on the side at the beginning of each round
        self.isolatedCard = []

        self.deck = []

    def initRound(self):
        # Initializes a round

        print("\n----------NEW ROUND----------")
        self.deck = fillDeck(self.listOfCards)

        self.player1.hand = []
        self.player2.hand = []
        self.player1.playedCards = self.player2.playedCards = []

        self.player1.isAlive = self.player2.isAlive = True
        self.player1.deadpool = self.player2.deadpool = False
        self.player1.hasWon = self.player2.hasWon = False
        self.player1.extraPoint = self.player2.extraPoint = 0

        print(f"\nCurrent scores are :"
              f"\n{self.player1.name} : {self.player1.points}\n{self.player2.name} : {self.player2.points}")

        print("\n\nKnown isolated cards are : ")
        for i in range(3):
            card = self.deck.pop(0)
            pack = [card, 0]  # 0 is visible, 1 is invisible
            self.isolatedCard.append(pack)
            print(f" {card.title} [{card.value}]", end=" ")

        card = self.deck.pop(0)
        pack = [card, 1]  # 0 is visible, 1 is invisible
        self.isolatedCard.append(pack)

        self.player1.draw(self.deck)
        self.player2.draw(self.deck)

    def endRound(self):
        # Checks if the round has ended and give points to the winning player
        if not self.player1.isAlive:
            self.player2.points += 1 + self.player2.extraPoint
            print(f"{self.player2.name} wins the round ! He scores {1 + self.player2.extraPoint} point(s)\n")
            return False
        elif not self.player2.isAlive:
            self.player1.points += 1 + self.player1.extraPoint
            print(f"{self.player1.name} wins the round ! He scores {1 + self.player1.extraPoint} point(s)\n")
            return False
        else:
            return True
