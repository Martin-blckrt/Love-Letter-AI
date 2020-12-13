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
    # TODO. Trouver soluce pour valeur non trouvée

    if getNodeValue(node) == value:
        target = node

    elif node.children:
        for child in node.children:
            target = getAncestor(child, value)
    else:
        target = node.children[0]
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


def findCard(cardvalue, selectedList):

    index = 0
    for i in range(len(selectedList)):
        if cardvalue == selectedList[i].value:
            index = i
    return index


def nextStates(virtualNode, activePlayer):

    print(f"Active player is : {activePlayer.name} and node value is {virtualNode.value}")

    next_nodes = []

    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    for card in virtualNode.state.listOfCards:

        if card.totalNumber - knownCards.count(card) > 0:
            print("je boucle tant que des cartes sont dispos")

            """
            copiedDeck = copy.deepcopy(virtualNode.state.deck)
            copiedHand = copy.deepcopy(virtualNode.state.player.hand)

            index = findCard(card.value, copiedDeck)
            copiedHand.append(copiedDeck[index])
            del copiedDeck[index]
            """
            for i in range(2):

                newVirtualNode = copy.deepcopy(virtualNode)
                # on cree une copie du noeud pour genere des enfants de celui ci
                newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

                cond = (len(virtualNode.state.deck) == 12) and virtualNode.state.player.playedCards[1].value == 5
                if (len(virtualNode.state.deck) == 13) or cond:
                    pass
                else:
                    index = findCard(card.value, newVirtualNode.state.deck)
                    newVirtualNode.state.player.hand.append(newVirtualNode.state.deck[index])
                    del newVirtualNode.state.deck[index]

                    print(f"nextStates hand : {newVirtualNode.state.player.hand}")

                    activePlayer.playTurn(newVirtualNode.state.player.hand, i, caption=False)

                if not activePlayer.hand:

                    for drawnCard in virtualNode.state.listOfCards:

                        if drawnCard.totalNumber - knownCards.count(drawnCard) > 0:

                            princedNode = copy.deepcopy(newVirtualNode)
                            princedNode.parent = virtualNode

                            index = findCard(drawnCard.value, newVirtualNode.state.deck)
                            activePlayer.hand.append(newVirtualNode.state.deck[index])
                            del newVirtualNode.state.deck[index]

                            next_nodes.append(princedNode)

                elif not activePlayer.opponent.hand:

                    drawnCard = newVirtualNode.state.deck.pop(0)
                    activePlayer.opponent.hand.append(drawnCard)
                    next_nodes.append(newVirtualNode)

                else:
                    next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.
    return next_nodes
