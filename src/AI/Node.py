class State:
    def __init__(self, deck, isolatedCards, listofCards, player):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.listofCards = listofCards
        self.player = player
        self.opponent = player.opponent


class Node:
    def __init__(self, state, value, parent):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self, childNode):

        self.children.append(childNode)
