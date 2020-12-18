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

    # arrondi pour éviter décimale infinie

    impact = round(impact, 5)
    return impact


def getAncestor(testedChild, value):

    children = testedChild.children

    if testedChild.value == value:
        print(f"\nje vais return ce child : {testedChild}")
        print(f"parent of the child : {testedChild.parent}")

        target = testedChild

        return target

    else:
        for newChild in children:
            result = getAncestor(newChild, value)

            if not result:
                continue


def getAncestorCardIndex(node, value):

    origin = node
    lineage = []

    # On skip les noeuds humain dans l'arbre
    for humanChild in origin.children:
        for aiChild in humanChild.children:
            lineage.append(aiChild)

    for testedChild in lineage:
        target = getAncestor(testedChild, value)

        if target:
            break

    print("target : ", target)

    while target.parent.parent:
        print("found parents !")
        target = target.parent

    originHand = origin.state.player.hand
    targetHand = target.state.player.hand

    # debug for print :
    print("\n____________  PRINT DEBUG IN getAncestorIndex _____________\n")

    print("origin hand : ")
    for j in range(len(originHand)):
        print(f"{originHand[j].title} ")

    for a in range(len(targetHand)):
        print(f"targetHand = {targetHand[a].title}")
    # end debug print

    # TODO. Au secours prince et adresses

    i = 0

    for i in range(len(originHand)):
        if targetHand[0].title != originHand[i].title:
            print(f"found different card at {i}")
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
    print(f"we know {i}/{card.totalNumber} occurences of {card.title}")
    return i

# TODO. gérer THE exception index est dans hiddencard


def findOccurences(card, searchedList):

    i = 0
    for aCard in searchedList:
        if card.value == aCard.value:
            i += 1
    # print(f"we know {i}/{card.totalNumber} occurences of {card.title}")
    return i

# TODO. gérer THE exception index est dans hiddencard


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

            activePlayer.playTurn(newVirtualNode.state.deck, i, caption=False)

            if not activePlayer.hand:

                # cas ou le prince a été joué
                print("JE SUIS DANS if not activePlayer.hand")
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

            elif not activePlayer.opponent.hand:
                # TODO. Verif si le bon joueur est manipulé (peut etre la cause des node color opposee)

                print("JE SUIS DANS elif not activePlayer.opponent.hand")
                drawnCard = newVirtualNode.state.deck.pop(0)
                activePlayer.opponent.hand.append(drawnCard)

                next_nodes.append(newVirtualNode)

            else:
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
