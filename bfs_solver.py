import copy
import time


def is_filled(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return False
    return True


def is_valid(board, row, col, num):
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


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 denotes an empty cell
                return i, j
    return None  # No empty cell found

def bfs_solver(puzzle):
    queue = [puzzle]
    steps = 0
    while len(queue) > 0:
        steps += 1
        current = queue.pop(0)
        if is_filled(current):
            return {
                "solution": current,
                "steps": steps
            }

        current_cell_i, current_cell_j = find_empty_location(current)

        for choice in range(1, 10):
            if is_valid(current, current_cell_i, current_cell_j, choice):
                new_state = copy.deepcopy(current)
                new_state[current_cell_i][current_cell_j] = choice
                queue.append(new_state)
    return {
                "solution": False,
                "steps": steps
        }

puzzle_al_escargot = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 2, 3, 0, 0, 4, 0, 0],
    [0, 0, 1, 8, 0, 0, 0, 0, 5],
    [0, 6, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 8, 5, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 4, 0, 5, 0, 0],
    [4, 7, 0, 0, 0, 6, 0, 0, 0]
]

platinum_blonde_sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 2, 3, 0, 0, 4, 0, 0],
    [0, 0, 1, 8, 0, 0, 0, 0, 5],
    [0, 6, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 8, 5, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 4, 0, 5, 0, 0],
    [4, 7, 0, 0, 0, 6, 0, 0, 0]
]
easy_1_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

easy_2_sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

easy_3_sudoku = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 4, 0, 9, 5, 0, 0],
    [0, 0, 5, 9, 0, 1, 3, 0, 0],
    [1, 0, 0, 7, 0, 3, 0, 0, 8],
    [0, 0, 9, 0, 5, 0, 1, 0, 0]
]

easy_0_sudoku = [
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def test_performance_one_method(method, puzzle):
    start_time = time.time()
    result = method(puzzle)
    end_time = time.time()
    delta_time = end_time - start_time

    return {
        "delta_time": delta_time,
        "steps": result["steps"]
    }

def test_performance_all_methods(methods, puzzles, number_of_tests = 10):
    for method in methods:
        for puzzle in puzzles:
            metrics = {
                "total_delta_time": 0,
                "steps_taken": 0
            }
            for no_test in range(number_of_tests):
                results = test_performance_one_method(method, puzzle)
                metrics["total_delta_time"] += results["delta_time"]
                metrics["steps_taken"] += results["steps"]

            elapsed_mean_time = metrics["total_delta_time"] / number_of_tests
            mean_steps = metrics["steps_taken"] / number_of_tests
            print(f"{method} on {puzzle} puzzle yields {elapsed_mean_time}")
            print(f"{method} on {puzzle} puzzle yields {mean_steps}")

# solution = bfs_solver(easy_sudoku)
# print(solution[1])


test_puzzles = [easy_1_sudoku]
test_methods = [bfs_solver]

test_performance_all_methods(test_methods, test_puzzles, 1)
