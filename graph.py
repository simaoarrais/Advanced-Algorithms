from lib2to3.pgen2 import grammar
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math

class Vertice:
    # Class attributes
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
        return f'{self.label}'
        #return f'NODE: {self.label} -> oX: {self.oX}; oY: {self.oY}; w: {self.weight}'

class Edge:
    # Class attributes
    label = 0

    # Instance attributes
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.label += 1

    def __str__(self):
        return f'EDGE: {self.label} -> node1: {self.node1}; node2: {self.node2}'

class Graph:
    # Class attributes
    num_vertices = int()
    seed = int()
    k = float()
    adj = dict()
    vertices = dict()

    # Instance attributes
    def __init__(self, num_vertices, edge_percentage, seed, k):
        self.num_vertices = num_vertices
        self.edge_percentage = edge_percentage
        self.seed = seed
        self.k = k

    # Adds a node to adjacency matrix
    def add_node_to_matrix(self, u):
        if u not in self.adj:
            self.adj[u] = {}
            return True
        return False

    # Adds edges to 2 related nodes
    def add_edge_to_matrix(self, u, v):
        self.adj.get(u).add(v)
        self.adj.get(v).add(u)

        #print 
        print(f'adj matrix->')
        for i in self.adj:
            nodes = set()
            for n in self.adj.get(i):
                nodes.add(n.label)
            print(f'{i}: {nodes}')
    
    # Calculates Euclidean Distance between 2 coordinates
    def close_check(self, u, v):
        euclidean_distance = math.sqrt((u[0] + v[0])**2 + (u[1] + v[1])**2)
        if euclidean_distance < 2:
            return True
        return False

    def create_graph(self):
        rnd.seed(self.seed)

        # Create number of nodes loop
        for i in range(self.num_vertices):
            node_coord = (rnd.randint(1, 100), rnd.randint(1, 100))   # node_coord = (x,y)

            # Check if node coordinates match or is too close, if so calculates new coordinates
            for node in self.adj:
                if self.close_check((node.oX, node.oY), node_coord):
                    node_coord = (rnd.randint(1, 100), rnd.randint(1, 100))

            # Calculate weight and create node
            node_weight = rnd.randint(1, 100)
            node = Vertice(node_coord[0], node_coord[1], node_weight, i)

            # Add node to dictionary of vertices and also add node to graph and assign it an empty set
            self.vertices[i] = node
            self.add_node_to_matrix(node)
            self.adj[node] = set()
            
        #print
        print(f'adj matrix ->')
        for i in self.adj:
            print(f'{i}: {self.adj.get(i)}')
        
        #print
        print(f'vertices dic ->')
        for i in self.vertices:
            print(f'{i}: {self.vertices.get(i)}')
        
        # Calculate number of edges in a complete graph
        total_edges = (self.num_vertices * (self.num_vertices - 1)) // 2
        print(f'\nComplete graph edges: {total_edges}')

        # Calculate how many edges the graph will have and ensure at least 1 edge
        num_edges_graph = math.floor(total_edges * self.edge_percentage)
        if num_edges_graph == 0:
            num_edges_graph = math.ceil(total_edges * self.edge_percentage)
        print(f'Number of edges will exist: {num_edges_graph}\n')


        # # While the graph still has edges to be
        while(num_edges_graph > 0):
            vertices_done = set()
            # For the number of edges it will exist
            for i in range(num_edges_graph):
                print(f'edge number: {i}')
                node1 = rnd.randint(0, self.num_vertices-1)
                
                while(node1 in vertices_done):
                    node1 = rnd.randint(0, self.num_vertices-1)
                vertices_done.add(node1)
                node1 = self.vertices.get(node1)
                print(f'node1: {node1}')

                # If total edge number is lesser than maximum edges it can be in a node
                if num_edges_graph < self.num_vertices-1:
                    node_edges = rnd.randint(0, num_edges_graph)
                else:
                    node_edges = rnd.randint(0, self.num_vertices-1)
                print(f'number of edges: {node_edges}')

                node_edges_set = set()
                # If node1 will contain edges
                if node_edges != 0:
                    # For the number of edges it will contain, calculate node2
                    for i in range(node_edges):
                        node2 = rnd.randint(0, self.num_vertices-1) # num_vertices-1 cause first node is node 0
                        
                        # Node2 can't be the same as Node1
                        print(f'node2 before: {node2}')
                        while (node2 == node1.label or self.vertices.get(node2) in self.adj.get(node1)):
                            print(f'{node2 == node1.label}, {node2 in node_edges_set}')
                            node2 = rnd.randint(0, self.num_vertices-1)
                            print(f'node2: {node2}')
                        node2 = self.vertices.get(node2)
                        node_edges_set.add(node2)

                        #Add edge between the 2 nodes
                        self.add_edge_to_matrix(node1, node2)
                
                num_edges_graph -= node_edges
                print(f'num_edges_graph: {num_edges_graph}')

                print("-----------------------")

        #----------------------------------------------------------------

        # # For all nodes
        # for i in self.vertices:
        #     node1 = self.vertices.get(i)
        #     print(f'node1: {node1}')
            
        #     # If graph edges is greater than the number of vertices
        #     node_edges = rnd.randint(0, self.num_vertices-1)    #self.num_vertices-1 não pode ser ele mesmo
        #     if num_edges_graph > self.num_vertices-1:
        #         node_edges = rnd.randint(0, self.num_vertices-1)
        #     else:
        #         node_edges = rnd.randint(0, num_edges_graph)
        #     num_edges_graph -= node_edges
        #     node_edges = num_edges_graph
        #     print(f'number of edges: {node_edges}')

        #     # If it will contain edges
        #     node_edges_set = set()
        #     if node_edges != 0:
        #         # For the number of edges it will contain, calculate random node and add edge accordingly
        #         for i in range(node_edges):
        #             node2 = rnd.randint(0, self.num_vertices-1) # num_vertices-1 pois o nr começa no 0
        #             # The random node generated can't be it's own or already in the set
        #             while (node2 == node1.label or node2 in node_edges_set):
        #                 node2 = rnd.randint(0, self.num_vertices-1)
        #             node2 = self.vertices.get(node2)
        #             print(f'node2: {node2}')
        #             node_edges_set.add(node2)
        #             self.add_edge_to_matrix(node1, node2)
            
        #     print("-----------------------")

        #print 
        print(f'\nadj matrix after->')
        for i in self.adj:
            nodes = set()
            for n in self.adj.get(i):
                nodes.add(n.label)
            print(f'{i}: {nodes}')