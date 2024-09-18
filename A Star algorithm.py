import heapq

def heuristic(a, b):
    # Example heuristic: Euclidean distance
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def astar(graph, start, goal):
    # Priority queue for the open set
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionaries to track the cost of the path and the parent of each node
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        # Get the node with the lowest f_score
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            # Reconstruct the path from the goal to the start
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                # Update the best path to the neighbor
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                
                if all(neighbor != node for _, node in open_set):
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # If no path is found

# Example usage
if __name__ == "__main__":
    # Define a graph as an adjacency list with weights
    graph = {
        (0, 0): [((1, 0), 1), ((0, 1), 1)],
        (1, 0): [((1, 1), 1), ((0, 0), 1)],
        (0, 1): [((1, 1), 1), ((0, 0), 1)],
        (1, 1): [((1, 0), 1), ((0, 1), 1)]
    }
    
    start = (0, 0)
    goal = (1, 1)
    
    path = astar(graph, start, goal)
    
    print("Path found:", path)
