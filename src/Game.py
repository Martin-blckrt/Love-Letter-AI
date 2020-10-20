from src.Player import Player
from src.Card import *

deck = []  # à remplir

# --------------- Player init. ---------------

player1 = Player("Human", 0, 0)
player2 = Player("IA", 0, 0)


# --------------- Card init ---------------

Spy_Card = Spy("Spy", 0, 2, "Gardez un pion Faveur si personne ne joue ou défausse une carte Espionne.")
Guard_Card = Guard("Guard", 1, 6, "Devinez la main d'un autre joueur.")
Priest_Card = Priest("Priest", 2, 2, "Regardez la main d'un autre jouer.")
Baron_Card = Baron("Baron", 3, 2, "Comparez votre main avec celle d'un autre joueur.")
Handmaid_Card = Handmaid("Handmaid", 4, 2, "Les autres cartes n'ont pas d'effet sur vous jusqu'au prochain tour.")
Prince_Card = Prince("Prince", 5, 2, "Défaussez votre main et piochez à nouveau.")
Chancellor_Card = Chancellor("Chancellor", 6, 2, "Piochez et remettez deux cartes sous le paquet.")
King_Card = King("King", 7, 1, "Échangez votre main contre celle d'un autre joueur.")
Countess_Card = Countess("Countess", 8, 1, "Vous devez impérativement la jouer si vous avez le Roi ou un Prince.")
Princess_Card = Princess("Princess", 9, 1, "Quittez la manche si vous devez la jouer.")
