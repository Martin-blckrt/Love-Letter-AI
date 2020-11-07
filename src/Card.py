from abc import ABC


class Card(ABC):
    def __init__(self, title, value, totalNumber, description):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        # self.assets = assets 

    # abstract method
    def power(self, *target):  # *targetAndGuess is used to give a variable number of parameters to
        #  the function, when called, the function will receive a tuple of arguments
        pass

    def reveal(self):
        print(self.title)


class Spy(Card):
    def power(self, target):
        target[0].extraPoint += 1


class Guard(Card):
    def power(self, *target):
        if target[1].gender == "Human":
            cardGuessed = target[1].guess()  # target[1] is the player currently playing, not the actual target
        else:
            cardGuessed = target[1].decide()  # target[1] is the player currently playing, not the actual target
        if cardGuessed == target[0].hand[0]:
            target[0].isAlive = False


class Priest(Card):
    def power(self, target):
        target[0].hand[0].reveal()


class Baron(Card):
    def power(self, *target):
        if target[0].compare(target[1]) == 0:
            target[0].isAlive = False
        elif target[0].compare(target[1]) == 1:
            target[1].isAlive = False


class Handmaid(Card):
    def power(self, target):
        target.deadpool = True
        # TODO. Deadpool ne doit durer qu'un seul tour


class Prince(Card):
    def power(self, target):
        target[0].discard()
        target[0].draw()


class Chancellor(Card):
    def power(self, target, deck):
        target[0].draw(deck)
        target[0].draw(deck)
        target[0].draw(deck)


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
