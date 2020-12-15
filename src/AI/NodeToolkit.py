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

            impact = m / (1 - len(knownCards))

            if node.state.player.extraPoint:
                impact += 0.5
    else:
        impact = weights(node.state.player, knownCards, False)

    # arrondi pour éviter décimale infinie

    impact = round(impact, 5)
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
    lost = False
    target = node

    print(f"WE ARE LOOKING FOR {value} BUT I HAVE {node.value}")
    if node.value == value:
        target = node

    elif node.children:
        for child in node.children:
            target = getAncestor(child, value)
    else:
        lost = True
        print("Value not found")

    return target, lost


def getAncestorCardIndex(node, value):
    # TODO. WORK on it, NoneType error, Tuple error
    # returns the index of the card that we should play next

    origin = node

    target, lost = getAncestor(node, value)
    print("target", target)
    print("lost", lost)

    if not lost:
        while target.parent.parent:
            node = node.parent

        hand = node.state.player.hand
        originHand = origin.state.player.hand

        for index in range(len(hand)):
            if not hand[index] == originHand[index]:
                return index
    else:
        print("I AM LOST FOREVER IN THE DEEP COLD SEA")


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
    print(f"we know {i}/{card.totalNumber} occurences of {card.title}")
    return i


def generateChildren(virtualNode, next_nodes, knownCards, color, firstTurn, *simulatedCard):

    for i in range(2):  # Pour chaque carte de la main

        # on cree une copie du noeud pour genere des enfants de celui ci

        newVirtualNode = copy.deepcopy(virtualNode)
        newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

        if firstTurn:
            activePlayer = newVirtualNode.state.player

        else:
            if color == 1:
                activePlayer = newVirtualNode.state.player
            else:
                activePlayer = newVirtualNode.state.opponent

            index = findCard(simulatedCard[0].value, newVirtualNode.state.deck)

            activePlayer.hand.append(newVirtualNode.state.deck[index])
            del newVirtualNode.state.deck[index]

            knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

        # debug print
        print("hand :")
        for count in range(len(activePlayer.hand)):
            print(activePlayer.hand[count].title, end=", ")
        print("\n")
        # end debug print

        activePlayer.playTurn(newVirtualNode.state.deck, i, caption=False)

        if not activePlayer.hand:
            # cas ou le prince a été joué

            for drawnCard in virtualNode.state.listOfCards:
                # TODO. A vérifier si c'est bien drawnCard (c'était simulatedCard avant)
                n = findOccurences(drawnCard, knownCards)

                if drawnCard.totalNumber - n > 0:
                    princedNode = copy.deepcopy(newVirtualNode)
                    princedNode.parent = virtualNode

                    index = findCard(drawnCard.value, newVirtualNode.state.deck)

                    activePlayer.hand.append(newVirtualNode.state.deck[index])
                    del newVirtualNode.state.deck[index]

                    next_nodes.append(princedNode)

        elif not activePlayer.opponent.hand:
            # TODO. Verif si le bon joueur est manipulé (peut etre la cause des node color opposee

            drawnCard = newVirtualNode.state.deck.pop(0)
            activePlayer.opponent.hand.append(drawnCard)

            next_nodes.append(newVirtualNode)

        else:
            next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.


def nextStates(virtualNode, color):

    if color == 1:
        activePlayer = virtualNode.state.player
    else:
        activePlayer = virtualNode.state.opponent

    next_nodes = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    # debug print
    print(f"\nNode player : {activePlayer.name}\nnode value : {virtualNode.value}\n")

    print("KC début next state : ")
    for i in range(len(knownCards)):
        print(knownCards[i].title, end=", ")

    print("\n")
    # end debug print

    if len(virtualNode.state.deck) >= 12 and color == 1:
        generateChildren(virtualNode, next_nodes, knownCards, color, True)

    else:

        for simulatedCard in virtualNode.state.listOfCards:
            n = findOccurences(simulatedCard, knownCards)

            if simulatedCard.totalNumber - n > 0:

                generateChildren(virtualNode, next_nodes, knownCards, color, False, simulatedCard)

    return next_nodes
