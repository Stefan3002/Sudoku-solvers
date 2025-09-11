import copy

# Check if the puzzle is completely filled (no zeros)
def is_filled(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return False
    return True

# Check if placing 'num' at (row, col) is valid according to Sudoku rules
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

# Find the next empty cell (returns (row, col) or None if full)
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 denotes an empty cell
                return i, j
    return None  # No empty cell found

# Breadth-first search solver for Sudoku
def bfs_solver(puzzle):
    queue = [puzzle]  # Initialize queue with the starting puzzle
    steps = 0
    while len(queue) > 0:
        steps += 1
        current = queue.pop(0)  # Get the next board state
        if is_filled(current):  # Check if solved
            return {
                "solution": current,
                "steps": steps
            }

        # Find the next empty cell to fill
        current_cell_i, current_cell_j = find_empty_location(current)

        # Try all possible numbers (1-9) in the empty cell
        for choice in range(1, 10):
            if is_valid(current, current_cell_i, current_cell_j, choice):
                new_state = copy.deepcopy(current)  # Copy the board
                new_state[current_cell_i][current_cell_j] = choice  # Place the number
                queue.append(new_state)  # Add new state to the queue
    # No solution found
    return {
        "solution": False,
        "steps": steps
    }