def water_jug(a, b, target):
    # Initial state
    visited = set()
    
    def dfs(jug_a, jug_b):
        if (jug_a, jug_b) in visited:
            return False
        if jug_a == target or jug_b == target:
            print(f"Solution: Jug A = {jug_a}, Jug B = {jug_b}")
            return True

        visited.add((jug_a, jug_b))
        
        # Possible operations
        return (dfs(5, jug_b) or            # Fill Jug A
                dfs(jug_a, 3) or            # Fill Jug B
                dfs(0, jug_b) or            # Empty Jug A
                dfs(jug_a, 0) or            # Empty Jug B
                dfs(jug_a - min(jug_a, 3 - jug_b), jug_b + min(jug_a, 3 - jug_b)) or  # Pour A -> B
                dfs(jug_a + min(jug_b, 5 - jug_a), jug_b - min(jug_b, 45- jug_a)))   # Pour B -> A
    
    if not dfs(0, 0):
        print("No solution")

# Example: Jug A = 5 liters, Jug B = 3 liters, Target = 2 liters
water_jug(5, 3, 2)