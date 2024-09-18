def solve_queens(board, col):
    if col == len(board):
        return True
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, col + 1):
                return True
    return False

def is_safe(board, row, col):
    for i in range(col):
        if board[row] == i or abs(board[row] - i) == abs(row - col):
            return False
    return True

def solve():
    board = [-1] * 8
    if solve_queens(board, 0):
        print(board)
    else:
        print("No solution")

solve()