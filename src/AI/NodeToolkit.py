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
    # TODO. deck empty check
    return len(node.children) == 0


def getNodeValue(node):
    # TODO: si on a des erreurs, réfléchir au cas où state == None
    return node.value


def nextStates(virtualNode, listOfCards, isolatedCard):

    # TODO. Gerer qui joue est le player dans le noeud

    next_nodes = []
    for usedCard in virtualNode.state.player.hand:

        # usedCard is the card virtually played by the player
        usedCardIndex = virtualNode.state.player.hand.index(usedCard)
        virtualNode.state.player.playTurn(virtualNode.state.deck, caption=False)
        virtualNode.state.player.hand.remove(usedCard)

        for card in listOfCards:

            if card.leftNumber > 0:

                newVirtualNode = virtualNode  # on cree une copie du noeud pour genere des enfants de celui ci

                # piocher
                newVirtualNode.state.deck.remove(newVirtualNode.state.card)
                card.leftNumber -= 1
                newVirtualNode.state.player.hand.append(card)
                newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud
                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.

    return next_nodes




