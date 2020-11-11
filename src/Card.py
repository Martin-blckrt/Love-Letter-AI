class Card:
    def __init__(self, title, value, totalNumber, description):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        # self.assets = assets 

    def reveal(self):
        print(f"Opponent's card is {self.title}\n")


# TODO. Chancellor : rendre plus joli ma zeub
# TODO. Chancellor : Debug
# TODO. Tester les cas de deck vide (notamment avec Chancellor et Prince) et les debug en cas de soucis


class Spy(Card):
    def power(self, activePLayer, deck_arg):
        activePLayer.extraPoint = 1


class Guard(Card):
    def power(self, activePlayer, deck_arg):

        if activePlayer.gender == "Human":
            cardGuessed = activePlayer.guess()
        else:
            cardGuessed = activePlayer.decide()

        if cardGuessed == activePlayer.opponent.hand[0].value:
            activePlayer.opponent.isAlive = False
            print("The guess was correct !\n")
        else:
            print("Incorrect guess!")


class Priest(Card):
    def power(self, activePlayer, deck_arg):
        activePlayer.opponent.hand[0].reveal()


class Baron(Card):
    def power(self, activePlayer, deck_arg):

        opponent = activePlayer.opponent

        if activePlayer.compare(opponent) == 0:
            print(f"{activePlayer.name} loses the duel !")
            activePlayer.isAlive = False
        elif activePlayer.compare(opponent) == 1:
            print(f"\n{opponent.name} loses the duel !")
            opponent.isAlive = False
        else:
            print("It is a tie\n")


class Handmaid(Card):
    def power(self, activePlayer, deck_arg):
        activePlayer.deadpool = True


class Prince(Card):
    def power(self, activePlayer, deck_arg):
        choice = input("\nWho do you want to target ? [You/Opponent]\n")
        choice.lower()
        while (choice != "you") and (choice != "opponent"):
            choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n")
            choice.lower()

        if choice == "you":
            target = activePlayer
            target.discard()
            target.draw(deck_arg)
        else:
            target = activePlayer.opponent
            if not target.deadpool:
                target.discard()
                target.draw(deck_arg)
            else:
                print(f"{target.name} is protected : your card has no effect !\n")


class Chancellor(Card):
    def power(self, activePlayer, deck_arg):

        j = 0
        for i in range(2):
            activePlayer.draw(deck_arg)
            j += 1

        if j == 1:
            print(
                f"You now need to get rid of 1 of your cards by placing it at the bottom of the deck. Your hand is :\n")
            for i in range(len(activePlayer.hand)):
                print(f"{i + 1}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")
            index = int(input("Which card do you want to place as the last card in the deck ? (1/2)\n"))
            while index not in [1, 2]:  # TODO. boucle infinie ?
                index = int(
                    input("\nWrong input ! Which card do you want to place as the last card in the deck ? (1/2)\n"))

            placedCard = activePlayer.hand.pop(index - 1)
            deck_arg.append(placedCard)

        elif j == 2:
            print(
                f"You now need to get rid of 2 of your cards by placing them at the bottom of the deck. Your hand is :\n")
            for i in range(len(activePlayer.hand)):
                print(f"{i + 1}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

            index = int(input("Which card do you want to place as the penultimate card in the deck ? (1/2/3)\n"))
            while index not in [1, 2, 3]:  # TODO. boucle infinie ?
                index = int(input(
                    "\nWrong input ! Which card do you want to place as the penultimate card in the deck ? (1/2/3)\n"))

            placedCard = activePlayer.hand.pop(index - 1)
            deck_arg.append(placedCard)

            index = int(input("Which card do you want to place as the last card in the deck ? (1/2)\n"))
            while index not in [1, 2]:  # TODO. boucle infinie ?
                index = int(
                    input("\nWrong input ! Which card do you want to place as the last card in the deck ? (1/2)\n"))

            placedCard = activePlayer.hand.pop(index - 1)
            deck_arg.append(placedCard)


class King(Card):
    def power(self, activePlayer, deck_arg):
        opponent = activePlayer.opponent

        print("The hands have been switched !\n")
        temp = activePlayer.hand[0]
        activePlayer.hand[0] = opponent.hand[0]
        opponent.hand[0] = temp


class Countess(Card):
    def power(self, activePlayer, deck_arg):
        pass


class Princess(Card):
    def power(self, activePlayer, deck_arg):
        pass
