import copy
from src.AI.NodeToolkit import isTerminal, evaluate, nextStates


def negamax(node, depth, alpha, beta, color):

    virtualNode = copy.deepcopy(node)

    # TODO. Generation & valeurs des noeuds

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

        # child.value = evaluate(child)

        child.floor = virtualNode.floor + 1
        negaValue = - negamax(child, depth - 1, -beta, -alpha, -color)
        bestValue = max(bestValue, negaValue)

        alpha = max(alpha, negaValue)

        if beta <= alpha:
            break

    return bestValue
