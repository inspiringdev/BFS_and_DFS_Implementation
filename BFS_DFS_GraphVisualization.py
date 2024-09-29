#Name: Ubaid ur Rehman
#CMS: 470984

import queue
import networkx as nx
import matplotlib.pyplot as plt


# BFS Order Function
def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph.neighbors(vertex):
                if node not in visited:
                    q.put(node)

    return order


# DFS Order Function
def order_dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph.neighbors(start_node):
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))

    return order


# Visualization Function
def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    visited_set = set()  # To track visited nodes for visualization

    for i, node in enumerate(order):
        plt.clf()
        plt.title(title)
        # Mark the current node as visited
        visited_set.add(node)

        # Draw the graph
        node_colors = ['g' if n in visited_set else 'r'
        if n == node else 'b' for n in G.nodes]

        # Draw nodes with colors based on visitation
        nx.draw(G, pos, with_labels=True, node_color=node_colors)

        # Annotate the current order
        plt.text(0.5, 1.1, f'Visiting: {node}',
        fontsize=12, ha='center', transform=plt.gca().transAxes)
        plt.text(0.5, 0.02, f'Order: {order}',
        fontsize=12, ha='center', transform=plt.gca().transAxes)

        plt.draw()
        plt.pause(0.5)  # Pause to visualize the step

    plt.show()


# Create the graph
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                  ('B', 'E'), ('C', 'F'), ('C', 'G')])

# Generate positions for nodes
pos = nx.spring_layout(G)

# Visualize BFS
bfs_order = order_bfs(G, start_node='A')
print(f"BFS Order: {bfs_order}")  # Print the BFS order at the end
visualize_search(bfs_order, title='BFS Visualization', G=G, pos=pos)

# Visualize DFS
dfs_order = order_dfs(G, start_node='A')
print(f"DFS Order: {dfs_order}")  # Print the DFS order at the end
visualize_search(dfs_order, title='DFS Visualization', G=G, pos=pos)
