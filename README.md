8 QUEENS PROBLEM
 Algorithm:
Step 1:Board Representation: Represent the chessboard as an 8x8 grid, where each cell can be either empty or occupied by a queen.
Step 2:   Place Queen Function: Implement a function that attempts to place a queen in a given row. This function should check if the placement is valid by ensuring that no other queens threaten the newly placed queen.
Step 3: Backtracking Algorithm: a. Start with an empty chessboard. b. For each row from 0 to 7: i. Call the "Place Queen" function for the current row. ii. If a valid placement is found, move to the next row. iii. If no valid placement is found, backtrack to the previous row and continue searching for valid placements. c. If a valid placement is found for all rows, a solution is found.
 Step 4:   Recursion and Backtracking: a. The "Place Queen" function:
 i. Given a row, try placing a queen in each column of that row. 
ii. Check if the placement is valid by ensuring that no other queens threaten the newly placed queen. 
iii. If the placement is valid, mark the cell as occupied by a queen and move to the next row recursively. 
iv. If no valid placement is found in the current row, backtrack by removing the queen from the cell and returning to the previous row.
 Step 5:    Solution Extraction: Once a solution is found, you can extract the positions of the queens on the board to visualize the solution.

WATER JUG PROBLEM
ALGORITHM: 
STEP1:start the program 
Step2:give the required commands for vacuum cleaner 
Step3:Initialize two variables j1 and j2 to represent the current amount of water in each jug.
Step4:Set a target amount of water to measure out.
Step5:Create a list of possible actions, including filling a jug, emptying a jug, and pouring      water from one jug to the other.
Step6: Create an empty set to keep track of visited states.
Step7:Create a stack to keep track of states to visit, and add the initial state to the stack.



CRIPT ARITHMETIC 
ALGORITHM:
STEP1:start the program 
STEP 2:Generate all possible combinations of digit assignments for the letters involved.
STEP 3:For each combination, check if the equation holds true.
STEP 4:Print the combination that satisfies the equation.
STEP5:end the program

BFS
ALGORITHM:
STEP 1: Start from the initial node and enqueue it into the queue.
STEP 2:While the queue is not empty, dequeue a node and process it.
STEP 3:Enqueue all unvisited neighbors of the dequeued node.
STEP 4:Repeat steps 2 and 3 until the queue is empty.

DFS
ALGORITHM:
STEP1: Start at the initial node.
STEP 2:Mark the initial node as visited.
STEP 3:Explore an unvisited adjacent node, mark it as visited, and push it onto the stack.
STEP 4:If there are no unvisited adjacent nodes, backtrack by popping a node from the stack.
STEP 5:Repeat steps 3-4 until the stack is empty.


TRAVELING SALESMAN PROBLEM.
ALGORITHM:
STEP 1:start the program.
STEP 2:Brute Force: Check all possible permutations of cities and calculate the total distance for each. This approach becomes inefficient for larger datasets due to factorial time complexity.
STEP 3:Dynamic Programming (DP): Implement the Held-Karp algorithm, which reduces the number of redundant calculations. DP stores the optimal subproblem solutions to build the final solution.
STEP 4:Greedy Algorithms: Start with a city and repeatedly choose the nearest unvisited city until all cities are visited. Common methods include Nearest Neighbor and Minimum Spanning Tree.
STEP 6:Solution Extraction: Once the goal state is reached, follow the parent pointers from the goal node to the initial node to extract the sequence of moves that lead to the solution.
