import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
import math

class Vertice:

    # Instance attributes
    def __init__(self, oX, oY, w, label):
        self.oX = oX
        self.oY = oY
        self.weight = w
        self.label = label
        self.edge_num = int()

    def __str__(self):
        return f'{self.label}'
        #return f'NODE: {self.label} -> oX: {self.oX}; oY: {self.oY}; w: {self.weight}'

class Graph:
    
    # Instance attributes
    def __init__(self, num_vertices, edge_percentage, seed):
        self.num_vertices = num_vertices
        self.edge_percentage = edge_percentage
        self.seed = seed
        self.vertices_dict = dict()
        self.adj = dict()
        self.edges = set()

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
        self.edges.add((u, v))
        u.edge_num += 1
        v.edge_num += 1
    
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
            
            # Check if node coordinates match or is too close, if so calculates new coordinates
            node_coord = (rnd.randint(1, 100), rnd.randint(1, 100))
            for node in self.adj:
                if self.close_check((node.oX, node.oY), node_coord):
                    node_coord = (rnd.randint(1, 100), rnd.randint(1, 100))

            # Calculate weight and create node
            node_weight = rnd.randint(1, 100)
            node = Vertice(node_coord[0], node_coord[1], node_weight, i)

            # Add node to dictionary of vertices and also add node to graph and assign it an empty set
            self.vertices_dict[i] = node
            self.add_node_to_matrix(node)
            self.adj[node] = set()
        
        # Calculate number of edges in a complete graph
        total_edges = (self.num_vertices * (self.num_vertices - 1)) // 2
        # print(f'\nComplete graph edges: {total_edges}')

        # Calculate how many edges the graph will have
        num_edges_graph = math.floor(total_edges * self.edge_percentage)
        # print(f'Number of edges will exist: {num_edges_graph}\n')

        #----------------------------------------------------------------
        # While there are edges left to be given
        while(num_edges_graph > 0):

            node1 = rnd.randint(0, self.num_vertices-1)
            node1 = self.vertices_dict.get(node1)
            # print(f'node1: {node1}')

            # Check if node1 already has the maximum amount of edges
            node1_edge_set_len = len(self.adj.get(node1)) 
            node1_num_edges_available = self.num_vertices-1 - node1_edge_set_len
            # print(f'edges available: {node1_num_edges_available}')

            # If node1 can be given edges
            if node1_num_edges_available != 0:

                # Get number of edges node1 will have
                if node1_num_edges_available < num_edges_graph:
                    node_edges = rnd.randint(0, node1_num_edges_available)
                else:
                    node_edges = rnd.randint(0, num_edges_graph)
                num_edges_graph -= node_edges
                # print(f'number of edges: {node_edges}')
                
                # While there are edges to be given to the node
                while(node_edges > 0):

                    # If node2 is already in node1 set calculate another node2
                    node2 = rnd.randint(0, self.num_vertices-1)
                    while(node1.label == node2 or node2 in [a.label for a in self.adj.get(node1)]):
                        node2 = rnd.randint(0, self.num_vertices-1)
                    
                    # Add edge to adjacency matrix
                    node2 = self.vertices_dict.get(node2)
                    # print(f'node2: {node2}')
                    self.add_edge_to_matrix(node1, node2)
                    node_edges -= 1
            else:
                # print("Node has maximum number of edges")
                pass
            # print("-----------------------")

        # #print 
        # print(f'final adj matrix->')
        # for i in self.adj:
        #     nodes = set()
        #     for n in self.adj.get(i):
        #         nodes.add(n.label)
        #     print(f'{i}: {nodes}')
        # print("-----------------------")

    def draw_graph(self):
        pos = dict()
        G = nx.Graph()

        # Add nodes to networkx graph
        G.add_nodes_from(self.vertices_dict.keys())

        # Create a position dictionary
        for node in self.vertices_dict:
            node = self.vertices_dict.get(node)
            pos[node.label] = (node.oX, node.oY)

        # Add edges to networkx graph
        for node1 in self.adj:
            for node2 in self.adj.get(node1):
                G.add_edge(node1.label, node2.label)

        nx.draw(G, pos=pos, with_labels=True)
        plt.show()