import copy


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
            return current, steps

        current_cell_i, current_cell_j = find_empty_location(current)

        for choice in range(1, 10):
            if is_valid(current, current_cell_i, current_cell_j, choice):
                new_state = copy.deepcopy(current)
                new_state[current_cell_i][current_cell_j] = choice
                queue.append(new_state)
    return False, 0

puzzle = [
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

solution = bfs_solver(puzzle)
print(solution[1])