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
        w = 1 / a
        impact = 150 * w
        return impact

    def countess_weight():
        w = 1 / a
        countess_index = None
        idx = 0
        b = node.state.player.hand[1]
        impact = 175 * w

        for Card in node.state.player.hand:
            if Card.value == 8:
                countess_index = idx
            idx += 1

        bool(countess_index)
        if countess_index:
            b = node.state.player.hand[0]

        if node.state.b.value == [5, 7]:
            impact = 0

        return impact

    def princess_weight():
        w = 1 / a
        impact = 200 * w
        return impact

#TODO. pondérer avec les proba de tomber sur les cartes (guarde a plus de chance que princesse)

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

    x = 0
    j = 0

    for card in node.state.listOfCards:

        if card.totalNumber - knownCards.count(card) > 0:

            j += 1
            node.state.player.hand.append(card)
            #TODO. est-ce que known cards est modifié aussi ?
            for i in range(2):
                a = node.state.player.hand[i].value
                func = switcher.get(a)
                temp = func()
                x += temp
            node.state.player.hand.remove(card)
            # TODO. est-ce que known cards est modifié aussi ?
    return x / 2 * j
