import copy
from src.AI.NodeToolkit import isTerminal, evaluate, nextStates


def negamax(node, depth, alpha, beta, color):

    # Creation d'une copie permettant de ne pas toucher au noeud originel

    virtualNode = copy.deepcopy(node)

    # Verification du noeud (est il terminal? Est ce que la profondeur limite est atteinte?)
    if isTerminal(node) or depth == 0:

        return color * evaluate(node)

    node.children = nextStates(virtualNode, color)

    bestValue = float('-inf')

    print(f"Number of babies : {len(node.children)} ; floor {node.floor} :")

    # for child in node.children:

    # print("Hand in the child : ", child.state.player.hand[0].title)
    # print(f"color : {-color}")
    # print(f"name of the player in this child : {child.state.player.name}")

    for child in node.children:

        # Definition de l'étage des enfants dans l'arbre
        child.floor = virtualNode.floor + 1

        # Recursivité de Negamax
        negaValue = - negamax(child, depth - 1, -beta, -alpha, -color)
        bestValue = max(bestValue, negaValue)
        print("child has", bestValue)
        alpha = max(alpha, negaValue)

        # Elagage Alpha/Beta

        if beta <= alpha:
            break

    return bestValue
