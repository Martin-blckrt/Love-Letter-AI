import copy
from src.AI.NodeToolkit import isTerminal, evaluate, nextStates


def negamax(node, depth, alpha, beta, color):
    virtualNode = copy.deepcopy(node)

    # TODO. Generation & valeurs des noeuds

    if isTerminal(node) or depth == 0:

        node.value = evaluate(node)

        return color * node.value

    node.children = nextStates(virtualNode, color)

    print(f"\n{len(node.children)} babies at floor {node.floor} :")

    value = float('-inf')

    for child in node.children:

        print("Next color is ", -color)
        print("Child = ", child.state.player.name)
        print("Hand in the child : ", child.state.player.hand[0].title)

    for child in node.children:

        # child.value = evaluate(child)

        child.floor = virtualNode.floor + 1

        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))

        child.value = value
        print("child value is", child.value)
        """
        alpha = max(alpha, value)

        if beta <= alpha:
            break
        """

    """
    MINMAX AU CAS OU
    Attention, si on change, réflechir si evaluate est toujours adaptée
    Pensez aux valeurs des noeuds
    
    def minimax(node, depth, alpha, beta, isMax):

        if isTerminal(node) or depth == 0:

            node.value = evaluate(node)
            return color * node.value

        if isMax:
            bestVal = float('-inf')

            for child in node.children:
                value = minimax(node, depth-1, false, alpha, beta)
                bestVal = max( bestVal, value) 
                alpha = max( alpha, bestVal)

                if beta <= alpha:
                    break

            return bestVal
        else:
            bestVal = float('inf')

            for child in node.children:
                value = minimax(node, depth-1, true, alpha, beta)
                bestVal = min( bestVal, value) 
                beta = min( beta, bestVal)

                if beta <= alpha:
                    break

            return bestVal

    L'appel dans player ressemblerait à:

    value = minimax(node, depth, neg_inf, pos_inf, true)    
    """
    return value
