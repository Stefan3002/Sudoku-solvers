import time
from pysat.solvers import Solver
import numpy as np

from hard_tests import platinum_blonde_sudoku


def sudoku_to_sat_clauses(board):
    """
    Convert a Sudoku puzzle into CNF clauses for SAT solving.
    board: a 9x9 list of lists, with 0 representing empty cells and numbers 1-9 for filled cells.
    """
    clauses = []

    # Helper function to map (row, column, digit) to a single integer variable
    def var(i, j, k):
        return i * 81 + j * 9 + k + 1

    # Cell constraints: Each cell contains at least one number
    for i in range(9):
        for j in range(9):
            clauses.append([var(i, j, k) for k in range(9)])

    # Row constraints: Each number appears once per row
    for i in range(9):
        for k in range(9):
            for j1 in range(9):
                for j2 in range(j1 + 1, 9):
                    clauses.append([-var(i, j1, k), -var(i, j2, k)])

    # Column constraints: Each number appears once per column
    for j in range(9):
        for k in range(9):
            for i1 in range(9):
                for i2 in range(i1 + 1, 9):
                    clauses.append([-var(i1, j, k), -var(i2, j, k)])

    # Subgrid constraints: Each number appears once per 3x3 subgrid
    for k in range(9):
        for block_row in range(3):
            for block_col in range(3):
                # Collect all variables in the 3x3 block for the digit `k`
                block_cells = [
                    var(block_row * 3 + i, block_col * 3 + j, k)
                    for i in range(3) for j in range(3)
                ]
                # Add clauses that enforce each number appears exactly once per 3x3 subgrid
                # At least one occurrence in the subgrid
                clauses.append(block_cells)
                # At most one occurrence in the subgrid
                for idx1 in range(9):
                    for idx2 in range(idx1 + 1, 9):
                        clauses.append([-block_cells[idx1], -block_cells[idx2]])

    # Fixed cells: Use the initial numbers as additional constraints
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                clauses.append([var(i, j, board[i][j] - 1)])

    return clauses

def solve_sudoku_sat(board):
    """
    Solve a Sudoku puzzle using SAT solving.
    board: a 9x9 list of lists, with 0 for empty cells and numbers 1-9 for filled cells.
    Returns a solved board or None if no solution exists.
    """
    clauses = sudoku_to_sat_clauses(board)

    start_time = time.time()  # Start timing
    with Solver(name='g3') as solver:
        for clause in clauses:
            solver.add_clause(clause)

        if solver.solve():
            solution = solver.get_model()
            solved_board = [[0] * 9 for _ in range(9)]

            for v in solution:
                if v > 0:  # Only positive literals indicate actual values
                    v -= 1
                    i, j, k = v // 81, (v % 81) // 9, v % 9
                    solved_board[i][j] = k + 1
            end_time = time.time()  # End timing
            # print(f"Execution time for SAT: {end_time - start_time:.4f} seconds")  # Print time

            return {
                'solution': solved_board,
                'steps': 1
            }
        else:
            return None


# sudoku_np = np.array(platinum_blonde_sudoku)
# print(sudoku_np)
# solved_board = solve_sudoku_sat(platinum_blonde_sudoku)
# if solved_board:
#     for row in solved_board:
#         print(row)
# else:
#     print("No solution exists.")
