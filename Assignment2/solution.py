import graph as Graph
import math
import time
import random as rnd


class Solution:

    # Instance attributes
    def __init__(self, graph: Graph, outer_loop_time):
        self.adj_matrix = graph.adj
        self.vertices_dict = graph.vertices_dict
        self.num_vertices = graph.num_vertices
        self.outer_loop_time = outer_loop_time
        self.basic_operations = 0

    def solution(self):
        # rnd.seed(None)
        best_solution = set()
        tested_candidates = list()
        generated_solutions = 0

        # ------------------------ For each number of vertices ----------------------- #
        n = 1
        outer_loop_st = time.time()
        while (n < self.num_vertices + 1 and self.outer_loop_time > time.time() - outer_loop_st):
            self.basic_operations += 2
            # ------------ If the candidate solution will contain all vertices ----------- #
            self.basic_operations += 1
            if n == self.num_vertices:
                # print(f'all: {[v.label for v in self.adj_matrix.keys()]} -> {self.is_independent_set(self.adj_matrix.keys())}')
                if self.is_independent_set(self.adj_matrix.keys()):
                    best_solution = set(self.adj_matrix.keys())
                tested_candidates.append(self.adj_matrix.keys())
                self.basic_operations += 2
                n += 1
                break

            comb = self.calculate_combinations(n)
            inner_limit = comb * (1/math.log10(comb))
            self.basic_operations += 1
            # print(f'combination: {comb} -> {n} v -> inner: {inner_limit}')
            # ---------------------- For the amount of combinations ---------------------- #
            i = 0
            while (i < comb and i < inner_limit):
                self.basic_operations += 2
                # ------------------ Calculate a random candidate of size n ------------------ #
                candidate_set = self.get_candidate_set(n)
                generated_solutions += 1
                while (candidate_set in tested_candidates):
                    self.basic_operations += 1
                    if (self.outer_loop_time < time.time() - outer_loop_st):
                        self.basic_operations += 1
                        return best_solution, generated_solutions, len(tested_candidates), n-1
                    else:
                        candidate_set = self.get_candidate_set(n)
                        generated_solutions += 1

                # --------------- Check if candidate set is an independent set --------------- #
                # print([v.label for v in candidate_set])
                tested_candidates.append(candidate_set)
                if self.is_independent_set(candidate_set):
                    best_solution = candidate_set
                    break

                i += 1
                self.basic_operations += 1
            n += 1
            self.basic_operations += 1
        # print(f'best: {[v.label for v in best_solution]}')
        return best_solution, generated_solutions, len(tested_candidates), n-1


    def is_independent_set(self, candidate_set):
        '''Check if the candidate set is an independent set'''

        # For each node in the candidate solution
        for node in candidate_set:
            self.basic_operations += 1
            node_neighbours = self.adj_matrix.get(node)
            
            # Check if the neighbours to that node are in the candidate solution
            self.basic_operations += 1
            if len(self.similarity(node_neighbours, candidate_set)) != 0:
                return False
        return True
    

    def get_candidate_set(self, num_vertices_candidate):
        candidate_set = set(rnd.sample(list(self.adj_matrix.keys()), k = num_vertices_candidate))
        self.basic_operations += 1
        return candidate_set


    def similarity(self, structure1, structure2):
        '''Return list with similarity between 2 structures'''
        self.basic_operations += 1
        return [x for x in structure1 if x in structure2]


    def calculate_combinations(self, r):
        '''Calculates the combination value of nCr'''
        self.basic_operations += 1
        return math.comb(self.num_vertices, r)
