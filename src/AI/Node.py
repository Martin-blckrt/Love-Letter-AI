def getPathFrom(node):

    thePath = [node]

    while node.parent:
        node = node.parent
        thePath.insert(0, node)

    return thePath


def dfs(startingNode, negaValue, occurence_test=True):

    openList = [startingNode]
    closedList = []

    n = 0
    while openList:
        begNode = openList.pop(0)

        if begNode.value == negaValue and begNode is not startingNode:
            break
        else:
            next_nodes = begNode.children

            for elem in next_nodes:
                if not occurence_test or elem not in closedList:
                    n += 1
                    openList.insert(0, elem)
                    if occurence_test:
                        closedList.append(elem)

    for node in closedList:
        if node.value == negaValue:
            return node


class State:
    def __init__(self, deck, isolatedCards, listOfCards, player):
        self.deck = deck
        self.isolatedCards = isolatedCards
        self.listOfCards = listOfCards
        self.player = player


class Node:
    def __init__(self, state, value, parent, floor):
        self.state = state
        self.value = value
        self.parent = parent
        self.children = []
        self.floor = floor
