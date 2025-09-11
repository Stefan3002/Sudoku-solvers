import numpy as np
from constraint import Problem, AllDifferentConstraint
import time

def check_consistency(sudoku_grid):
    """
    Check if the initial Sudoku grid respects basic constraints.
    """
    for r in range(9):
        if len(set(sudoku_grid[r, :]) - {0}) != np.count_nonzero(sudoku_grid[r, :] != 0):
            return False
    for c in range(9):
        if len(set(sudoku_grid[:, c]) - {0}) != np.count_nonzero(sudoku_grid[:, c] != 0):
            return False
    for sr in range(3):
        for sc in range(3):
            subgrid = sudoku_grid[sr*3:(sr+1)*3, sc*3:(sc+1)*3].flatten()
            if len(set(subgrid) - {0}) != np.count_nonzero(subgrid != 0):
                return False
    return True

def solve_sudoku(sudoku_grid, max_steps=100000000000, max_time=10):
    """
    Solve a Sudoku problem using CSP and return a dictionary with relevant info.

    Args:
        sudoku_grid (numpy.ndarray): A 9x9 matrix representing the Sudoku grid (0 = empty).
        max_steps (int): Maximum number of constraint checks allowed.
        max_time (float): Maximum execution time in seconds.

    Returns:
        dict: {
            "solution" (list[list[int]]): Solved grid,
            "steps" (int): Number of constraint checks performed,
            "status" (str): "success", "failure" or "timeout",
            "num_solutions" (int): Total number of solutions found
        }
    """
    start_time = time.time()

    if not check_consistency(sudoku_grid):
        return {"status": "failure", "solution": None, "steps": 0, "num_solutions": 0}

    steps_counter = {"counter": 0}

    def counting_constraint(fn):
        """
        Wrapper for constraints that counts evaluations.
        """
        def constraint(*args):
            if steps_counter["counter"] > max_steps:
                raise RuntimeError("Exceeded maximum steps")
            if time.time() - start_time > max_time:
                raise RuntimeError("Exceeded maximum execution time")
            steps_counter["counter"] += 1
            return fn(*args)
        return constraint

    # Create CSP problem
    problem = Problem()

    # Define variables
    for r in range(9):
        for c in range(9):
            if sudoku_grid[r][c] != 0:
                problem.addVariable((r, c), [sudoku_grid[r][c]])
            else:
                problem.addVariable((r, c), range(1, 10))

    # Row constraints
    for r in range(9):
        row_vars = [(r, c) for c in range(9)]
        problem.addConstraint(counting_constraint(AllDifferentConstraint()), row_vars)

    # Column constraints
    for c in range(9):
        col_vars = [(r, c) for r in range(9)]
        problem.addConstraint(counting_constraint(AllDifferentConstraint()), col_vars)

    # Subgrid constraints
    for sr in range(3):
        for sc in range(3):
            subgrid_vars = [(r, c) for r in range(sr * 3, (sr + 1) * 3)
                                       for c in range(sc * 3, (sc + 1) * 3)]
            problem.addConstraint(counting_constraint(AllDifferentConstraint()), subgrid_vars)

    try:
        solutions = problem.getSolutions()
        total_steps = steps_counter["counter"]

        if solutions:
            first_solution = solutions[0]
            solved_grid = [[first_solution[(r, c)] for c in range(9)] for r in range(9)]
            return {
                "solution": solved_grid,
                "steps": total_steps,
                "status": "success",
                "num_solutions": len(solutions)
            }
        else:
            return {
                "solution": None,
                "steps": total_steps,
                "status": "failure",
                "num_solutions": 0
            }
    except RuntimeError as e:
        return {
            "solution": None,
            "steps": steps_counter["counter"],
            "status": str(e),
            "num_solutions": 0
        }
