# defines every weight of cards for the evaluation function
def weights(node, knownCards):
    def spy_weight():
        if node.state.player.extraPoint:
            impact = 0
        else:
            impact = 0.5

        return impact

    def guard_weight():
        probs = []
        b = 21 - len(knownCards)
        for Card in node.state.player.listofCards:
            a = Card.totalNumber - knownCards.count(Card)
            probs.append((a / b))

        impact = max(probs)
        return impact

    def priest_weight():
        impact = 0.15
        return impact

    def baron_weight():
        a = 21 - len(knownCards)
        j = 0
        b = node.state.player.hand[1]

        baron_index = node.state.player.hand.index(baron_card)
        bool(baron_index)
        if baron_index:
            b = node.state.player.hand[0]

        for Card in node.state.player.listofCards:
            if b.value > Card.value:
                i = Card.totalNumber - knownCards.count(Card)
                j += i

        impact = 1 - (j / a)
        return impact

    def handmaid_weight():
        impact = 0.2
        return impact

    def prince_weight():
        p = node.state.princess_card.totalNumber - knownCards.count(node.state.princess_card)
        impact = 0.15 + p / (21 - len(knownCards))
        return impact

    def chancellor_weight():
        impact = 0.25
        return impact

    def king_weight():
        a = 1 / (21 - len(knownCards))
        impact = 150 * a
        return impact

    def countess_weight():
        a = 1 / (21 - len(knownCards))
        b = node.state.player.hand[1]
        impact = 175 * a

        countess_index = node.state.player.hand.index(node.state.countess_card)
        bool(countess_index)

        if countess_index:
            b = node.state.player.hand[0]

        if node.state.b.value == [5, 7]:
            impact = 0

        return impact

    def princess_weight():
        a = 1 / (21 - len(knownCards))
        impact = 200 * a
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

    x = 0

    for i in range(2):
        a = node.state.player.hand[i].value
        func = switcher.get(a)
        temp = func()
        x += temp

    return x/2
