
class State:
    def __init__(self, deck, isolatedCards, player1, player2):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.player1 = player1
        self.player2 = player2

class Node:
    def __init__(self, value=0, parent=None, state):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self, childNode):

        self.children.append(childNode)

    def getChildren(self, node):

        return node.children

    def isTerminal(self, node):

        if node is None:
            return
        else:
            return len(node.children) == 0

    def getNodeValue(self, node):

        assert node is not None
        return node.value

    def max_value(self, node):

        print("MiniMax–>MAX: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getNodeValue(node)

        max_value = float('-inf')

        successors_states = self.getChildren(node)

        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def min_value(self, node):

        print("MiniMax–>MIN: Visited Node :: " + node.Name)

        if self.isTerminal(node):
            return self.getNodeValue(node)

        min_value = float('inf')

        successor_states = self.getChildren(node)

        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value
