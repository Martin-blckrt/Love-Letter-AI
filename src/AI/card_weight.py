# defines every weight of cards for the evaluation function

def weights(player, knownCards, chancellor):
    a = 21 - len(knownCards)

    def spy_weight():
        if player.extraPoint:
            impact = 0
        else:
            impact = 0.5

        return impact

    def guard_weight():
        probs = []
        for Card in player.listofCards:
            b = Card.totalNumber - knownCards.count(Card)
            probs.append((b / a))

        impact = max(probs)
        return impact

    def priest_weight():
        impact = 0.15
        return impact

    def baron_weight():

        m = 0
        idx = 0
        b = player.hand[1]
        baron_index = None

        for Card in player.hand:
            if Card.value == 3:
                baron_index = idx
            idx += 1

        bool(baron_index)
        if baron_index:
            b = player.hand[0]

        for Card in player.listofCards:
            if b.value > Card.value:
                m += Card.totalNumber - knownCards.count(Card)

        impact = 1 - (m / a)
        return impact

    def handmaid_weight():
        impact = 0.2
        return impact

    def prince_weight():
        p = 1
        for Card in knownCards:
            if Card.value == 9:
                p = 0
        impact = 0.15 + (p / a)
        return impact

    def chancellor_weight():
        impact = 0.25
        return impact

    def king_weight():
        impact = 150 / a
        return impact

    def countess_weight():
        countess_index = None
        idx = 0
        b = player.hand[1]
        impact = 175 / a

        for Card in player.hand:
            if Card.value == 8:
                countess_index = idx
            idx += 1

        bool(countess_index)
        if countess_index:
            b = player.hand[0]

        if b.value == [5, 7]:
            impact = 0

        return impact

    def princess_weight():
        impact = 200 / a
        return impact

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
                    a = player.hand[i].value
                    func = switcher.get(a)
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
            impactList[j] = impact
            valueList[j] = j

        for i in range(9):

            if impactList[i] > impactList[i + 1]:
                temp = impactList[i]
                impactList[i] = impactList[i + 1]
                impactList[i + 1] = temp

                temp = valueList[i]
                valueList[i] = valueList[i + 1]
                valueList[i + 1] = temp

        return valueList
