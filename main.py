"""
Created by: Simão Teles Arrais - 85132

Main python code for the AA class assigment_1.

The code was tested on python version 3.8.10.
"""
from graph import Graph


def main():
    vertices = 4
    edges = 10
    seed = 85132
    k = 1
    G = Graph(vertices,edges,seed, k)
    G.create_graph()
    pass

if __name__ == "__main__":
    main()