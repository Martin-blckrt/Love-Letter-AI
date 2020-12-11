from src.AI.NodeToolkit import isTerminal, evaluate, getAncestorCardIndex, nextStates
import copy


def negamax(node, depth, alpha, beta, color):
    virtualNode = copy.deepcopy(node)

    if isTerminal(node) or depth == 0:
        return color * evaluate(node)

    node.children = nextStates(virtualNode)

    value = float('-inf')

    for child in node.children:

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    return value
