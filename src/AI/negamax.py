import copy
from src.AI.NodeToolkit import isTerminal, evaluate, nextStates


def negamax(node, depth, alpha, beta, color):
    virtualNode = copy.deepcopy(node)

    # TODO. Fix color, switch des joueurs, generation des enfants, attribution des valeurs des noeuds

    if isTerminal(node) or depth == 0:

        node.value = evaluate(node)

        return color * node.value

    if color == 1:
        targetPlayer = virtualNode.state.player
        print(targetPlayer.name, "is playing")
    else:
        targetPlayer = virtualNode.state.opponent
        print(targetPlayer.name, "is playing")

    print("Current player is", targetPlayer.name)

    nextChildren = nextStates(virtualNode, targetPlayer)
    node.children = copy.deepcopy(nextChildren)

    print(f"Next state over and i have {len(node.children)} babies")

    value = float('-inf')

    for child in node.children:

        print("Next color is ", -color)
        value = max(value, -negamax(child, depth - 1, -beta, -alpha, -color))
        alpha = max(alpha, value)

        if beta <= alpha:
            break

    """
    MINMAX AU CAS OU
    Attention, si on change, réflechir si evaluate est toujours adaptée
    
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
