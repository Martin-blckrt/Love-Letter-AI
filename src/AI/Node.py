class State:
    def __init__(self, deck, isolatedCards, player1, player2):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.player1 = player1
        self.player2 = player2


class Node:
    def __init__(self, state, value, parent):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self, childNode):

        self.children.append(childNode)
