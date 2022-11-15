import graph
import itertools
import copy
import random as rnd

def brute_solution(graph_adj):
    # Base Case - Given Graph has no nodes
    if(len(graph_adj) == 0):
        return []
        
    # Base Case - Given Graph has 1
    if(len(graph_adj) == 1):
        return [list(graph_adj.keys())[0]]

    # For Graphs with 2 or more node

    final_result = list()
    for i in range(2, len(graph_adj.keys())+1):
        combinations = list(itertools.combinations(graph_adj.keys(), i))
        tmp_result = copy.copy(combinations)

        # For every combination tuple
        for comb in combinations:
            # print([x.label for x in comb])
            
            # For node pair
            for j in range(len(comb)-1):
                node1 = comb[j]
                for k in range(j+1, len(comb)):
                    node2 = comb[k]

                    # If exists an edge between them
                    if node2 in graph_adj.get(node1):
                        if comb in tmp_result:
                            tmp_result.remove(comb)
                        break

        final_result.append(tmp_result)
    
    # Get number of solutions
    # counter = 0
    for res in final_result:
        for a in res:
            pass
            # counter += 1
            # print([x.label for x in a])
    print(f'exhaustive: {[x.label for x in a]}')
    # print(f'nr solutions -> {counter}')

    return final_result

def bfs(graph_adj, v):
    visited = []
    queue = []     #Initialize a queue
    visited.append(v)
    queue.append(v)
    solution = set()
    counter = 0

    while queue:
        node = queue.pop(0)

        # If vertice has maximum number of edges, choose the best neighbour
        if len(graph_adj.get(node)) == len(graph_adj.keys())-1:
            node = heuristic(list(graph_adj.get(node)))[0]
        # print(f'cNode: {node}')

        # Get neighbours of current vertice
        neighbours = graph_adj.get(node)

        # Get all the vertices that are not adjacent to current one
        not_neighbours = difference(graph_adj.keys(), neighbours)
        # Remove itself
        not_neighbours.remove(node)

        # Apply heuristic by sort a list of the not adjacent vertices by number of edges ascending
        not_neighbours_sorted = heuristic(not_neighbours)
        # print(f'not adjacent: {[v.label for v in not_neighbours_sorted]}')

        for vertice in not_neighbours_sorted:
            if vertice not in visited:
                # print(f'edge_node: {vertice}')
                visited.append(vertice)
                queue.append(vertice)
                
                # Check similarity between vertice and other not_neighbours
                common_neighbours = similarity(graph_adj.get(vertice), not_neighbours_sorted)
                # print([v.label for v in common_neighbours])
                if len(common_neighbours) == 0:
                    solution.add(vertice)
                    solution.add(node)
                    counter += 1

                elif len(common_neighbours) == 1 and vertice not in solution:
                    solution.add(common_neighbours[0])
                    counter += 1
            
        # print(f'visited: {[v.label for v in visited]}')
        # print("----------------------")
    print(f'solution greedy: {[v.label for v in solution]}')
    # print(f'counter greedy: {counter}')
    pass

# Get list sorted by number of edges
def heuristic(queue):
    return [v for v in sorted(queue, key=lambda x: x.edge_num)]

# Return list with difference between 2 lists
def difference(list1, list2):
    s = set(list2)
    return [x for x in list1 if x not in s]

# Return list with similarity between 2 lists
def similarity(list1, list2):
    s = set(list2)
    return [x for x in list1 if x in s]