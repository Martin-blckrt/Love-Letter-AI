import copy
from src.AI.NodeToolkit import isTerminal, evaluate, nextStates


def negamax(node, depth, alpha, beta, color):
    # Creation d'une copie permettant de ne pas toucher au noeud originel

    virtualNode = copy.deepcopy(node)

    # Verification du noeud (est il terminal? Est ce que la profondeur limite est atteinte?)
    if isTerminal(node) or depth == 0:
        node.value = color * evaluate(node)
        return color * evaluate(node)

    node.children = nextStates(virtualNode, color)

    bestValue = -1000000

    print(f"Number of babies : {len(node.children)} ; floor {node.floor} :")

    for child in node.children:
        # Definition de l'étage des enfants dans l'arbre
        child.floor = virtualNode.floor + 1

        # Recursivité de Negamax
        negaValue = - negamax(child, depth - 1, -beta, -alpha, -color)
        child.value = negaValue

        bestValue = max(bestValue, negaValue)

        alpha = max(alpha, negaValue)

        # Elagage Alpha/Beta

        if beta <= alpha:
            return alpha

    return bestValue