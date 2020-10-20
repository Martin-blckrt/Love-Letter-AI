from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, title, value, totalNumber, description):
        self.title = title
        self.value = value
        self.totalNumber = totalNumber
        self.leftNumber = totalNumber
        self.description = description
        # self.assets = assets 

    # abstract method
    def power(self, *targetAndGuess):  # *targetAndGuess is used to give a variable number of parameters to
        #  the function, when called, the function will receive a tuple of arguments
        pass


class Spy(Card):
    def power(self, target):
        target[0].extraPoint += 1


class Guard(Card):
    # TODO. Write guess() & decide() functions

    pass


class Priest(Card):

    pass


class Baron(Card):
    pass


class Handmaid(Card):
    pass


class Prince(Card):
    pass


class Chancellor(Card):
    pass


class King(Card):
    pass


class Countess(Card):
     # pas de pouvoir, donc pas de pwer function mais faut checker à chaque tirage si la carte
     # tirée est la comtesse ou pas

class Princess(Card):
    def power(self, target):
        target.isAlive = 0

