import gc
import time
import matplotlib.pyplot as plt
import seaborn as sns

times = []

def sudoku_performance_one_method(method, puzzle):
    gc.collect()
    gc.disable()
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

        # elapsed_mean_time = metrics["total_delta_time"] / number_of_tests
        # mean_steps = metrics["steps_taken"] / number_of_tests
        # print(f"{method} on {puzzle} puzzle yields {elapsed_mean_time}")
        # print(f"{method} on {puzzle} puzzle yields {mean_steps}")
    return metrics, times

# solution = bfs_solver(easy_sudoku)
# print(solution[1])


# sudoku_puzzles = prepare_tests(6.0, 7.0)

# sudoku_puzzles = [puzzle_al_escargot]
# sudoku_methods = [bfs_solver]

#
# list_tests = []
# for i in sudoku_puzzles[:200]:
#     list_tests.append(i.tolist())


# sudoku_performance_all_methods(sudoku_methods, sudoku_puzzles, 10)


def plot_times(times):
    sns.histplot(times, kde=True, bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Solving time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Solving time distribution for BFS')
    plt.show()

# plot_times(times)

