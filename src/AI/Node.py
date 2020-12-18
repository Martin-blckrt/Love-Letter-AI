class State:
    def __init__(self, deck, isolatedCards, listOfCards, player):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.listOfCards = listOfCards
        self.player = player


class Node:
    def __init__(self, state, value, parent, floor):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []
        self.floor = floor

    def getParent(self, negaValue):
        if self.value == negaValue:
            self.parent.getParent(negaValue)
