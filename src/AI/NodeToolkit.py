import copy
from src.AI.card_weight import weights
from src.AI.Node import dfs, getPathFrom


def evaluate(node):
    """
    :param node: Send the node of the tree that needs to be evaluated.
    :return: Return the impact of the card
    """

    knownCards = node.state.player.isolatedCards + node.state.player.hand + node.state.player.playedCards
    m = 0
    impact = 0.75

    if isTerminal(node):

        if node.state.player.isAlive:

            if node.state.player.extraPoint:
                impact = 1

        elif node.state.player.opponent.isAlive:
            impact = 0

        elif not node.state.deck:

            for Card in node.state.player.listOfCards:

                if node.state.player.hand[0].value > Card.value:

                    n = findOccurences(Card, knownCards)
                    m += Card.totalNumber - n

            impact = m / (1 - len(knownCards))

            if node.state.player.extraPoint:
                impact += 0.5
    else:
        impact = weights(node.state.player, knownCards, False)

    # arrondi pour faciliter la lecture

    impact = round(impact, 5)
    return impact


def getAncestor(start, value):

    lineage = dfs(start, value)

    return lineage


def getAncestorCardIndex(node, value):
    """
    Allow to get the index of the card that the AI must play to follow the planned scenario
    :param node: Origin node
    :param value: value of the node that the AI is targeting.
    :return: Return the index of the card that will be played.
    """

    # copie du noeud de départ pour eviter des modifs non prévuees
    start = copy.deepcopy(node)

    # DFS
    dfsResult = getAncestor(start, value)

    path = getPathFrom(dfsResult)

    # 0 est le noeud start
    target = path[1]

    originHand = start.state.player.hand
    targetHand = target.state.player.hand

    i = 0

    firstCardCond = targetHand[0].title != originHand[0].title
    secondCardCond = targetHand[0].title != originHand[1].title

    if firstCardCond and secondCardCond:

        if target.state.player.playedCards[1] == 5:
            return findCard(5, originHand)
        elif target.state.player.playedCards[0] == 6:
            return findCard(6, originHand)
        elif target.state.player.playedCards[0] == 7:
            return findCard(7, originHand)
    else:
        for i in range(len(originHand)):
            if targetHand[0].title != originHand[i].title:
                return i

    # cas défaut
    return i


def isTerminal(node):
    """
    Function that check if the node is terminal or not
    :param node: The node that we want to consider.
    :return: Return True if the node is terminal.
    """

    cond1 = not node.state.deck  # deck vide
    cond2 = (not node.state.player.isAlive) or node.state.player.opponent.hasWon
    cond3 = (not node.state.player.opponent.isAlive) or node.state.player.hasWon

    return cond1 or cond2 or cond3


def getNodeValue(node):
    """
    Accessor of the node value. Needed to debug
    :return: value of the considered node.
    """
    return node.value


def findCard(cardvalue, selectedList):
    """
    Function that allows to get the index of a card in a list thx to its value.
    :param cardvalue: Value of the card
    :param selectedList: List in which we are looking for the card index.
    :return: Index of the card if found, else, return None.
    """

    index = -1

    for i in range(len(selectedList)):
        if cardvalue == selectedList[i].value:
            index = i

    return index


def findOccurences(card, searchedList):
    """
    Find if there is an occurence of the card in the list, if yes, return the index of the card
    :param card: Card that we're looking for in the list
    :param searchedList: List in which we are looking for if the card exists.
    :return: index of the card in searchedList
    """
    i = 0

    for aCard in searchedList:
        if card.value == aCard.value:
            i += 1

    return i


def generateChildren(virtualNode, next_nodes, color, knownCards, firstTurn, *simulatedCard):
    """
    Function that generate the tree by filling the next_nodes list.
    -> copy the virtualNode, define the activePlayer and make the activeplayer play a turn.
    Manage case of prince that is played in the tree generation.

    :param virtualNode: Copy of the parent node of newVirtualNode
    :param next_nodes: List of children of a node
    :param color: define the gender of the player in negamax
    :param knownCards: Known cards of the active player.
    :param firstTurn: Define if the turn is the first of the round or not.
    :param simulatedCard: optional argument used if not First Turn
    """

    for i in range(2):  # Pour chaque carte de la main

        # on cree une copie du noeud pour genere des enfants de celui ci
        newVirtualNode = copy.deepcopy(virtualNode)
        newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

        if firstTurn:
            # Cas du premier tour
            activePlayer = newVirtualNode.state.player
            index = -1

        else:

            # Si la couleur est à 1, le joueur est l'IA
            if color == 1:

                activePlayer = newVirtualNode.state.player

            else:

                activePlayer = newVirtualNode.state.player.opponent

            index = findCard(simulatedCard[0].value, newVirtualNode.state.deck)

            if index != -1:
                activePlayer.hand.append(newVirtualNode.state.deck[index])
                del newVirtualNode.state.deck[index]

            knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

        if index == -1 and not firstTurn:
            del newVirtualNode

        else:

            # On fait jouer activePlayer
            activePlayer.playTurn(newVirtualNode.state.deck, i, real=False)

            if not activePlayer.hand:

                # cas ou le prince a été joué
                for drawnCard in virtualNode.state.listOfCards:

                    n = findOccurences(drawnCard, knownCards)

                    if drawnCard.totalNumber - n > 0:

                        princedNode = copy.deepcopy(newVirtualNode)
                        princedNode.parent = virtualNode

                        if color == 1:
                            activePlayer = princedNode.state.player

                        else:

                            activePlayer = princedNode.state.player.opponent

                        index = findCard(drawnCard.value, princedNode.state.deck)

                        if index == -1 and not firstTurn:
                            del princedNode
                        else:
                            activePlayer.hand.append(princedNode.state.deck[index])
                            del princedNode.state.deck[index]

                            next_nodes.append(princedNode)

            elif not activePlayer.opponent.hand:

                drawnCard = newVirtualNode.state.deck.pop(0)
                activePlayer.opponent.hand.append(drawnCard)

                next_nodes.append(newVirtualNode)

            else:
                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.


def nextStates(virtualNode, color):
    """
    call the generateChildren function that create the game tree.
    :param virtualNode: copy of the origin node
    :param color: define the gender of activePlayer from negamax.
    :return: list of next_nodes
    """

    if color == 1:
        activePlayer = virtualNode.state.player
    else:
        activePlayer = virtualNode.state.player.opponent

    # On déclare la liste de noeuds (les futurs enfant du noeud origin "node"
    next_nodes = []

    # On calcule les cartes connu par l'activePlayer
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    if len(activePlayer.hand) == 2:

        generateChildren(virtualNode, next_nodes, color, knownCards, True)

    else:

        for simulatedCard in virtualNode.state.listOfCards:
            n = findOccurences(simulatedCard, knownCards)

            if simulatedCard.totalNumber - n > 0:
                generateChildren(virtualNode, next_nodes, color, knownCards, False, simulatedCard)

    del knownCards
    return next_nodes
