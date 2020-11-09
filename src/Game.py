from src.Player import Player
from src.Card import *
import random


def initGame(name1, name2):
    game = Game(name1, "Human", name2, "AI")
    return game


def computePoints(player):
    player.points += player.hasWon + (player.isAlive and player.extraPoint)


class Game:
    def __init__(self, player1name, player1Gender, player2name, player2Gender):

        self.player1 = Player(player1name, player1Gender)
        self.player2 = Player(player2name, player2Gender)

        self.player1.oppositePlayer(self.player2)
        self.player2.oppositePlayer(self.player1)

        Spy_Card = Spy("Spy", 0, 2, "Gardez un pion Faveur si personne ne joue ou défausse une carte Espionne.")
        Guard_Card = Guard("Guard", 1, 6, "Devinez la main d'un autre joueur.")
        Priest_Card = Priest("Priest", 2, 2, "Regardez la main d'un autre jouer.")
        Baron_Card = Baron("Baron", 3, 2, "Comparez votre main avec celle d'un autre joueur.")
        Handmaid_Card = Handmaid("Handmaid", 4, 2,
                                 "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour.")
        Prince_Card = Prince("Prince", 5, 2, "Défaussez votre main et piochez à nouveau.")
        Chancellor_Card = Chancellor("Chancellor", 6, 2, "Piochez et remettez deux cartes sous le paquet.")
        King_Card = King("King", 7, 1, "Échangez votre main contre celle d'un autre joueur.")
        Countess_Card = Countess("Countess", 8, 1,
                                 "Vous devez impérativement la jouer si vous avez le Roi ou un Prince.")
        Princess_Card = Princess("Princess", 9, 1, "Quittez la manche si vous devez la jouer.")

        self.deck = [Spy_Card, Spy_Card,
                     Guard_Card, Guard_Card, Guard_Card, Guard_Card, Guard_Card, Guard_Card,
                     Priest_Card, Priest_Card,
                     Baron_Card, Baron_Card,
                     Handmaid_Card, Handmaid_Card,
                     Prince_Card, Prince_Card,
                     Chancellor_Card, Chancellor_Card,
                     King_Card,
                     Countess_Card,
                     Princess_Card]

        self.isolatedCard = []

    def initRound(self):
        random.shuffle(self.deck)

        print("Known isolated cards are : ")
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

        if not self.player1.isAlive:
            self.player2.points += 1 + self.player2.extraPoint
            return False
        elif not self.player2.isAlive:
            self.player1.points += 1 + self.player1.extraPoint
            return False
        else:
            return True
