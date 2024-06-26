import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  
from scipy import stats
from networkx.algorithms import bipartite


class Paper_BiTri_functions():
    
        def interaction_number(G):
            # connectance of the network
            num_edges = G.number_of_edges()
            #checked
            print("Number of Total possible interactions(Edges):", num_edges)   
            return num_edges
            
        def size_number_of_nodes(adjacency_matrix, G):    
            row, col = adjacency_matrix.shape
            print("size verified",row*col)
            num_nodes = G.number_of_nodes()
            return num_nodes
        
        def connectance_density(adjacency_matrix, G):
            # Number of nodes
            n = adjacency_matrix.shape[0] 
            # Number of links  
            links = (adjacency_matrix != 0).sum()
            # Possible number of links 
            possible_links = n*(n-1)/2
            # Connectance
            C = links/possible_links
            print("Connectance verified:", C, "\n")#.55 for test
            density = nx.density(G)
            print(f"Network Density: {density}")
            return C, density
        
        def modularity(G):
            mod=nx.community.modularity(G, nx.community.label_propagation_communities(G))
            print('Community Modularity', mod)
            print('verify against MATLAB Code')
            return mod
        
        def z_p_value_perf_nodes(G):
            node_degrees = dict(G.degree())
            # Calculate the mean and standard deviation of node degrees
            degree_values = list(node_degrees.values())
            mean_degree = np.mean(degree_values)
            std_degree = np.std(degree_values)
            # Calculate the z-value and p-value for each node's degree
            z_values = {}
            p_values = {}
            for node, degree in node_degrees.items():
                z = (degree - mean_degree) / std_degree
                p = 1 - stats.norm.cdf(z)  # Calculate the one-tailed p-value
                z_values[node] = z
                p_values[node] = p
            # Define thresholds for categorizing nodes
            ultra_peripheral_threshold = -1.96  # Customize this threshold
            peripheral_threshold = -0.5       # Customize this threshold
            hub_threshold = 0.5               # Customize this threshold
            # Categorize nodes based on z-values
            node_categories = {}
            for node, z in z_values.items():
                if z < ultra_peripheral_threshold:
                    node_categories[node] = "Ultra-Peripheral"
                elif z < peripheral_threshold:
                    node_categories[node] = "Peripheral"
                elif z < hub_threshold:
                    node_categories[node] = "Non-Hub"
                else:
                    node_categories[node] = "Hub"
            print("Node Categories:")
            print(node_categories)
            return node_categories

        def ecological_error_tolerance(graph):
            # Calculate the size of the largest connected component before failure
            largest_cc_before = max(nx.connected_components(graph), key=len)
            largest_cc_size_before = len(largest_cc_before)
            # Remove a random node and calculate the size of the largest connected component
            random_node = list(graph.nodes())[0]  # Change this if you want to select a different random node
            graph.remove_node(random_node)
            largest_cc_after = max(nx.connected_components(graph), key=len)
            largest_cc_size_after = len(largest_cc_after)
            # Calculate ecological error tolerance
            error_tolerance = largest_cc_size_after / largest_cc_size_before
            return error_tolerance
        
        def ecological_attack_tolerance(graph):
            # Calculate the size of the largest connected component before attack
            largest_cc_before = max(nx.connected_components(graph), key=len)
            largest_cc_size_before = len(largest_cc_before)
            # Identify the most central node (highest degree) and remove it
            central_node = max(graph.degree, key=lambda x: x[1])[0]
            graph.remove_node(central_node)
            # Calculate the size of the largest connected component after attack
            largest_cc_after = max(nx.connected_components(graph), key=len)
            largest_cc_size_after = len(largest_cc_after)
            # Calculate ecological attack tolerance
            attack_tolerance = largest_cc_size_after / largest_cc_size_before
            return attack_tolerance
        
        def edge_deletion(G):
            print("here is the edge deletion graph")
            plt.figure()
            x = []
            y = []
            removed_nodes = []

            # Iterate, removing max connected node each time
            while G.number_of_edges() > 0:
                node = max(G.degree(), key=lambda x: x[1])[0]
                removed_nodes.append(node)
                G.remove_node(node)
                x.append(G.number_of_nodes())
                y.append(G.number_of_edges())

            plt.plot(x, y)
            plt.xlabel('Nodes removed')
            plt.ylabel('Total connections')
            plt.title('Connections vs Nodes removed')
            plt.show()
            print("First 20 nodes removed:")
            print(removed_nodes[:20])
            return x,y,removed_nodes
        
        def bi_from_tri(matrix, G):
            for row in matrix:
                source, target = row[:2]  # Get source and target node IDs
                # Optionally, use additional columns as attributes, e.g., weight=row[2]
                G.add_edge(source, target)
            bi = nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
            plt.show()
            return
