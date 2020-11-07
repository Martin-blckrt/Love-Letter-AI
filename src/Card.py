
class Card:
    def __init__(self, title, value, totalNumber, description):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        # self.assets = assets 


    def reveal(self):
        print(self.title)


class Spy(Card):
    def power(self):
        target.extraPoint += 1


class Guard(Card):
    def power(self, target):
        if target[1].gender == "Human":
            cardGuessed = target[1].guess()  # target[1] is the player currently playing, not the actual target
        else:
            cardGuessed = target[1].decide()  # target[1] is the player currently playing, not the actual target
        if cardGuessed == target[0].hand[0]:
            target[0].isAlive = False


class Priest(Card):
    def power(self, target):
        target.hand[0].reveal()


class Baron(Card):
    def power(self, player1, player2):
        if player1.compare(player2) == 0:
            player1.isAlive = False
        elif player1.compare(player2) == 1:
            player2.isAlive = False


class Handmaid(Card):
    def power(self, target):
        target.deadpool = True

class Prince(Card):
    def power(self, target):
        target.discard()
        target.draw()


class Chancellor(Card):
    def power(self, target, deck):
        target.draw(deck)
        target.draw(deck)
        target.draw(deck)


class King(Card):
    def power(self, *target):
        temp = target[0].hand[0]
        target[0].hand[0] = target[1].hand[1]
        target[1].hand[1] = temp


class Countess(Card):
    # pas de pouvoir, donc pas de pwer function mais faut checker à chaque tirage si la carte
    # tirée est la comtesse ou pas
    pass


class Princess(Card):
    pass
