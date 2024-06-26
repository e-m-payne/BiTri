import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  
from scipy import stats
from networkx.algorithms import bipartite


class Generate_graph():

        def Graph(num_herbivores, num_plants, num_carnivores, herbivore_plant_matrix, carnivore_herbivore_matrix, scenario,
              names_h_phy_cps, names_c_cyb_cps, names_relays_cps):
            # Create a new graph
            G = nx.Graph()
            # Create dictionaries to store node types and positions
            node_types = {}
            pos = {}

            # Add herbivore nodes CPS nodes = Relay nodes
            herbivore_nodes = [str(i) for i in names_relays_cps]
            G.add_nodes_from(herbivore_nodes, bipartite=0)
            node_types.update({node: "herbivore" for node in herbivore_nodes})
            
            # Add plant nodes Physical nodes = B, G, L
            plant_nodes = [str(i) for i in names_h_phy_cps]
            G.add_nodes_from(plant_nodes, bipartite=1)
            node_types.update({node: "plant" for node in plant_nodes})
            
            # Add carnivore nodes Cyber nodes = Sub, CC, r
            carnivore_nodes = [str(i) for i in names_c_cyb_cps]
            G.add_nodes_from(carnivore_nodes, bipartite=2)
            node_types.update({node: "carnivore" for node in carnivore_nodes})

            # Add edges and weights to the graph for herbivores and plants
            for i in range(num_herbivores):
                for j in range(num_plants):
                    weight = herbivore_plant_matrix[i, j]
                    if weight > 0:
                        G.add_edge(herbivore_nodes[i], plant_nodes[j], weight=weight)
            
            # Add edges and weights to the graph for carnivores and herbivores
            for i in range(num_carnivores):
                for j in range(num_herbivores):
                    weight = carnivore_herbivore_matrix[i, j]
                    if weight > 0:
                        G.add_edge(carnivore_nodes[i], herbivore_nodes[j], weight=weight)
            
            # Create a layout manually separating the types
            for node_type in set(node_types.values()):
                sub_nodes = [node for node, n_type in node_types.items() if n_type == node_type]
                if node_type == 'herbivore':
                    x = 0.5  # Position herbivores exactly in the middle of the x-axis
                elif node_type == 'plant':
                    x = 0.2  # Position plants to the left
                else:
                    x = 0.8  # Position carnivores to the right
                pos.update({node: (x, i) for i, node in enumerate(sub_nodes)})

            # Define node colors
            node_colors = {
                "herbivore": "lightblue",
                "plant": "lightgreen",
                "carnivore": "lightcoral",
            }
            # Define edge color (you can customize the color as needed)
            edge_color = 'grey'
            # Increase edge width for better visibility
            edge_width = 2.0 
            # Plot the tripartite graph with thicker and more visible lines
            plt.figure(figsize=(12, 6))
            nx.draw_networkx(
                G, pos, with_labels=True, node_size=500, font_size=10, font_color='black', font_weight='bold',
                node_color=[node_colors[node_types[node]] for node in G.nodes], edge_color=edge_color,
                width=edge_width  # Adjust the edge width here
            )
            plt.axis('off')
            plt.show()

            return G
        
        def send_adjacency_to_excel(G, scenario):
            # make an adjacency matrix of the graph G?
            adjacency_matrix = nx.adjacency_matrix(G)
            # Convert the sparse matrix to a dense NumPy array
            adjacency_matrix_array = adjacency_matrix.toarray()
            # Create a pandas DataFrame from the array
            df_adjacency = pd.DataFrame(adjacency_matrix_array)
            # Save the DataFrame to an Excel file
            excel_filename = f"testfile_adjacency_matrix{scenario}.xlsx"
            df_adjacency.to_excel(excel_filename, index=False)
            print(f"Adjacency matrix saved to {excel_filename}. This is important for running the matlab code for the other parts.")
            return adjacency_matrix