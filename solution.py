from graph import Graph
import itertools

def brute_solution(graph_adj):
    # Base Case - Given Graph has no nodes
    if(len(graph_adj) == 0):
        return []
        
    # Base Case - Given Graph has 1
    if(len(graph_adj) == 1):
        return [list(graph_adj.keys())[0]]

    # Select a vertex from the graph
    vCurrent = list(graph_adj.keys())[0]
    # print(f'vCurrent: {vCurrent}')

    # Case 1 - Proceed removing
    # the selected vertex
    # from the Maximal Set
    graph2 = dict(graph_adj)

    # Delete current vertex
    # from the Graph
    del graph2[vCurrent]
    # print(f'graph2: {[a.label for a in graph2]}')

    # Recursive call - Gets
    # Maximal Set,
    # assuming current Vertex
    # not selected
    res1 = brute_solution(graph2)

    # Case 2 - Proceed considering
    # the selected vertex as part
    # of the Maximal Set

    # Loop through its neighbours
    for v in graph_adj.get(vCurrent):

        # print(f'for v: {v} and vCurrent: {vCurrent}')
        
        # Delete neighbor from
        # the current subgraph
        if(v in graph2):
            del graph2[v]
    
    # This result set contains VFirst,
    # and the result of recursive
    # call assuming neighbors of vFirst
    # are not selected
    res2 = [vCurrent] + brute_solution(graph2)
    
    # Our final result is the one
    # which is bigger, return it
    if(len(res1) > len(res2)):
        # print(f'res1: {[a.label for a in res1]}')
        return res1
    # print(f'res2: {[a.label for a in res1]}')
    return res2

def brute_solution2(graph_adj):
    # Base Case - Given Graph has no nodes
    if(len(graph_adj) == 0):
        return []
        
    # Base Case - Given Graph has 1
    if(len(graph_adj) == 1):
        return [list(graph_adj.keys())[0]]

    for i in range(2, len(graph_adj.keys())):
        combinations = itertools.combinations(graph_adj.keys(), i)
        for comb in combinations:
            # print([x.label for x in comb])
            pass
    pass