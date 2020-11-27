from src.IA.NodeManipulationToolkit import isTerminal, evaluate


def negamax(node, depth, alpha, beta, color):

    if isTerminal(node):
        return color * evaluate(node)

    # generate children
    # generate moves

    value = float('-inf')

    for child in node.children:

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, color))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    return value
