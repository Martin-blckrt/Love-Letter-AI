# defines every weight of cards for the evaluation function

# TODO. Tout refaire

def weights(node, knownCards):
    a = 21 - len(knownCards)

    def spy_weight():
        if node.state.player.extraPoint:
            impact = 0
        else:
            impact = 0.5

        return impact

    def guard_weight():
        probs = []
        for Card in node.state.player.listofCards:
            b = Card.totalNumber - knownCards.count(Card)
            probs.append((b / a))

        impact = max(probs)
        return impact

    def priest_weight():
        impact = 0.15
        return impact

    def baron_weight():

        j = 0
        idx = 0
        b = node.state.player.hand[1]
        baron_index = None

        for Card in node.state.player.hand:
            if Card.value == 3:
                baron_index = idx
            idx += 1

        bool(baron_index)
        if baron_index:
            b = node.state.player.hand[0]

        for Card in node.state.player.listofCards:
            if b.value > Card.value:
                j += Card.totalNumber - knownCards.count(Card)

        impact = 1 - (j / a)
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
        b = node.state.player.hand[1]
        impact = 175 / a

        for Card in node.state.player.hand:
            if Card.value == 8:
                countess_index = idx
            idx += 1

        bool(countess_index)
        if countess_index:
            b = node.state.player.hand[0]

        if b.value == [5, 7]:
            impact = 0

        return impact

    def princess_weight():
        impact = 200 / a
        return impact

# TODO. pondérer avec les proba de tomber sur les cartes (guarde a plus de chance que princesse)

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

    mean = 0
    j = 0
    x = 0 #pour enlever un warning 0 use

    for card in node.state.player.listOfCards:

        n = card.totalNumber - knownCards.count(card)
        if n > 0:

            x = 0
            j += 1

            node.state.player.hand.append(card)
            knownCards.append(card)

            for i in range(2):
                a = node.state.player.hand[i].value
                func = switcher.get(a)
                temp = func()
                x += temp

            mean += n * x / a
            node.state.player.hand.remove(card)
            knownCards.remove(card)

    return mean / (2 * j)
