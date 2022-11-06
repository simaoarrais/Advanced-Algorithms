"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph
import solution


def main():
    vertices = 6
    edge_percentage = 0.125
    seed = 85132
    G = Graph(vertices, edge_percentage, seed)

    G.create_graph()
    solution.brute_solution(G.adj)
    # solution.bfs([], G.adj)
    #G.draw_graph()
    

if __name__ == "__main__":
    main()