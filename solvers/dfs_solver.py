python
import copy

# Check if placing 'num' at (row, col) is valid according to Sudoku rules
def is_valid(board, row, col, num):
    # Check if 'num' is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is not present in the 3x3 subgrid
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

# Helper function to create a copy and solve the Sudoku
def solve_sudoku_aux(board):
    board_copy = copy.deepcopy(board)  # Create a deep copy to avoid modifying the original
    solve_sudoku_backtracking(board_copy)

# Recursive backtracking solver for Sudoku
def solve_sudoku_backtracking(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve_sudoku_backtracking(board):  # Recurse to solve the rest
                            return True
                        board[row][col] = 0  # Backtrack if not solvable
                return False  # No valid number found, trigger backtracking
    return True  # Puzzle solved