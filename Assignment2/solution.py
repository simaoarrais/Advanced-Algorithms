import random as rnd
import copy
import time

class Solution:

    # Instance attributes
    def __init__(self, adj_matrix, vertices_dict):
        self.adj_matrix = adj_matrix
        self.vertices_dict = vertices_dict

    def solution(self):
        rnd.seed(None)
        tested_candidates = list()

        # Calculate how many vertices the candidate solution will have
        num_vertices_candidate = rnd.randint(2, len(self.vertices_dict.keys())) # candidate solutions must have at least 2 vertices
        print(f"num_vertices_candidate : {num_vertices_candidate}")

        time_loop_duration = 10 # seconds
        time_loop_start = time.time()
        while(time.time() < time_loop_start + time_loop_duration):

            # Calculate what vertices will belong to the candidate solution
            candidate_set = set()
            remaining_vertices = copy.copy(self.vertices_dict)
            for i in range(num_vertices_candidate):

                # Random choice of vertex
                vertice_label = rnd.choice(list(remaining_vertices.keys()))
                vertice = self.vertices_dict.get(vertice_label)

                # Add vertex to candidate solution and delete it for future random choice
                candidate_set.add(vertice)
                del remaining_vertices[vertice_label]

            # Add candidate solution to tested solutions list
            tested_candidates.append(tested_candidates)

            print(f"candidate -> {[v.label for v in candidate_set]}")
            print(self.is_independent_set(candidate_set))
            if self.is_independent_set(candidate_set):
                break

            pass

    # Check if the candidate set is an independent set
    def is_independent_set(self, candidate_set):

        # For each node in the candidate solution
        for node in candidate_set:
            node_neighbours = self.adj_matrix.get(node)
            
            # Check if the neighbours to that node are in the candidate solution
            if len(self.similarity(node_neighbours, candidate_set)) != 0:
                return False
        return True
    

    # Return list with similarity between 2 structures
    def similarity(self, structure1, structure2):
        return [x for x in structure1 if x in structure2]