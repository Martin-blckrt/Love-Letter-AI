from src.cardPower import king_power, chancellor_power, prince_power


class Card:

    def __init__(self, title, value, totalNumber):
        self.title = title  # Title of the card
        self.value = value  # Value of the card
        self.totalNumber = totalNumber  # Keeps in mind how much copies of a card there are

    def reveal(self, activePlayer, real):
        """
        Allow to reveal the card of a player.
        :param activePlayer:
        :param real: Check if the turn is real or not.
        """

        if activePlayer.gender == "Human":
            print(f"The opponent has a {self.title}\n" if real else "", end="")
        else:
            print(f"The AI knows your card.\n" if real else "", end="")

    def power(self, activePlayer, deck_arg, real=True):
        """
        :param activePlayer: Joueur qui va utiliser le pouvoir de la carte
        :param deck_arg: Envoie le deck
        :param real: Argument utilisé pour vérifier si le tour est virtuel ou non
        :return: Ne return rien.
        """

        # ------------------------------ Spy ------------------------------
        if self.value == 0:
            activePlayer.extraPoint = 1

        # ------------------------------ Guard ----------------------------
        elif self.value == 1:  # guard

            if activePlayer.gender == "Human" and real:
                cardGuessed = activePlayer.guess()
            else:
                cardGuessed = activePlayer.decide()

            if cardGuessed == activePlayer.opponent.hand[0].value:
                activePlayer.opponent.isAlive = False
                print("The guess was correct !\n" if real else "", end="")
            else:
                if activePlayer.gender == "Human":
                    print("Incorrect guess!\n" if real else "", end="")
                else:
                    print("The AI's guess was incorrect !\n" if real else "", end="")

        # ------------------------------ Priest --------------------------

        elif self.value == 2:

            activePlayer.opponent.hand[0].reveal(activePlayer, real)

        # ------------------------------ Baron ---------------------------
        elif self.value == 3:

            opponent = activePlayer.opponent

            i = activePlayer.compare(opponent, real)
            if i == 0:
                print(f"{activePlayer.name} loses the duel !\n" if real else "", end="")
                activePlayer.isAlive = False

            elif i == 1:
                print(f"\n{opponent.name} loses the duel !\n" if real else "", end="")
                opponent.isAlive = False

            else:
                print("It is a tie\n" if real else "", end="")

        # ------------------------------ Handmaid ------------------------
        elif self.value == 4:

            activePlayer.deadpool = True

        # ------------------------------ Prince --------------------------
        elif self.value == 5:

            prince_power(activePlayer, deck_arg, real)

        # ------------------------------ Chancellor ---------------------

        elif self.value == 6:

            chancellor_power(activePlayer, deck_arg, real)

        # ------------------------------ King ------------------------------
        elif self.value == 7:

            king_power(activePlayer, real)

        # Coumtess and Princess, not necessary because no active effect
