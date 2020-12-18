# -----------------------------------------------
# Fichier regroupant les fonctions representant les actifs des cartes suivantes :
#   - prince
#   - Roi
#   - Chancelier
#
# Isolées pour la clarté du code.
# -----------------------------------------------
# TODO. refaire prince
# TODO. mettre fonction findCard partout ou y avait for card in listOfcards

from src.AI.card_weight import weights
from src.AI.NodeToolkit import findCard
from src.AI.NodeToolkit import findOccurences


def powerChancellorAI(activePlayer):
    indexList = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    sortedValueList = weights(activePlayer, knownCards, True)

    for i in range(len(sortedValueList)):

        for j in range(len(activePlayer.hand)):

            if activePlayer.hand[j].value == sortedValueList[i]:
                indexList.append(j)

    return indexList


def powerPrinceAI(activePlayer):
    if activePlayer.hand[0].value in [4, 6, 9]:
        return "opponent"

    elif activePlayer.hand[0].value == 0:

        if activePlayer.extraPoint:
            return "you"
        else:
            return "opponent"

    elif activePlayer.hand[0].value == 1:

        knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

        probs = []
        b = 21 - len(knownCards)

        for Card in activePlayer.listOfCards:
            n = findOccurences(Card, knownCards)
            a = Card.totalNumber - n
            probs.append((a / b))

        impact = max(probs)

        if impact > 0.2:
            return "opponent"
        else:
            return "you"

    else:
        return "you"


def prince_power(activePlayer, deck_arg, caption=True):
    if activePlayer.gender == "Human" and caption:
        choice = input("\nWho do you want to target ? [You/Opponent]\n")
        choice.lower()

        while (choice != "you") and (choice != "opponent"):
            choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n")
            choice.lower()
    else:
        choice = powerPrinceAI(activePlayer)
        choice.lower()

    if choice == "you":

        target = activePlayer
        target.discard(caption)

        if not deck_arg:
            target.hand.append(target.hiddenCard)
        else:
            if caption:
                target.draw(deck_arg)

    else:

        target = activePlayer.opponent
        if not target.deadpool:

            target.discard(caption)
            if not deck_arg:
                target.hand.append(target.hiddenCard)
            else:
                if caption:
                    target.draw(deck_arg)

        else:
            print(f"{target.name} is protected : your card has no effect !\n" if caption else "")


def chancellor_power(activePlayer, deck_arg, caption=True):
    if len(deck_arg) > 1:
        k = 2

    else:
        k = len(deck_arg)

    for i in range(k):
        activePlayer.draw(deck_arg)

    print("\nThere are no more cards in the deck !" if not k else "")

    if activePlayer.gender == "AI" or not caption:
        listOfIndex = powerChancellorAI(activePlayer)
        print("list of index is : ", listOfIndex)
    aiCount = 0

    while k != 0:

        if activePlayer.gender == "Human" and caption:

            print(f"\nYou need to put {k} card(s) in the deck !"
                  f"\n\nYour hand is :\n")

            for i in range(len(activePlayer.hand)):
                print(f"{i}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

            playerInput = input(f"Which card do you want to place at the bottom of the deck ? Pick between 0 and {k}\n")

            numbers = "0123456789"
            numberList = list(numbers)
            availableIndexes = [numberList[i] for i in range(k+1)]

            while len(playerInput) != 1 or playerInput not in availableIndexes:
                playerInput = input(f"\nWrong input ! Remember, between 0 and {k}\n")

            index = int(playerInput)

        else:
            index = listOfIndex[aiCount]
            if aiCount == 1 and index != 0:
                index -= 1
            print("index is : ", index)
            aiCount += 1

        placedCard = activePlayer.hand.pop(index)
        deck_arg.append(placedCard)
        k -= 1


def king_power(activePlayer, caption=True):
    opponent = activePlayer.opponent

    print("The hands have been switched !\n" if caption else "")
    temp = activePlayer.hand[0]
    activePlayer.hand[0] = opponent.hand[0]
    opponent.hand[0] = temp
