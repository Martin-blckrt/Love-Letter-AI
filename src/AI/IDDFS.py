from src.AI.Node import Node
# TODO. adapter l'algo pour l'integrer à l'IA


def IDDFS(problem, initial_state, final_state, maxDepth):

    for depth in range(0, maxDepth):
        DFS(problem, initial_state, final_state, depth)


def DFS(problem, initial_state, final_state, depth):
    #TODO: La déclaration est imcomplète, si c'est le noeud parent, rajoutez 'None'
    #TODO: faire next states
    orderedList = [Node(initial_state, None)]
    checkedStatesList = []

    while orderedList:

        e = orderedList.pop(0)
        if e.state == final_state:
            print(f"Final node state is : {e.state}\n its value is : {e.value} \n")
            break

        elif depth >= 0:

            next_states = problem.nextStates(e.state)

            for s in next_states:
                if s not in checkedStatesList:
                    node = Node(s, e)
                    orderedList.insert(0, node)
                    checkedStatesList.append(s)
