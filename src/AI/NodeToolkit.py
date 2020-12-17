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


def getAncestor(lineage, value):

    for child in lineage:

        if child.value == value:

            print(f"\nje vais return ce child : {child}")
            print(f"parent of the child : {child.parent}")
            target = child
            break

        else:
            target = getAncestor(child.children, value)

    return target


def getAncestorCardIndex(node, value):

    origin = node
    lineage = []

    # On skip les noeuds humain dans l'arbre
    for humanChild in origin.children:
        for aiChild in humanChild.children:
            lineage.append(aiChild)

    target = getAncestor(lineage, value)

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

    #TODO. Au secours prince et adresses
    i = 0

    for i in range(len(originHand)):
        if targetHand[0].title != originHand[i].title:
            print(f"found different card at {i}")
            return i

    # cas défaut
    return i


def isTerminal(node):

    cond1 = not node.state.deck  # deck vide
    cond2 = (not node.state.player.isAlive) or node.state.opponent.hasWon
    cond3 = (not node.state.opponent.isAlive) or node.state.player.hasWon

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


def generateChildren(virtualNode, next_nodes, knownCards, color, firstTurn, *simulatedCard):

    for i in range(2):  # Pour chaque carte de la main

        # on cree une copie du noeud pour genere des enfants de celui ci

        newVirtualNode = copy.deepcopy(virtualNode)
        newVirtualNode.parent = virtualNode  # on definit le parent du nouveau noeud

        if firstTurn:
            activePlayer = newVirtualNode.state.player
            index = -1
            print("_____________ FIRST TURN ________________")
        else:
            if color == 1:
                activePlayer = newVirtualNode.state.player
            else:
                activePlayer = newVirtualNode.state.opponent

            print(f"player name : {activePlayer.name}")
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
                            activePlayer = princedNode.state.opponent

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
        activePlayer = virtualNode.state.opponent

    next_nodes = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    # debug print
    print(f"\nNode player in nextstate : {activePlayer.name}")

    print("KC début next state : ")
    for i in range(len(knownCards)):
        print(knownCards[i].title, end=", ")

    print("\nactivePlayer.hand")
    for i in range(len(activePlayer.hand)):
        print(activePlayer.hand[i].title, end=", ")

    print("\nactivePlayer.playedCards")
    for i in range(len(activePlayer.playedCards)):
        print(activePlayer.playedCards[i].title, end=", ")

    print("\n")
    # end debug print

    cond1 = len(virtualNode.state.deck) == 12 and activePlayer.playedCards[1].value == 5

    if color == 1 and (len(virtualNode.state.deck) == 13 or cond1):

        generateChildren(virtualNode, next_nodes, knownCards, color, True)

    else:

        for simulatedCard in virtualNode.state.listOfCards:
            n = findOccurences(simulatedCard, knownCards)

            if simulatedCard.totalNumber - n > 0:
                generateChildren(virtualNode, next_nodes, knownCards, color, False, simulatedCard)

    return next_nodes
