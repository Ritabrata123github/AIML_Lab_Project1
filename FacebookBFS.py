import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Load the dataset from a txt file
def load_dataset(file_path):
    edges = []
    with open(file_path, 'r') as f:
        for line in f:
            user1, user2 = line.strip().split()
            edges.append((user1, user2))
    return edges

# Create a graph using NetworkX
def create_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# BFS to find the shortest path between two users
def bfs_shortest_path(G, start_node, target_node):
    visited = set()
    queue = deque([[start_node]])

    if start_node == target_node:
        return [start_node]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = G.neighbors(node)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == target_node:
                    return new_path
            
            visited.add(node)

    return None  # If no path is found

# Visualize the graph and the BFS path
def visualize_bfs(G, bfs_path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

    if bfs_path:
        path_edges = list(zip(bfs_path, bfs_path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=bfs_path, node_color='orange')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2)

    plt.show()

# Main execution
file_path = "C:\\Users\\RITABRATA JOSH\\Downloads\\facebook_combined.txt"# Replace with your file path
edges = load_dataset(file_path)
G = create_graph(edges)

start_user = '0'  # Replace with actual user
target_user = '100'  # Replace with actual user

bfs_path = bfs_shortest_path(G, start_user, target_user)
visualize_bfs(G, bfs_path)
