import copy
from src.AI.card_weight import weights


def evaluate(node):
    knownCards = node.state.player.isolatedCards + node.state.player.hand + node.state.player.playedCards
    m = 0
    impact = 0.75

    if isTerminal(node):

        if node.state.player.isAlive:
            if node.state.player.extraPoint:
                impact = 1

        elif node.state.opponent.isAlive:
            impact = 0

        elif not node.state.deck:

            for Card in node.state.player.listOfCards:

                if node.state.player.hand[0].value > Card.value:

                    n = findOccurences(Card, knownCards)
                    m += Card.totalNumber - n

            impact = m / (1-len(knownCards))

            if node.state.player.extraPoint:
                impact += 0.5
    else:
        impact = weights(node.state.player, knownCards, False)

    return impact


def getAncestor(node, value):
    # returns the before-last ancestor of the child with the given value
    # TODO. Trouver soluce pour valeur non trouvée
    """
        Option possible : param depth qu'on utiliserais pour limiter la recherche
        :param node: Noeud d'où la recherche part
        :param value: valeur à trouver dans le noeud
        :return: retourne le noeud (enfant de node) vers lequel il faut se diriger
    """

    if getNodeValue(node) == value:
        target = node

    elif node.children:
        for child in node.children:
            target = getAncestor(child, value)
    else:
        print("Value not found")

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


def findOccurences(card, searchedList):

    i = 0
    for aCard in searchedList:
        if card.value == aCard.value:
            i += 1
    print(i)
    return i


def nextStates(virtualNode, color):

    if color == 1:
        activePlayer = virtualNode.state.player
    else:
        activePlayer = virtualNode.state.opponent

    print(f"\n{activePlayer.name} and node value is {virtualNode.value}\n")

    next_nodes = []

    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    if len(virtualNode.state.deck) >= 12 and color == 1:

        for i in range(2):
            newVirtualNode = copy.deepcopy(virtualNode)
            # on cree une copie du noeud pour genere des enfants de celui ci
            newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud
            activePlayer = newVirtualNode.state.player

            activePlayer.playTurn(newVirtualNode.state.deck, i, caption=False)

            if not activePlayer.hand:

                for drawnCard in virtualNode.state.listOfCards:

                    if drawnCard.totalNumber - knownCards.count(drawnCard) > 0:
                        princedNode = copy.deepcopy(newVirtualNode)
                        princedNode.parent = virtualNode

                        index = findCard(drawnCard.value, newVirtualNode.state.deck)
                        activePlayer.hand.append(newVirtualNode.state.deck[index])
                        del newVirtualNode.state.deck[index]
                        knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

                        next_nodes.append(princedNode)

            elif not activePlayer.opponent.hand:

                drawnCard = newVirtualNode.state.deck.pop(0)
                activePlayer.opponent.hand.append(drawnCard)
                next_nodes.append(newVirtualNode)

            else:
                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.
    else:
        for card in virtualNode.state.listOfCards:

            n = findOccurences(card, knownCards)

            if card.totalNumber - n > 0:

                for i in range(2):

                    newVirtualNode = copy.deepcopy(virtualNode)
                    # on cree une copie du noeud pour genere des enfants de celui ci
                    newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

                    if color == 1:
                        activePlayer = newVirtualNode.state.player
                    else:
                        activePlayer = newVirtualNode.state.opponent

                    index = findCard(card.value, newVirtualNode.state.deck)
                    activePlayer.hand.append(newVirtualNode.state.deck[index])
                    del newVirtualNode.state.deck[index]
                    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

                    activePlayer.playTurn(newVirtualNode.state.deck, i, caption=False)

                    if not activePlayer.hand:

                        for drawnCard in virtualNode.state.listOfCards:

                            n = findOccurences(card, knownCards)

                            if drawnCard.totalNumber - n > 0:

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
