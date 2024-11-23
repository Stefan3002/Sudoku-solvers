import time

from bfs_solver import bfs_solver
from hard_tests import puzzle_al_escargot, easy_1_sudoku
from sat_solver import solve_sudoku_sat


# from sat_solver import solve_sudoku_sat


def sudoku_performance_one_method(method, puzzle):
    print("STARTED ALGO")
    result = method(puzzle)
    print("FINISHED ALGO")

sudoku_performance_one_method(solve_sudoku_sat, puzzle_al_escargot)