# defines every weight of cards for the evaluation function

def spy_weight(node):
    if node.state.player1.extrapoint:
        impact = 0
    else:
        impact = 0.5

    return impact


def guard_weight():
    pass


def priest_weight():
    impact = 0.15
    return impact


def baron_weight(node, knownCards):
    a = 21 - len(knownCards)
    j = 0
    b = node.state.player1.hand[1]

    baron_index = node.state.player1.hand.index(node.state.baron_card)
    bool(baron_index)
    if baron_index:
        b = node.state.player1.hand[0]

    for i in range(a):
        # if b > cartes inconnues
        j += 1

    impact = 1 - (j / a)

    return impact


def handmaid_weight():
    impact = 0.2
    return impact


def prince_weight(node, knownCards):
    impact = 0.15 + node.state.princess_card.left_Number / (21 - len(knownCards))
    return impact


def chancellor_weight():
    impact = 0.25
    return impact


def king_weight(knownCards):
    a = 1 / (21 - len(knownCards))
    impact = 150 * a
    return impact


def countess_weight(node, knownCards):
    a = 1 / (21 - len(knownCards))
    b = node.state.player1.hand[1]
    impact = 175 * a

    countess_index = node.state.player1.hand.index(node.state.countess_card)
    bool(countess_index)

    if countess_index:
        b = node.state.player1.hand[0]

    if node.state.b.value == [5, 7]:
        impact = 0

    return impact


def princess_weight(knownCards):
    a = 1 / (21 - len(knownCards))
    impact = 200 * a
    return impact
