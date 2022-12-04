import math
import random as rnd
import graph as Graph

class Solution:

    # Instance attributes
    def __init__(self, graph: Graph):
        self.adj_matrix = graph.adj
        self.vertices_dict = graph.vertices_dict
        self.num_vertices = graph.num_vertices

    def solution(self):
        rnd.seed(None)
        best_solution = set()
        tested_candidates = list()
        # ------------------------ For each number of vertices ----------------------- #
        for n in range(1, self.num_vertices + 1):

            # ------------ If the candidate solution will contain all vertices ----------- #
            if n == self.num_vertices:
                print(f'all: {[v.label for v in self.adj_matrix.keys()]} -> {self.is_independent_set(self.adj_matrix.keys())}')
                if self.is_independent_set(self.adj_matrix.keys()):
                    best_solution = set(self.adj_matrix.keys())
                break

            comb = self.calculate_combinations(n)
            print(f'combination: {comb}')
            # ---------------------- For the amount of combinations ---------------------- #
            for i in range(comb):

                # ------------------ Calculate a random candidate of size n ------------------ #
                candidate_set = self.get_candidate_set(n)
                while (candidate_set in tested_candidates):
                    candidate_set = self.get_candidate_set(n)

                # --------------- Check if candidate set is an independent set --------------- #
                print([v.label for v in candidate_set])
                tested_candidates.append(candidate_set)
                if self.is_independent_set(candidate_set):
                    best_solution = candidate_set
                    break
                
        print(f'best: {[v.label for v in best_solution]}')


    def is_independent_set(self, candidate_set):
        '''Check if the candidate set is an independent set'''

        # For each node in the candidate solution
        for node in candidate_set:
            node_neighbours = self.adj_matrix.get(node)
            
            # Check if the neighbours to that node are in the candidate solution
            if len(self.similarity(node_neighbours, candidate_set)) != 0:
                return False
        return True
    

    def get_candidate_set(self, num_vertices_candidate):
        candidate_set = set(rnd.sample(list(self.adj_matrix.keys()), k = num_vertices_candidate))
        return candidate_set


    def similarity(self, structure1, structure2):
        '''Return list with similarity between 2 structures'''
        return [x for x in structure1 if x in structure2]


    def calculate_combinations(self, r):
        '''Calculates the combination value of nCr'''
        return math.comb(self.num_vertices, r)
