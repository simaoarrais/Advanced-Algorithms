from lib2to3.pgen2 import grammar
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from itertools import permutations

class Vertice:
    #Class attributes
    oX = int()
    oY = int()
    w = int()
    label = int()
    
    # Instance attributes
    def __init__(self, oX, oY, w, label):
        self.oX = oX
        self.oY = oY
        self.weight = w
        self.label = label
    
    def __str__(self):
        return f'NODE: {self.label} -> oX: {self.oX}; oY: {self.oY}; w: {self.weight}'

class Edge:
    #Class attributes
    label = 0

    # Instance attributes
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.label += 1

    def __str__(self):
        return f'EDGE: {self.label} -> node1: {self.node1}; node2: {self.node2}'

class Graph:
    #Class attributes
    num_vertices = int()
    num_edges = int()
    seed = int()
    k = float()
    adj = dict()

    # Instance attributes
    def __init__(self, n, m, seed, k):
        self.num_vertices = n
        self.num_edges = m
        self.seed = seed
        self.k = k
    
    #Adds a node to adjacency matrix 
    def add_node(self, n):
        if n not in self.adj:
            self.adj[n] = {}
            return True
        return False
    
    #Adds edges to 2 related nodes
    def add_edge(self, u, v):
        self.adj[u] = v
        self.adj[v] = u

    # def draw(self):
    #     nx.draw(self)
    #     plt.show()
    
    def create_graph(self):
        vertices = set()
        rnd.seed(self.seed)

        #Create nodes loop
        for i in range(self.num_vertices):
            node_coord = (rnd.randint(1, 20), rnd.randint(1, 20))   #node_coord = (x,y)

            #Check if node coordinates already exist
            while(node_coord in vertices):
                node_coord = (rnd.randint(1, 20), rnd.randint(1, 20))

            #Calculate weight and create node
            node_weight = rnd.randint(1, 20)
            node = Vertice(node_coord[0], node_coord[1], node_weight, i+1)

            #Add node to graph and node coords to set of vertices
            vertices.add((node.oX, node.oY))
            self.add_node(node)
            #print(node)
        
        #Calculate number of edges in a complete graph 
        total_edges = (self.num_vertices * (self.num_vertices - 1)) // 2

        
        for node1 in self.adj:
            num_edges = rnd.randint(1, self.num_vertices-1)

            #Randomly choose a node that's not itself
            random_node = rnd.randint(1, self.num_vertices)
            while(random_node == node1.label):
                random_node = rnd.randint(1, self.num_vertices)

            #print(f'{random_node}')

            for node2 in self.adj:
                #print(f'node2: {node2}')
                if random_node == node2.label:
                     #print(f'{random_node} == {node2.label}')
                    break
            

            
        #     self.adj.keys()
        #     if node_label == node.label:
        #         print(node)
        #    self.add_edge(node1, node2)
        # for node in nodes:
        #     print(f'NODE: {node}')
        #     self.add_node(node)
        # self.draw()