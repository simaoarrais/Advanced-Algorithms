"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph


def main():
    vertices = 5
    edge_percentage = 0.5
    seed = 85132
    k = 1
    G = Graph(vertices, edge_percentage, seed, k)
    G.create_graph()
    G.draw_graph()
    pass

if __name__ == "__main__":
    main()