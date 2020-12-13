# -----------------------------------------------
# Fichier de définition de la classe Card representant les cartes du jeu.
# Template de la classe Card et ses méthodes.
#   --> Reveal() : dévoile la carte du joueur adverse
#   --> power() : applique le pouvoir de la carte jouée.
# -----------------------------------------------

from src.cardPower import *


class Card:
    def __init__(self, title, value, totalNumber, description):
        self.title = title  # Title of the card
        self.value = value  # Value of the card
        self.totalNumber = totalNumber  # Keeps in mind how much copies of a card there are
        # self.description = description  # Description of the card's effect
        # self.assets = assets 

    def reveal(self):
        print(f"Opponent's card is {self.title}\n")

    def power(self, activePlayer, deck_arg, caption=True):

        # ------------------------------ Spy ------------------------------
        if self.value == 0:
            activePlayer.extraPoint = 1

        # ------------------------------ Guard ----------------------------
        elif self.value == 1:  # guard

            if activePlayer.gender == "Human":
                cardGuessed = activePlayer.guess()
            else:
                cardGuessed = activePlayer.decide()

            if cardGuessed == activePlayer.opponent.hand[0].value:
                activePlayer.opponent.isAlive = False
                print("The guess was correct !\n" if caption else "")
            else:
                print("Incorrect guess!" if caption else "")

        # ------------------------------ Priest --------------------------

        elif self.value == 2:

            activePlayer.opponent.hand[0].reveal()

        # ------------------------------ Baron ---------------------------
        elif self.value == 3:

            opponent = activePlayer.opponent

            i = activePlayer.compare(opponent, caption)
            if i == 0:
                print(f"{activePlayer.name} loses the duel !" if caption else "")
                activePlayer.isAlive = False

            elif i == 1:
                print(f"\n{opponent.name} loses the duel !"if caption else "")
                opponent.isAlive = False

            else:
                print("It is a tie\n"if caption else "")

        # ------------------------------ Handmaid ------------------------
        elif self.value == 4:

            activePlayer.deadpool = True

        # ------------------------------ Prince --------------------------
        elif self.value == 5:

            prince_power(activePlayer, deck_arg, caption)

        # ------------------------------ Chancellor ---------------------

        elif self.value == 6:

            chancellor_power(activePlayer, deck_arg, caption)

        # ------------------------------ King ------------------------------
        elif self.value == 7:

            king_power(activePlayer, caption)

        elif self.value == 8 :

            print("Countess has been played" if caption else "")

        elif self.value == 9:

            print("Princess has been played" if caption else "")
