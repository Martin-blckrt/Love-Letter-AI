from src.cardPower import *

# TODO. if player rajouter leftNUmber-1 dans discard and play
# TODO. if AI rajouter leftNumber-1 dans draw / gerer chancellier


class Card:
    def __init__(self, title, value, totalNumber, description):
        self.title = title  # Title of the card
        self.value = value  # Value of the card
        self.totalNumber = totalNumber  # Keeps in mind how much copies of a card there are
        self.leftNumber = totalNumber  # Keeps in mind how much copies of a card are left in the game
        self.description = description  # Description of the card's effect
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
                print("The guess was correct !\n" if caption else None)
            else:
                print("Incorrect guess!" if caption else None)

        # ------------------------------ Priest --------------------------

        elif self.value == 2:

            activePlayer.opponent.hand[0].reveal()

        # ------------------------------ Baron ---------------------------
        elif self.value == 3:

            opponent = activePlayer.opponent

            i = activePlayer.compare(opponent)
            if i == 0:
                print(f"{activePlayer.name} loses the duel !" if caption else None)
                activePlayer.isAlive = False

            elif i == 1:
                print(f"\n{opponent.name} loses the duel !"if caption else None)
                opponent.isAlive = False

            else:
                print("It is a tie\n"if caption else None)

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

        else:

            print("une carte mystique ou countess ou princess")
