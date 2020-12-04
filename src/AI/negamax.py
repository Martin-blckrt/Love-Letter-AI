from src.AI.NodeToolkit import isTerminal, evaluate, getAncestorCardIndex, nextStates
import copy


def negamax(node, depth, alpha, beta, color):

    virtualNode = copy.deepcopy(node)


    if isTerminal(node):
        return color * evaluate(node, fake.listOfCards)

    nextStates(virtualNode)

    value = float('-inf')

    for child in node.children:

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    cardIndex = getAncestorCardIndex(node, value)

    return cardIndex
