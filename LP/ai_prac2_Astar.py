import heapq

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        current_position = current_node.position

        if current_position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_position)

        for direction in directions:
            neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                if neighbor in closed_list:
                    continue

                g_cost = current_node.g_cost + 1
                h_cost = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

                if not any(node.position == neighbor and node.f_cost <= neighbor_node.f_cost for node in open_list):
                    heapq.heappush(open_list, neighbor_node)
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Example grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
