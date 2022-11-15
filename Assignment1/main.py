"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph
import solution
import time
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Program that solves the Independent Set of Size k Problem')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-s', '--seed', metavar='SEED', default=85132, type=int, required=False,
                       help='create a random graph based on a seed (default: %(default)s)')
    parser.add_argument('-v', '--vertices', metavar='VERTICES', default=4, type=int, required=False,
                        help='the number of vertices of the graph (default: %(default)s)')
    parser.add_argument('-e', '--edge', metavar='EDGE DENSITY', default=0.5, type=float, required=False,
                        help='edge density that will be generated (default: %(default)s)')

    args = vars(parser.parse_args())

    vertices = args["vertices"]
    edge_percentage = args["edge"]
    seed = args["seed"]

    G = Graph(vertices, edge_percentage, seed)
    print(f'p = {edge_percentage}')

    #Calculate graph creation time
    st_graph = time.time()
    G.create_graph()
    et_graph = time.time()
    elapsed_time_graph = et_graph - st_graph
    # print(f'graph creation: {elapsed_time_graph}')
    #------------------------------------------------------------
    # Calculate brute force solution time
    st_brute = time.time()
    final_brute = solution.brute_solution(G.adj)
    et_brute = time.time()
    elapsed_time_brute = et_brute - st_brute
    # print(f'brute time: {elapsed_time_brute:.2f}')
    #------------------------------------------------------------
    #Calculate brute greedy solution time
    st_greedy = time.time()
    solution.bfs(G.adj, G.vertices.get(0))
    et_greedy = time.time()
    elapsed_time_greedy = et_greedy - st_greedy
    # print(f'greedy time: {elapsed_time_greedy}')

    G.draw_graph()