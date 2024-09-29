from collections import deque

# BFS Algorithm
def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Queue for BFS
    bfs_order = []

    while queue:
        node = queue.popleft()  # Get the first element
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

# DFS Algorithm (iterative approach)
def dfs(graph, start):
    visited = set()  # To track visited nodes
    stack = [start]  # Stack for DFS
    dfs_order = []

    while stack:
        node = stack.pop()  # Get the last element (LIFO)
        if node not in visited:
            visited.add(node)
            dfs_order.append(node)

            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):  # Reverse for correct order
                if neighbor not in visited:
                    stack.append(neighbor)
        else:
            # Indicate backtracking by adding the node again when returning
            dfs_order.append(node)

    return dfs_order

# Function to input a graph and perform BFS and DFS
def main():
    # Example adjacency list representation of a graph
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': [],
    }

    start_node = input("Enter the start node: ").strip()

    # Perform BFS and DFS
    bfs_result = bfs(graph, start_node)
    dfs_result = dfs(graph, start_node)

    # Output the results
    print("BFS Order:", bfs_result)
    print("DFS Order with Backtracking:", dfs_result)

if __name__ == "__main__":
    main()
