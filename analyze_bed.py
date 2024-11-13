import time
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

from bfs_solver import bfs_solver
from hard_tests import easy_1_sudoku
from sat_solver import solve_sudoku_sat
from test_importer import prepare_tests

times = []

def sudoku_performance_one_method(method, puzzle):
    start_time = time.time()
    result = method(puzzle)
    end_time = time.time()
    delta_time = end_time - start_time

    return {
        "delta_time": delta_time,
        "steps": result["steps"]
    }

def sudoku_performance_all_methods(methods, puzzles, number_of_tests = 10):
    for method in methods:
        index = 0
        for puzzle in puzzles:
            index += 1
            metrics = {
                "total_delta_time": 0,
                "steps_taken": 0
            }
            for no_test in range(number_of_tests):
                results = sudoku_performance_one_method(method, puzzle)
                metrics["total_delta_time"] += results["delta_time"]
                metrics["steps_taken"] += results["steps"]

            elapsed_mean_time = metrics["total_delta_time"] / number_of_tests
            mean_steps = metrics["steps_taken"] / number_of_tests
            # print(f"{method} on {puzzle} puzzle yields {elapsed_mean_time}")
            # print(f"{method} on {puzzle} puzzle yields {mean_steps}")
            print(index)
            times.append(elapsed_mean_time)

# solution = bfs_solver(easy_sudoku)
# print(solution[1])


sudoku_puzzles = prepare_tests(6.0, 7.0)
sudoku_methods = [solve_sudoku_sat]


list_tests = []
for i in sudoku_puzzles[:200]:
    list_tests.append(i.tolist())


sudoku_performance_all_methods(sudoku_methods, list_tests, 100)


def plot_times(times):
    sns.histplot(times, kde=True, bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Solving time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Solving time distribution for BFS')
    plt.show()

plot_times(times)

print(np.mean(times))