
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

#TODO. Chancellor doit remettre 2 card dans deck (actuellement il garde tt ce qu'il a pioché dans sa main
#TODO. Chancellor cas particulier ou plus assez de carte dans deck, same for prince avec defausse (pcq pioche double)

#TODO. Gérer la double pioche lorsque defausse
#TODO. Servante affiche le msg "immunity" que si la carte en face l'aggresse
#TODO. Ecrire points a la fin du round
#TODO. gestion input prince
#TODO. Ecrire action king


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
        while (choice != "You") and (choice != "Opponent"):
            choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n")

        if choice == "You":
            target = activePlayer
        else:
            target = activePlayer.opponent

        target.discard()
        target.draw(deck_arg)


class Chancellor(Card):
    def power(self, activePlayer, deck_arg):

        for i in range(3):
            activePlayer.draw(deck_arg)


class King(Card):
    def power(self, activePlayer, deck_arg):

        opponent = activePlayer.opponent

        temp = activePlayer.hand[0]
        activePlayer.hand[0] = opponent.hand[0]
        opponent.hand[0] = temp


class Countess(Card):
    def power(self, activePlayer, deck_arg):
        pass


class Princess(Card):
    def power(self, activePlayer, deck_arg):
        pass
