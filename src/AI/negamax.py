from src.AI.NodeToolkit import isTerminal, evaluate, getAncestorCardIndex, nextStates
# from src.Game import Game
# TODO. régler limport circulaire


def negamax(node, depth, alpha, beta, color):

    fake = Game()

    virtualNode = node


    if isTerminal(node):
        return color * evaluate(node, fake.listOfCards)

    nextStates(virtualNode, fake.listOfCards, fake.isolatedCard)

    del fake  # supprimer l'instance d'objet pour eviter le bordel

    value = float('-inf')

    for child in node.children:

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    cardIndex = getAncestorCardIndex(node, value)

    return cardIndex
