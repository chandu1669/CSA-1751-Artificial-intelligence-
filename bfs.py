
from collections import deque

def bfs(graph, start):
    # Initialize a queue for BFS and a set to track visited nodes
    queue = deque([start])
    visited = set()
    
    # Start with the initial node
    visited.add(start)
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Define a graph using an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }
    
    print("BFS traversal starting from node 0:")
    bfs(graph, 0)

