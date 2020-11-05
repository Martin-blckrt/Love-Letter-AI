from src.Player import Player
from src.Card import *
import random

class Game:
    def __init__(self):
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

    def initRound(self, deck, isolatedCard, player1, player2):
        random.shuffle(deck)
        for i in range (3):
            card = deck.pop(0)
            pack = [card, 0]    #0 is visible, 1 is invisible
            isolatedCard.append(pack)
        card = deck.pop(0)
        pack = [card, 1]  # 0 is visible, 1 is invisible
        isolatedCard.append(pack)

        player1.draw(deck)
        player2.draw(deck)

    def initGame(self):
        player1 = Player("Human")
        player2 = Player("IA")

    def computeEarnedPoints(self, player):
        player.points += player.hasWon + (player.isAlive and player.extraPoint)