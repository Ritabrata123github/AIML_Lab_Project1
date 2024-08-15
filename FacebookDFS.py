import networkx as nx
import matplotlib.pyplot as plt

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

# Iterative DFS to explore connections starting from a given user
def dfs_iterative(G, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in G.neighbors(node) if neighbor not in visited)

    return visited

# Visualize the graph and the DFS visited nodes
def visualize_dfs(G, dfs_visited):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

    if dfs_visited:
        nx.draw_networkx_nodes(G, pos, nodelist=dfs_visited, node_color='green')
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black')

    plt.show()

# Main execution
file_path = "C:\\Users\\RITABRATA JOSH\\Downloads\\facebook_combined.txt"  # Replace with your file path
edges = load_dataset(file_path)
G = create_graph(edges)

start_user = '0'  # Replace with actual user

dfs_visited = dfs_iterative(G, start_user)
visualize_dfs(G, dfs_visited)


