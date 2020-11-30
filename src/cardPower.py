# TODO. ajouter les captions True

def prince_power(activePlayer, deck_arg):
    choice = input("\nWho do you want to target ? [You/Opponent]\n")
    # TODO: peut etre trouver une alternative à 'opponent' (frost)
    choice.lower()

    while (choice != "you") and (choice != "opponent"):
        choice = input("\nIncorrect Input ! Who do you want to target ? [You/Opponent]\n")
        choice.lower()

    if choice == "you":
        target = activePlayer
        target.discard()
        target.draw(deck_arg)
    else:
        target = activePlayer.opponent
        if not target.deadpool:
            target.discard()
            target.draw(deck_arg)
        else:
            print(f"{target.name} is protected : your card has no effect !\n")


def chancellor_power(activePlayer, deck_arg):
    j = 0

    if len(deck_arg) > 1:
        k = 2
    else:
        k = len(deck_arg)

    for i in range(k):
        activePlayer.draw(deck_arg)
        j += 1

    if j == 0:
        print("\nThere are no more cards in the deck !")

    else:
        if j == 2:
            print(
                f"You need to get rid of 2 of your cards by placing them "
                f"at the bottom of the deck. Your hand is :\n")
            for i in range(len(activePlayer.hand)):
                print(f"{i + 1}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

            index = int(
                input("Which card do you want to place as the penultimate card in the deck ? (1/2/3)\n"))
            while index not in [1, 2, 3]:
                index = int(input(
                    "\nWrong input ! Which card do you want to place "
                    "as the penultimate card in the deck ? (1/2/3)\n"))

            placedCard = activePlayer.hand.pop(index - 1)
            deck_arg.append(placedCard)

        print(f"\nYou now need to get rid of 1 of your cards by placing it at the bottom of the deck."
              f"\n\nYour hand is :\n")

        for i in range(len(activePlayer.hand)):
            print(f"{i + 1}. {activePlayer.hand[i].title} [{activePlayer.hand[i].value}]")

        index = int(input("Which card do you want to place as the last card in the deck ? (1/2)\n"))
        while index not in [1, 2]:
            index = int(
                input("\nWrong input ! Which card do you want to place as the last card in the deck ? (1/2)\n"))

        placedCard = activePlayer.hand.pop(index - 1)
        deck_arg.append(placedCard)


def king_power(activePlayer):
    opponent = activePlayer.opponent

    print("The hands have been switched !\n")
    temp = activePlayer.hand[0]
    activePlayer.hand[0] = opponent.hand[0]
    opponent.hand[0] = temp
