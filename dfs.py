def dfs_iterative(graph, start):
    # Use a stack to store the nodes for DFS
    stack = [start]
    visited = set()
    
    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()
        
        if vertex not in visited:
            # Mark the vertex as visited
            visited.add(vertex)
            print(vertex, end=' ')
            
            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

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
    
    print("\nDFS traversal starting from node 0 (iterative):")
    dfs_iterative(graph, 0)
