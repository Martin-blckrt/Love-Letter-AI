def evaluate(node):
    knownCards = node.state.isolatedCards + node.state.player1.hand[0] + \
                 node.state.player1.hand[1] + node.state.player1.playedCards + node.state.player2.playedCards
    # TODO. histoire de je connais la fin du deck si chancellier
    # return card1_impact + card2_impact
    pass


def getChildren(node):
    return node.children


def isTerminal(node):
    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return len(node.children) == 0


def getNodeValue(node):
    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return node.value
