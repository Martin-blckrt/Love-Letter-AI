# -----------------------------------------
#  Fichier permettant de determiner les poids de chaque carte nécessaires au bon fonctionnement de la fonction evaluate
#  --> weights() : utilisation d'un switcher pour savoir quelle sous fonctione utiliser ;
#  Cette fonction est aussi utilisé par la fonction powerChancellorAI.
# -----------------------------------------
# TODO. if terminal node, mettre valeur en fonction de qui est vivant

def weights(player, knownCards, chancellor):

    print(f"\nau debut de weights, len knowncards : ", len(knownCards))
    for i in range(len(knownCards)):
        print(knownCards[i].title)

    print(f"player.pLayedcards in weights : ")
    for j in range(len(player.playedCards)):
        print(player.playedCards[j].title)

    print(f"opponent.pLayedcards in weights : ")
    for j in range(len(player.opponent.playedCards)):
        print(player.opponent.playedCards[j].title)

    a = 21 - len(knownCards)
    d = 0
    if player.opponent.deadpool:
        d = 0.15

    def spy_weight():

        if player.extraPoint:

            spy_impact = 0
        else:
            spy_impact = 0.5

        return spy_impact

    def guard_weight():

        probabilities = []

        for Card in player.listOfCards:

            b = Card.totalNumber - knownCards.count(Card)
            probabilities.append((b / a))

        guard_impact = max(probabilities) - d

        return guard_impact

    def priest_weight():

        return 0.15 - d

    def baron_weight():

        if chancellor:
            baron_impact = 0
        else:
            m = 0
            b = player.hand[1]

            if player.hand[1].value == 3:
                b = player.hand[0]

            for Card in player.listOfCards:
                if b.value > Card.value:
                    m += Card.totalNumber - knownCards.count(Card)

            baron_impact = (m / a) - d

        return baron_impact

    def handmaid_weight():

        return .2

    def prince_weight():
        p = 1
        for Card in knownCards:
            if Card.value == 9:
                p = 0
        prince_impact = 0.15 + (p / a)
        return prince_impact

    def chancellor_weight():

        return 0.25

    def king_weight():

        return (1.5 / a) - d

    def countess_weight():
        countess_impact = 1.75 / a
        if not chancellor:
            countess_index = None
            b = player.hand[1]

            if player.hand[1].value == 8:
                b = player.hand[0]

            if b.value == [5, 7]:
                countess_impact = 0

        return countess_impact

    def princess_weight():

        return 2 / a

    switcher = {
        0: spy_weight,
        1: guard_weight,
        2: priest_weight,
        3: baron_weight,
        4: handmaid_weight,
        5: prince_weight,
        6: chancellor_weight,
        7: king_weight,
        8: countess_weight,
        9: princess_weight
    }

    if not chancellor:

        mean = 0
        j = 0

        for card in player.listOfCards:

            n = card.totalNumber - knownCards.count(card)
            if n > 0:

                x = 0
                j += 1

                player.hand.append(card)
                knownCards.append(card)

                for i in range(2):
                    switchValue = player.hand[i].value
                    func = switcher.get(switchValue)
                    temp = func()
                    x += temp

                mean += n * x / a
                player.hand.remove(card)
                knownCards.remove(card)

        return mean / (2 * j)

    else:
        impactList = []
        valueList = []

        for j in range(10):
            func = switcher.get(j)
            impact = func()
            impactList.append(impact)
            valueList.append(j)

        for i in range(9):

            if impactList[i] > impactList[i + 1]:
                temp = impactList[i]
                impactList[i] = impactList[i + 1]
                impactList[i + 1] = temp

                temp = valueList[i]
                valueList[i] = valueList[i + 1]
                valueList[i + 1] = temp

        return valueList
