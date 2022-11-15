"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph
import solution
import time
import argparse
import matplotlib.pyplot as plt


if __name__ == "__main__":

    vertices = 4
    edge_percentage = 0.5
    seed = 85132
    G = Graph(vertices, edge_percentage, seed)
    print(f'p = {edge_percentage}')

    #Calculate graph creation time
    st_graph = time.time()
    G.create_graph()
    et_graph = time.time()
    elapsed_time_graph = et_graph - st_graph
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