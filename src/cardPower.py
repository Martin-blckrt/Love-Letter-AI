# -----------------------------------------------
# Fichier regroupant les fonctions representant les actifs des cartes suivantes :
#   - prince
#   - Roi
#   - Chancelier
#
# Isolées pour la clarté du code.
# -----------------------------------------------

from src.AI.card_weight import weights


def powerChancellorAI(activePlayer):

    indexList = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards + \
        activePlayer.opponent.playedCards

    sortedValueList = weights(activePlayer, knownCards, True)

    for i in range(len(sortedValueList)):

        for j in range(len(activePlayer.hand)):

            if activePlayer.hand[j].value == sortedValueList[i]:
                indexList.append(j)
                # avant c'était indexList.append(i) mais ça marche pas car l'index serait entre 0-9

    return indexList


def powerPrinceAI(activePlayer):

    if activePlayer.hand[0].value == 9:
        return "opponent"
    elif activePlayer.hand[0].value == 0 and activePlayer.extraPoint:
        return "you"
    elif activePlayer.hand[0].value == 1:

        knownCards = activePlayer.isolatedCards + activePlayer.hand + \
                     + activePlayer.playedCards + activePlayer.opponent.playedCards

        probs = []
        b = 21 - len(knownCards)

        for Card in activePlayer.listofCards:
            a = Card.totalNumber - knownCards.count(Card)
            probs.append((a / b))

        impact = max(probs)

        if impact > 0.2:
            return "opponent"


def prince_power(activePlayer, deck_arg, caption=True):

    if activePlayer.gender == "Human":
        choice = input("\nWho do you want to target ? [You/Opponent]\n")
        choice.lower()

    else:
        choice = powerPrinceAI(activePlayer)

    while (choice != "you") and (choice != "opponent"):
        choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n" if caption else None)
        choice.lower()

    if choice == "you":

        target = activePlayer
        target.discard()
        if not deck_arg:
            target.hand[0] = target.hiddenCard
        else:
            target.draw(deck_arg)

    else:

        target = activePlayer.opponent
        if not target.deadpool:

            target.discard()
            if not deck_arg:
                target.hand[0] = target.hiddenCard
            else:
                target.draw(deck_arg)

        else:
            print(f"{target.name} is protected : your card has no effect !\n" if caption else None)


def chancellor_power(activePlayer, deck_arg, caption=True):

    if len(deck_arg) > 1:
        k = 2

    else:
        k = len(deck_arg)

    for i in range(k):
        activePlayer.draw(deck_arg)

    print("\nThere are no more cards in the deck !" if not k else None)

    while k != 0:

        aiCount = 0
        if activePlayer.gender == "Human":

            if caption:
                print(f"\n you need to put {k} card(s) in the deck !"
                      f"\n\nYour hand is :\n")

                for i in range(len(activePlayer.hand)):
                    print(f"{i}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

                index = int(
                    input(f"Which card do you want to place at the bottom of the deck ? Pick between 0 and {k}\n"))

                availableIndexes = list(range(k + 1))

                while index not in availableIndexes:
                    index = int(input(f"\nWrong input ! Remember, between 0 and {k}\n"))

        else:
            listOfIndex = powerChancellorAI(activePlayer)
            index = listOfIndex[aiCount]
            aiCount += 1

        placedCard = activePlayer.hand.pop(index)
        deck_arg.append(placedCard)
        k -= 1

    """
    if j == 0:

        print("\nThere are no more cards in the deck !")

    else:

        
        Dans le cas ou le deck a une longueur strict. supérieure à 0.
            - Le test j = 2 permet de tirer une seconde carte.
            - l'autre cas, executé dans tous les cas, permet de tirer une carte.
    

        if j == 2:

            print(
                f"You need to get rid of 2 of your cards by placing them "
                f"at the bottom of the deck. Your hand is :\n" if caption else None)

            for i in range(len(activePlayer.hand)):
                print(f"{i + 1}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]" if caption else None)

            if activePlayer.gender == "Human":
                index = int(input("Which card do you want to place as the penultimate card in the deck ? (0/1/2)\n"))

                while index not in [0, 1, 2]:
                    index = int(input(
                        "\nWrong input ! Which card do you want to place "
                        "as the penultimate card in the deck ? (0/1/2)\n"))

            else:
                listOfIndex = powerChancellorAI(activePlayer)
                index = listOfIndex[1]

            placedCard = activePlayer.hand.pop(index)
            deck_arg.append(placedCard)

        if activePlayer.gender == "Human":

            print(f"\nYou now need to get rid of 1 of your cards by placing it at the bottom of the deck."
                  f"\n\nYour hand is :\n" if caption else None)

            for i in range(len(activePlayer.hand)):
                print(f"{i}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]" if caption else None)

            index = int(input("Which card do you want to place as the last card in the deck ? (0/1)\n"))

            while index not in [0, 1]:
                index = int(
                    input("\nWrong input ! Which card do you want to place as the last card in the deck ? (0/1)\n"))
        else:
            listOfIndex = powerChancellorAI(activePlayer)
            index = listOfIndex[0]

        placedCard = activePlayer.hand.pop(index)
        deck_arg.append(placedCard)
    """


def king_power(activePlayer, caption=True):
    opponent = activePlayer.opponent

    print("The hands have been switched !\n" if caption else None)
    temp = activePlayer.hand[0]
    activePlayer.hand[0] = opponent.hand[0]
    opponent.hand[0] = temp
