import gc
import time
import matplotlib.pyplot as plt
import seaborn as sns

times = []

def sudoku_performance_one_method(method, puzzle):
    gc.collect()
    gc.disable()
    if not isinstance(puzzle, list):
        puzzle = puzzle.tolist()
    start_time = time.perf_counter()
    result = method(puzzle)
    end_time = time.perf_counter()
    delta_time = end_time - start_time
    gc.enable()
    return {
        "delta_time": delta_time,
        "steps": 0
    }


def sudoku_performance_all_methods(method, puzzles, number_of_tests = 10, warm_ups = 0):
    print("STARTED ALGO")
    times = []
    index = 0
    for puzzle in puzzles:
        index += 1
        metrics = {
            "total_delta_time": 0,
            "steps_taken": 0
        }
        for no_test in range(1, number_of_tests + 1):
            results = sudoku_performance_one_method(method, puzzle)
            if no_test > warm_ups:
                times.append(results["delta_time"])
                metrics["total_delta_time"] += results["delta_time"]
                metrics["steps_taken"] += results["steps"]
    return metrics, times






