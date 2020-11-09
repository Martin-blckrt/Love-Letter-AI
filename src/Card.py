
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

#TODO. Chancellor doit remettre 2 card dans deck (actuellement il garde tt ce qu'il a pioché dans sa main,
#TODO. Guard doit tuer,     A TESTER (mais marche normalement)
#TODO. Princesse doit tuer aussi (mais pas le même)     A TESTER
#TODO. Vérifier comtesse avec roi/prince        A TESTER
#TODO. Chancellor cas particulier ou plus assez de carte dans deck, same for prince avec defausse (pcq pioche double)
#TODO. Handmaid gérer l'immunité        A TESTER


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
