from src.AI.card_weight import weights
import copy


def evaluate(node):
    knownCards = node.state.player.isolatedCards + node.state.player.hand + \
                 node.state.player.playedCards + node.state.opponent.playedCards
    # TODO. histoire de je connais la fin du deck si chancellier

    impact = weights(node.state.player, knownCards, False)

    return impact


def getChildren(node):
    return node.children


def getAncestor(node, value):
    # returns the before-last ancestor of the child with the given value
    target = None

    if getNodeValue(node) == value:
        target = node

    elif node.children:
        for child in node.children:
            target = getAncestor(child, value)

    return target


def getAncestorCardIndex(node, value):
    # returns the index of the card that we should play next

    origin = node

    target = getAncestor(node, value)

    while target.parent.parent:
        node = node.parent

    hand = node.state.player.hand
    originHand = origin.state.player.hand

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


def nextStates(virtualNode):
    # TODO. Gerer qui joue est le player dans le noeud

    next_nodes = []
    knownCards = virtualNode.state.player.isolatedCards + virtualNode.state.player.hand + \
                 virtualNode.state.player.playedCards + virtualNode.state.opponent.playedCards

    for card in virtualNode.state.listOfCards:

        if card.totalNumber - knownCards.count(card) > 0:
            copiedDeck = copy.deepcopy(virtualNode.state.deck)
            copiedHand = copy.deepcopy(virtualNode.state.player.hand)
            copiedDeck.remove(card)
            copiedHand.append(card)

            for i in range(2):
                newVirtualNode = copy.deepcopy(virtualNode)
                # on cree une copie du noeud pour genere des enfants de celui ci
                newVirtualNode.state.deck.remove(card)
                newVirtualNode.state.player.hand.append(card)
                newVirtualNode.state.player.playTurn(copiedDeck, i, caption=False)
                newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

                if newVirtualNode.state.player.playedCards[0].value == 5:

                    for drawnCard in virtualNode.state.listOfCards:

                        if drawnCard.totalNumber - knownCards.count(drawnCard) > 0:

                            newVirtualNode.state.deck.remove(drawnCard)

                            if not newVirtualNode.state.player.hand:
                                newVirtualNode.state.player.hand.append(drawnCard)

                            elif not newVirtualNode.state.opponent.hand:
                                newVirtualNode.state.opponent.hand.append(drawnCard)

                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.
    return next_nodes
