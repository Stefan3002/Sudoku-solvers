import copy


def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row, column, and 3x3 box
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

def solve_sudoku_aux(board):
    board_copy = copy.deepcopy(board)
    solve_sudoku_backtracking(board_copy)

def solve_sudoku_backtracking(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Assign the number
                        if solve_sudoku_backtracking(board):  # Recurse to solve the rest
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

