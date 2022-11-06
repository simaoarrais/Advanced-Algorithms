from graph import Graph
import itertools
import copy

def brute_solution(graph_adj):
    # Base Case - Given Graph has no nodes
    if(len(graph_adj) == 0):
        return []
        
    # Base Case - Given Graph has 1
    if(len(graph_adj) == 1):
        return [list(graph_adj.keys())[0]]

    final_result = list()
    for i in range(2, len(graph_adj.keys())):
        combinations = list(itertools.combinations(graph_adj.keys(), i))

        tmp_result = copy.copy(combinations)

        # For every combination tuple
        for comb in combinations:
            print([x.label for x in comb])
            
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
    
    # for res in final_result:
    #     for a in res:
    #         print([x.label for x in a])

# def bfs(visited, graph_adj):
#     queue = []     #Initialize a queue
#     visited.append(node)
#     queue.append(node)

#     while queue:          # Creating loop to visit each node
#         m = queue.pop(0) 
#         print (m, end = " ") 

#         for neighbour in graph_adj[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)