from src.AI.NodeToolkit import isTerminal, evaluate, getAncestorCardIndex, nextStates
from src.Game import Game



def negamax(node, depth, alpha, beta, color):

    if isTerminal(node):
        return color * evaluate(node)

    fake = Game()

    virtualNode = node

    nextStates(virtualNode, fake.listOfCards)

    del fake  # supprimer l'instance d'objet pour eviter le bordel

    value = float('-inf')

    for child in node.children:

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    cardIndex = getAncestorCardIndex(node, value)

    return cardIndex
