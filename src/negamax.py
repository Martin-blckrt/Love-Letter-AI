def spy(node, knownCards):
    if node.state.player1.extrapoint:
        impact = 0
    else:
        impact = 0.5

    return impact

def guard(node, knownCards):

def priest(node, knownCards):
    impact = 0.15
    return impact

def baron(node, knownCards):
    a = 21 - len(knownCards)
    j = 0
    b = node.state.player1.hand[1]

    baron_index = node.state.player1.hand.index(node.state.baron_card)
    bool(baron_index)
    if baron_index:
        b = node.state.player1.hand[0]


    for i in range(a):
        if b > #cartes inconnues
            j+=1


    impact = 1 - (j/a)

    return impact

def handmaid(node, knownCards):

    impact = 0.2
    return impact

def prince(node, knownCards):

    impact = 0.15 + node.state.princess_card.left_Number/(21 - len(knownCards))
    return impact

def chancellor(node, knownCards):

    impact = 0.25
    return impact

def king(node, knownCards):

    a = 1/(21 - len(knownCards))
    impact = 150*a
    return impact

def countess(node, knownCards):

    a = 1/(21 - len(knownCards))
    b = node.state.player1.hand[1]
    impact = 175*a

    countess_index = node.state.player1.hand.index(node.state.countess_card)
    bool(countess_index)
    if countess_index:
        b = node.state.player1.hand[0]

    if node.state.b.value == [5, 7]:
        impact = 0

    return impact

def princess(node, knownCards):

    a = 1/(21 - len(knownCards))
    impact = 200*a
    return impact


def evaluate(node):

    knownCards = node.state.isolatedCards + node.state.player1.hand[0] + node.state.player1.hand[1] + node.state.player1.playedCards + node.state.player2.playedCards
    #TODO. histoire de je connais la fin du deck si chancellier

    return card1_impact + card2_impact

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

    def negamax(self, node, depth, alpha, beta, color):

        if isTerminal(node):
            return color * evaluate(node)

        # generate children
        # generate moves

        value = float('-inf')

        for child in node.children:

            value = max(value, -self.negamax(child, depth-1, -beta, -alpha, color))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value
