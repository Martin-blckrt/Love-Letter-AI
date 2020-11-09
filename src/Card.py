
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


class Spy(Card):
    def power(self, activePLayer, deck_arg):

        activePLayer.extraPoint += 1


class Guard(Card):
    def power(self, activePlayer, deck_arg):

        opponent = activePlayer.opponent

        if activePlayer.gender == "Human":
            cardGuessed = activePlayer.guess()
        else:
            cardGuessed = activePlayer.decide()

        if cardGuessed == opponent.hand[0].value:
            opponent.isAlive = False


class Priest(Card):
    def power(self, activePlayer, deck_arg):

        activePlayer.opponent.hand[0].reveal()


class Baron(Card):
    def power(self, activePlayer, deck_arg):

        opponent = activePlayer.opponent

        if activePlayer.compare(opponent) == 0:
            activePlayer.isAlive = False
        elif activePlayer.compare(opponent) == 1:
            opponent.isAlive = False


class Handmaid(Card):
    def power(self, activePlayer, deck_arg):

        activePlayer.deadpool = True


class Prince(Card):
    def power(self, activePlayer, deck_arg):

        choice = input("who do you want to target ? [You/Opponent]\n")

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
        print('BOOM Countess')

    pass


class Princess(Card):
    def power(self, activePlayer, deck_arg):
        print('BOOM Princess')
    pass
