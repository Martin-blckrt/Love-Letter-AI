import copy
from src.AI.card_weight import weights
from src.AI.Node import dfs, getPathFrom


def evaluate(node):

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

    # copie du noeud de départ pour eviter des modifs non prévuees
    start = copy.deepcopy(node)

    # DFS
    dfsResultList = getAncestor(start, value)

    # On récupère le dernier de la liste
    # Normalement c'est celui qui a la valeur cherchée

    lastKid = dfsResultList[-1]
    path = getPathFrom(lastKid)

    # sauf erreur de ma part, le noeud voulu est à un 1
    # 0 est le noeud start
    target = path[1]

    originHand = start.state.player.hand
    targetHand = target.state.player.opponent.hand

    i = 0

    for i in range(len(originHand)):
        if targetHand[0].title != originHand[i].title:
            return i

    # cas défaut
    return i


def isTerminal(node):

    cond1 = not node.state.deck  # deck vide
    cond2 = (not node.state.player.isAlive) or node.state.player.opponent.hasWon
    cond3 = (not node.state.player.opponent.isAlive) or node.state.player.hasWon

    return cond1 or cond2 or cond3


def getNodeValue(node):
    # Utile si besoin de debugger.
    return node.value


def findCard(cardvalue, selectedList):

    index = -1
    for i in range(len(selectedList)):
        if cardvalue == selectedList[i].value:
            index = i
    print("index in findCard is : ", index)
    print("first card of deck is : ", selectedList[0].title)
    return index


def findOccurences(card, searchedList):

    i = 0

    for aCard in searchedList:
        if card.value == aCard.value:
            i += 1

    return i


def generateChildren(virtualNode, next_nodes, color, knownCards, firstTurn, *simulatedCard):

    for i in range(2):  # Pour chaque carte de la main


        # on cree une copie du noeud pour genere des enfants de celui ci

        newVirtualNode = copy.deepcopy(virtualNode)
        newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

        print(f"\nau debut du for, len knowncards : ", len(knownCards))
        for k in range(len(knownCards)):
            print(knownCards[k].title)

        print(f"player.pLayedcards in for : ")
        for a in range(len(newVirtualNode.state.player.playedCards)):
            print(newVirtualNode.state.player.playedCards[a].title)

        print(f"opponent.pLayedcards in for : ")
        for j in range(len(newVirtualNode.state.player.opponent.playedCards)):
            print(newVirtualNode.state.player.opponent.playedCards[j].title)

        if firstTurn:
            activePlayer = newVirtualNode.state.player
            index = -1
            # print("_____________ FIRST TURN ________________")

        else:

            if color == 1:
                activePlayer = newVirtualNode.state.player
            else:
                activePlayer = newVirtualNode.state.player.opponent

            # print(f"player name : {activePlayer.name}")
            index = findCard(simulatedCard[0].value, newVirtualNode.state.deck)

            if index != -1:
                activePlayer.hand.append(newVirtualNode.state.deck[index])
                del newVirtualNode.state.deck[index]

            knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

        if index == -1 and not firstTurn:
            del newVirtualNode

        else:

            # debug print
            print("hand between 2 nodes :")
            for count in range(len(activePlayer.hand)):
                print(activePlayer.hand[count].title, end=", ")
            print("\n")
            # end debug print

            activePlayer.playTurn(newVirtualNode.state.deck, i, real=False)

            if not activePlayer.hand:

                # cas ou le prince a été joué
                for drawnCard in virtualNode.state.listOfCards:
                    # TODO. A vérifier si c'est bien drawnCard (c'était simulatedCard avant)
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
                            print("J'ajoute le node dans le if")

            elif not activePlayer.opponent.hand:
                # TODO. Verif si le bon joueur est manipulé (peut etre la cause des node color opposee)

                drawnCard = newVirtualNode.state.deck.pop(0)
                activePlayer.opponent.hand.append(drawnCard)
                print("J'ajoute le node dans le elif")

                next_nodes.append(newVirtualNode)

            else:
                print("J'ajoute le node dans le else")
                next_nodes.append(newVirtualNode)  # on ajoute new child à la liste des noeuds.


def nextStates(virtualNode, color):

    if color == 1:
        activePlayer = virtualNode.state.player
    else:
        activePlayer = virtualNode.state.player.opponent

    next_nodes = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    # debug print
    print(f"\nNode player in nextstate : {activePlayer.name}")

    print("KC début next state : ")
    for i in range(len(knownCards)):
        print(knownCards[i].title, end=", ")

    print(f"{len(knownCards)}\n")
    # end debug print

    if len(activePlayer.hand) == 2:

        generateChildren(virtualNode, next_nodes, color, knownCards, True)

    else:

        for simulatedCard in virtualNode.state.listOfCards:
            n = findOccurences(simulatedCard, knownCards)

            if simulatedCard.totalNumber - n > 0:
                generateChildren(virtualNode, next_nodes, color, knownCards, False, simulatedCard)

    del knownCards
    return next_nodes
