import copy
import time

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

# Initialize a dictionary to track statistics for each box
# box_stats = {(row, col): {'assignments': 0, 'backtracks': 0, 'final_value': None} for row in range(9) for col in range(9)}

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
                        # box_stats[(row, col)]['assignments'] += 1  # Log the assignment
                        if solve_sudoku_backtracking(board):  # Recurse to solve the rest
                            return True
                        board[row][col] = 0  # Backtrack
                        # box_stats[(row, col)]['backtracks'] += 1  # Log the backtrack
                return False
    # # If solved, assign the final value to each box
    # for row in range(9):
    #     for col in range(9):
    #         if board[row][col] != 0:  # Non-zero cell has a final value
    #             box_stats[(row, col)]['final_value'] = board[row][col]
    return True

# # Platinum Blonde Sudoku puzzle setup
# platinum_blonde_sudoku = [
#     [0, 0, 0, 0, 0, 0, 0, 1, 2],
#     [0, 0, 0, 0, 0, 0, 0, 0, 3],
#     [0, 0, 2, 3, 0, 0, 4, 0, 0],
#     [0, 0, 1, 8, 0, 0, 0, 0, 5],
#     [0, 6, 0, 0, 7, 0, 8, 0, 0],
#     [0, 0, 0, 0, 0, 9, 0, 0, 0],
#     [0, 0, 8, 5, 0, 0, 0, 0, 0],
#     [9, 0, 0, 0, 4, 0, 5, 0, 0],
#     [4, 7, 0, 0, 0, 6, 0, 0, 0]
# ]
#
# # Track the time to solve the Sudoku
# start_time = time.time()  # Start the timer
# # matrix = arto_inkala
# if solve_sudoku(matrix):
#     print("Sudoku solved!")
#     for row in matrix:
#         print(row)
# else:
#     print("No solution exists.")
#
# end_time = time.time()  # End the timer
# elapsed_time = end_time - start_time  # Calculate the elapsed time
#
# print(f"\nTime taken to solve the Sudoku: {elapsed_time:.4f} seconds")
#
# # Print statistics for each box (assignment, backtracks, final value)
# print("\nStatistics for each box:")
# for row in range(9):
#     for col in range(9):
#         stats = box_stats[(row, col)]
#         print(f"Box ({row},{col}) - Assignments: {stats['assignments']}, "
#               f"Backtracks: {stats['backtracks']}, Final Value: {stats['final_value']}")
