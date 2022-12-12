"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
import argparse
import time

from graph import Graph
from solution import Solution

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Program that solves the Independent Set of Size k Problem')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-s', '--seed', metavar='SEED', default=85132, type=int, required=False,
                       help='create a random graph based on a seed (default: %(default)s)')
    parser.add_argument('-v', '--vertices', metavar='VERTICES', default=5, type=int, required=False,
                        help='the number of Graphs it will create (default: %(default)s)')
    parser.add_argument('-e', '--edge', metavar='EDGE DENSITY', default=0.5, type=float, required=False,
                        help='edge density that will be generated (default: %(default)s)')
    parser.add_argument('-l', '--loop_limit', metavar='RUNNING TIME', default=60, type=float, required=False,
                        help='elapsed time until the algorithm stops searching solutions (default: %(default)s)')

    args = vars(parser.parse_args())

    vertices = args["vertices"]
    edge_percentage = args["edge"]
    seed = args["seed"]
    loop_limit = args["loop_limit"]

    for i in range(20, vertices+1):
        G = Graph(i, edge_percentage, seed)
        # print(f'vertices = {vertices}, p = {edge_percentage}, seed = {seed}')
        print(f'vertices = {i}')
        #Calculate graph creation time
        st_graph = time.time()
        G.create_graph()
        et_graph = time.time()
        elapsed_time_graph = et_graph - st_graph
        print(f'graph creation: {format(elapsed_time_graph, ".2e")}')
        #------------------------------------------------------------
        # Solution
        st_solution = time.time()
        solution = Solution(G, loop_limit)
        best_solution, num_generated_solutions, num_tested_candidates, len_last_tested = solution.solution()
        et_solution = time.time()
        # print(f'best: {best_solution} -> {len(best_solution)}')
        # print(f'generated_solutions: {num_generated_solutions}')
        # print(f'tested_candidates: {num_tested_candidates}')
        # print(f'basic_operations: {solution.basic_operations}')
        # print(f'len_last_solution: {len_last_tested}')
        elapsed_time_solution = et_solution - st_solution
        print(f'solution time: {format(elapsed_time_solution, ".2e")}')

        # G.draw_graph()