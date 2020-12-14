class State:
    def __init__(self, deck, isolatedCards, listOfCards, player):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.listOfCards = listOfCards
        self.player = player
        self.opponent = player.opponent


class Node:
    def __init__(self, state, value, parent, floor):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []
        self.floor = floor

    def addChild(self, childNode):

        self.children.append(childNode)
