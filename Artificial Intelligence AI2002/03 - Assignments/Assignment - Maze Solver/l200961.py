from typing import List, Tuple
from collections import deque

def load_maze(file_name: str) -> List[List[int]]:
    maze = []
    with open(file_name) as f:
        for line in f:
            row = []
            for ch in line.strip().split():
                # append 1 for wall, 0 for start, 99 for goal, and int for cost
                if ch == 'S':
                    row.append(0)
                elif ch == 'G':
                    row.append(99)
                else:
                    row.append(int(ch))
            maze.append(row)
    return maze

def dfs(maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """"Returns a list of nodes in the path from start to goal, or an empty list if no path exists"""
    def search(curr):
        """Returns True if goal is found, False otherwise"""
        if curr == goal:
            return True
        visited.add(curr)
        for neighbor in neighbors(curr):
            if neighbor not in visited and maze[neighbor[0]][neighbor[1]] != 1:
                if search(neighbor):
                    path.append(neighbor)
                    return True
        return False

    def neighbors(node):
        """Returns a list of neighbors of node"""
        for r, c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            neighbor = (node[0] + r, node[1] + c)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != 1:
                yield neighbor

    path = [start]
    visited = set()
    search(start)
    return path[::-1]


def bfs(maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Returns a list of nodes in the path from start to goal, or an empty list if no path exists"""
    def neighbors(node):
        for r, c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            neighbor = (node[0] + r, node[1] + c)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != 1:
                yield neighbor
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for neighbor in neighbors(node):
            if neighbor not in visited and maze[neighbor[0]][neighbor[1]] != 1:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node

    path = []
    while node:
        path.append(node)
        node = parent[node]

    return path[::-1]

def q1():
    file_name = input("Enter maze file name: ")
    maze = load_maze(file_name)
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                start = (i, j)
            elif maze[i][j] == 99:
                goal = (i, j)
    dfs_path = dfs(maze, start, goal)
    bfs_path = bfs(maze, start, goal)
    print(f"DFS Path: {dfs_path}")
    print(f"BFS Path: {bfs_path}")
    
    import matplotlib.pyplot as plt
    import numpy as np
    # plotting the maze
    fig, ax = plt.subplots(figsize=(len(maze[0]), len(maze)))

    # plot walls
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, len(maze)-i-1), 1, 1, color='gray'))

    # plot start and goal points
    ax.add_patch(plt.Rectangle((start[1], len(maze)-start[0]-1), 1, 1, color='green'))
    ax.add_patch(plt.Rectangle((goal[1], len(maze)-goal[0]-1), 1, 1, color='red'))

    # plot path
    print('Now plotting\nwhich path to plot?\t1. DFS\t2. BFS')
    choice = input()
    if choice == '1':
        x, y = zip(*dfs_path)
        ax.plot(y, len(maze)-1-np.array(x), 'bo-')
    if choice == '2':
        x, y = zip(*bfs_path)
        ax.plot(y, len(maze)-1-np.array(x), 'bo-')

    # set axis limits and ticks
    ax.set_xlim(0, len(maze[0]))
    ax.set_ylim(0, len(maze))
    ax.set_xticks(range(len(maze[0])+1))
    ax.set_yticks(range(len(maze)+1))

    # invert y-axis to match maze orientation
    ax.invert_yaxis()

    # show plot
    plt.show()

def q2():
    from heapq import heappop, heappush

    class Node:
        def __init__(self, location):
            self.location = location
            self.neighbors = []
            self.parent = None
            self.g = float('inf')
            self.f = 0

        def clear(self):
            self.parent = None
            self.g = float('inf')
            self.f = 0

        def addneighbor(self, cost, other):
            # add edge in both directions
            self.neighbors.append((cost, other))
            other.neighbors.append((cost, self))

        def __gt__(self, other):  # make nodes comparable
            return self.f > other.f

        def __repr__(self):
            return str(self.location)

    class Graph:
        def __init__(self, filename):
            def read_file(self, filename):
                with open(filename, "r") as f:
                    content = f.read().splitlines()
                    content = [row.replace(' ', '') for row in content]  # remove spaces
                    content = [row.replace('S', '6') for row in content]  # replace start with 6
                    content = [row.replace('G', '9') for row in content]  # replace goal with 9
                    
                    height = len(content)
                    width = len(content[0])
                    grid = [[int(x) for x in row] for row in content]

                    # set start and goal nodes
                    start = None
                    goal = None
                    for i in range(1, height-1):
                        for j in range(1, width-1):
                            if content[i-1][j-1] == '6':
                                if start is None:
                                    start = (i, j)
                                else:
                                    raise ValueError("Multiple start positions")
                            elif content[i-1][j-1] == '9':
                                if goal is None:
                                    goal = (i, j)
                                else:
                                    raise ValueError("Multiple goal positions")
                    if start is None or goal is None:
                        raise ValueError("Missing start or goal position")
                    return grid, start, goal
            
            self.grid,self.start, self.goal = read_file(self, filename)
            
        @staticmethod
        def reconstructpath(node):
            path = []
            while node is not None:
                path.append(node)
                node = node.parent
            path.reverse()
            return path

        @staticmethod
        def heuristic(a, b):
            # optimistic score, assuming all cells are friendly
            dy = abs(a[0] - b[0])
            dx = abs(a[1] - b[1])
            return min(dx, dy) * 15 + abs(dx - dy) * 10

        def clear(self):
            # remove search data from graph 
            for row in self.nodes:
                for node in row:
                    node.clear()

        def a_star(self, start, end):
            self.clear()
            startnode = self.nodes[start[0]][start[1]]
            endnode = self.nodes[end[0]][end[1]]
            startnode.g = 0
            openlist = [startnode] 
            closed = set()
            while openlist:
                node = heappop(openlist)
                if node in closed:
                    continue
                closed.add(node)
                if node == endnode:
                    return self.reconstructpath(endnode)
                for weight, neighbor in node.neighbors:
                    g = node.g + weight
                    if g < neighbor.g:
                        neighbor.g = g
                        neighbor.f = g + self.heuristic(neighbor.location, endnode.location)
                        neighbor.parent = node
                        heappush(openlist, neighbor)    
    graph = Graph('C://Users//ammar//Desktop//Slides & Docs//Assignments + Notes//AI//input2.txt') 
    path = graph.a_star(graph.start, graph.goal)
    print   (path)



if __name__ == '__main__':
    inp = input('Which part to run?\n\t\t')
    if inp:
        if inp == '1':
            q1()
        if inp == '2':
            q2()