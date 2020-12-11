from src.AI.card_weight import weights
import copy


def evaluate(node):
    knownCards = node.state.player.isolatedCards + node.state.player.hand + \
                 node.state.player.playedCards

    impact = weights(node.state.player, knownCards, False)

    return impact


def getChildren(node):
    return node.children


def getAncestor(node, value):
    # returns the before-last ancestor of the child with the given value

    if getNodeValue(node) == value:
        target = node

    elif node.children:
        for child in node.children:
            target = getAncestor(child, value)
    else:
        print("WRONG")

    return target


def getAncestorCardIndex(node, value):
    # returns the index of the card that we should play next

    origin = node

    target = getAncestor(node, value)

    while target.parent.parent:
        node = node.parent

    hand = node.state.player.hand
    originHand = origin.state.player.hand

    for index in range(len(hand)):
        if not hand[index] == originHand[index]:
            return index


def isTerminal(node):

    cond1 = not node.state.deck  # deck vide
    cond2 = (not node.state.player.isAlive) or node.state.opponent.hasWon
    cond3 = (not node.state.opponent.isAlive) or node.state.player.hasWon

    return cond1 or cond2 or cond3


def getNodeValue(node):
    # Utile si besoin de debugger.

    return node.value


def findCard(cardvalue, list):

    index = 0
    for i in range(len(list)):
        if cardvalue == list[i].value:
            index = i
    return index


def nextStates(virtualNode):
    # TODO. Gerer qui joue est le player dans le noeud
    print("NEXT STATE ENTERED")

    next_nodes = []
    index = 0

    knownCards = virtualNode.state.player.isolatedCards + virtualNode.state.player.hand + \
        virtualNode.state.player.playedCards

    for card in virtualNode.state.listOfCards:

        if card.totalNumber - knownCards.count(card) > 0:
            copiedDeck = copy.deepcopy(virtualNode.state.deck)
            copiedHand = copy.deepcopy(virtualNode.state.player.hand)

            index = findCard(card.value, copiedDeck)
            del copiedDeck[index]

            index = findCard(card.value, copiedHand)
            del copiedHand[index]

            for i in range(2):
                newVirtualNode = copy.deepcopy(virtualNode)
                # on cree une copie du noeud pour genere des enfants de celui ci

                index = findCard(card.value, newVirtualNode.state.deck)
                del newVirtualNode.state.deck[index]
                newVirtualNode.state.player.hand.append(card)

                newVirtualNode.state.player.playTurn(newVirtualNode.state.player.hand, i, caption=False)

                newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

                if newVirtualNode.state.player.playedCards[0].value == 5:

                    for drawnCard in virtualNode.state.listOfCards:

                        if drawnCard.totalNumber - knownCards.count(drawnCard) > 0:

                            index = findCard(drawnCard.value, newVirtualNode.state.deck)
                            del newVirtualNode.state.deck[index]

                            if not newVirtualNode.state.player.hand:
                                newVirtualNode.state.player.hand.append(drawnCard)

                            elif not newVirtualNode.state.opponent.hand:
                                newVirtualNode.state.opponent.hand.append(drawnCard)

                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.
    return next_nodes
