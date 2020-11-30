def evaluate(node):
    knownCards = node.state.isolatedCards + node.state.player1.hand[0] + \
                 node.state.player1.hand[1] + node.state.player1.playedCards + node.state.player2.playedCards
    # TODO. histoire de je connais la fin du deck si chancellier
    # return card1_impact + card2_impact
    pass


def getChildren(node):
    return node.children


def getAncestor(node, value):
    # returns the before-last ancestor of the child with the given value

    if getNodeValue(node) == value:
        target = node

    elif node.children is not None:
        for child in node.children:
            target = getAncestor(child)

    return target


def getAncestorCardIndex(node, value):
    # returns the index of the card that we should play next

    origin = node

    target = getAncestor(node, value)

    while target.parent.parent is not None:
        node = node.parent

    hand = node.state.player2.hand
    originHand = origin.state.player2.hand

    for index in range(2):
        if not hand[index] == originHand[index]:
            result = index
            return result


def isTerminal(node):
    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return len(node.children) == 0


def getNodeValue(node):
    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return node.value
