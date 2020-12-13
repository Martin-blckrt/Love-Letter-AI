from src.AI.NodeToolkit import isTerminal, evaluate, nextStates
import copy


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

        if alpha >= beta:
            break

    return value
