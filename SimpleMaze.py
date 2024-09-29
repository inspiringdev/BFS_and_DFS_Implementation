from collections import deque
import matplotlib.pyplot as plt
import numpy as np


def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start, goal = (0, 0), (rows - 1, cols - 1)

    if maze[start[0]][start[1]] == 1 or maze[goal[0]][goal[1]] == 1:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (current_row, current_col), path = queue.popleft()

        if (current_row, current_col) == goal:
            return path

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze[new_row][
                new_col] == 0:
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
                visited.add((new_row, new_col))

    return None


def plot_maze(maze, path=None):
    maze_array = np.array(maze)
    rows, cols = maze_array.shape

    fig, ax = plt.subplots()
    ax.imshow(maze_array, cmap="gray_r")

    if path:
        path = np.array(path)
        ax.plot(path[:, 1], path[:, 0], color='red')

    plt.show()

import matplotlib.pyplot as plt
import numpy as np

def plot_maze(maze, path):
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap=plt.cm.binary)

    # Plot the path if it exists
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_y, path_x, color="blue", linewidth=2, marker='o', markersize=5, label='Path')

    # Set axis limits and labels
    ax.set_xticks(np.arange(-0.5, maze.shape[1], 1))
    ax.set_yticks(np.arange(-0.5, maze.shape[0], 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='black', linestyle='-', linewidth=1)

    # Show start and goal points
    ax.plot(0, 0, marker='o', color='green', markersize=10, label='Start')
    ax.plot(maze.shape[1]-1, maze.shape[0]-1, marker='o', color='red', markersize=10, label='Goal')

    ax.legend()
    plt.show()

# Example usage
maze = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
])

# Find the path using BFS (assuming bfs function is defined)
path = bfs(maze)

# Plot the maze and the path
plot_maze(maze, path)
