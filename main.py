"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph
import solution


def main():
    vertices = 5
    edge_percentage = 0.5
    seed = 85132
    G = Graph(vertices, edge_percentage, seed)

    G.create_graph()
    # G.draw_graph()

    print(f'solution: {[a.label for a in solution.brute_solution(G.adj)]}')
    solution.brute_solution2(G.adj)
    

if __name__ == "__main__":
    main()