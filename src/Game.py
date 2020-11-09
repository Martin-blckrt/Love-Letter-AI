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

        self.Spy_Card = Spy("Spy", 0, 2, "Gardez un pion Faveur si personne ne joue ou défausse une carte Espionne.")
        self.Guard_Card = Guard("Guard", 1, 6, "Devinez la main d'un autre joueur.")
        self.Priest_Card = Priest("Priest", 2, 2, "Regardez la main d'un autre jouer.")
        self.Baron_Card = Baron("Baron", 3, 2, "Comparez votre main avec celle d'un autre joueur.")
        self.Handmaid_Card = Handmaid("Handmaid", 4, 2,
                                 "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour.")
        self.Prince_Card = Prince("Prince", 5, 2, "Défaussez votre main et piochez à nouveau.")
        self.Chancellor_Card = Chancellor("Chancellor", 6, 2, "Piochez et remettez deux cartes sous le paquet.")
        self.King_Card = King("King", 7, 1, "Échangez votre main contre celle d'un autre joueur.")
        self.Countess_Card = Countess("Countess", 8, 1,
                                 "Vous devez impérativement la jouer si vous avez le Roi ou un Prince.")
        self.Princess_Card = Princess("Princess", 9, 1, "Quittez la manche si vous devez la jouer.")



        self.isolatedCard = []

    def initRound(self):

        self.deck = [self.Spy_Card, self.Spy_Card,
                     self.Guard_Card, self.Guard_Card, self.Guard_Card, self.Guard_Card, self.Guard_Card, self.Guard_Card,
                     self.Priest_Card, self.Priest_Card,
                     self.Baron_Card, self.Baron_Card,
                     self.Handmaid_Card, self.Handmaid_Card,
                     self.Prince_Card, self.Prince_Card,
                     self.Chancellor_Card, self.Chancellor_Card,
                     self.King_Card,
                     self.Countess_Card,
                     self.Princess_Card]

        random.shuffle(self.deck)

        self.player1.extraPoint = 0
        self.player2.extraPoint = 0

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
