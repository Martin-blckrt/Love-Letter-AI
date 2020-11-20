
def getChildren(node):

    return node.children


def isTerminal(node):

    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return len(node.children) == 0


def getNodeValue(node):

    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return node.value


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

    def negamax(self, node, alpha, beta, color):

        if isTerminal(node):
            return color * evaluate(node)

        # generate children
        # generate moves

        value = float('-inf')

        for child in node.children:

            value = max(value, -self.negamax(child, -beta, -alpha, color))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value
