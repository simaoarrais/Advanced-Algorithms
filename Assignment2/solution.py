import random as rnd
import graph

class Solution:

    # Instance attributes
    def __init__(self, adj_matrix, vertices_dict):
        self.adj_matrix = adj_matrix
        self.vertices_dict = vertices_dict

    def solution(self):
        rnd.seed(None)
        tested_candidates = list()
        num_vertices_candidate = rnd.randint(2, len(self.vertices_dict.keys())) # candidate solutions must have at least 2 vertices
        print(f"num_vertices_candidate : {num_vertices_candidate}")

        candidate_set = set()
        for i in range(num_vertices_candidate):
            vertice_label = rnd.randint(0, len(self.vertices_dict.keys())-1)
            vertice = self.vertices_dict.get(vertice_label)

            while (vertice in candidate_set):
                vertice_label = rnd.randint(0, len(self.vertices_dict.keys())-1)
                vertice = self.vertices_dict.get(vertice_label)

            candidate_set.add(vertice)

        print(f"candidate -> {[v.label for v in candidate_set]}")
        print(self.is_independent_set(candidate_set))

    # Check if the candidate set is an independent set
    def is_independent_set(self, candidate_set):
        for node in candidate_set:
            node_neighbours = self.adj_matrix.get(node)
            if len(self.similarity(node_neighbours, candidate_set)) != 0:
                return False
        return True
    
    # Return list with similarity between 2 structures
    def similarity(self, structure1, structure2):
        return [x for x in structure1 if x in structure2]