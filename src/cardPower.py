from src.AI.card_weight import weights
from src.AI.NodeToolkit import findOccurences


def powerChancellorAI(activePlayer):
    """
    Power of the card chancellor
    :param activePlayer: Define the player who's playing the chancellor
    :return: An ordered list of index of cards that will be played by the AI
    """

    indexList = []
    knownCards = activePlayer.isolatedCards + activePlayer.hand + activePlayer.playedCards

    sortedValueList = weights(activePlayer, knownCards, True)

    for i in range(len(sortedValueList)):

        for j in range(len(activePlayer.hand)):

            if activePlayer.hand[j].value == sortedValueList[i]:
                indexList.append(j)

    return indexList


def powerPrinceAI(activePlayer):
    """
    power of the Prince (AI version)
    :param activePlayer: player that is playing the prince
    :return: The person that will be targeted with the prince.
    """

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


def prince_power(activePlayer, deck_arg, real=True):
    """
    Power of the card prince
    :param activePlayer: Define the player that is playing the prince
    :param deck_arg: deck of cards.
    :param real: check if the turn is real or virtual
    """
    if activePlayer.gender == "Human" and real:
        choice = input("\nWho do you want to target ? [You/Opponent]\n")

        while (choice != "you") and (choice != "opponent"):
            choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n")
    else:
        choice = powerPrinceAI(activePlayer)
    choice.lower()

    if choice == "you":

        target = activePlayer
        target.discard(real)

        if not deck_arg:
            target.hand.append(target.hiddenCard)
        else:
            if real:
                target.draw(deck_arg)

    else:

        target = activePlayer.opponent
        if not target.deadpool:

            target.discard(real)
            if not deck_arg:
                target.hand.append(target.hiddenCard)
            else:
                if real:
                    target.draw(deck_arg)

        else:

            print(f"{target.name} is protected : your card has no effect !\n" if real else "", end="")


def chancellor_power(activePlayer, deck_arg, real=True):
    """
    Function power of the card chancellor
     :param activePlayer: Define the player that is playing the chancellor
    :param deck_arg: deck of cards.
    :param real: check if the turn is real or virtual
    """
    if len(deck_arg) > 1:
        k = 2

    else:
        k = len(deck_arg)

    for i in range(k):
        activePlayer.draw(deck_arg)

    if real:
        print("\nThere are no more cards in the deck !\n" if not k else "", end="")

    if activePlayer.gender == "AI" or not real:
        listOfIndex = powerChancellorAI(activePlayer)
    aiCount = 0
    p = 0

    while k != 0:

        if activePlayer.gender == "Human" and real:

            print(f"\nYou need to put {k} card(s) in the deck !"
                  f"\n\nYour hand is :\n")

            for i in range(len(activePlayer.hand)):
                print(f"{i}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

            playerInput = input(f"\nWhich card do you want to place at the bottom of the deck ? Pick between 0 and {k}\n")

            numbers = "0123456789"
            numberList = list(numbers)
            availableIndexes = [numberList[i] for i in range(k+1)]

            while len(playerInput) != 1 or playerInput not in availableIndexes:
                playerInput = input(f"\nWrong input ! Remember, between 0 and {k}\n")

            index = int(playerInput)

        else:
            index = listOfIndex[aiCount]
            if listOfIndex[0] == 2:
                p = 1
            elif aiCount == 1 and index != 0 and p != 1:
                index -= 1

            aiCount += 1

        placedCard = activePlayer.hand.pop(index)
        deck_arg.append(placedCard)
        k -= 1


def king_power(activePlayer, real=True):
    """
    Power of the king card
    :param activePlayer: Define the player who's playing the king
    :param real: Check if the turn is virtual or real
    :return:
    """
    opponent = activePlayer.opponent

    print("The hands have been switched !\n" if real else "", end="")
    temp = activePlayer.hand[0]
    activePlayer.hand[0] = opponent.hand[0]
    opponent.hand[0] = temp
