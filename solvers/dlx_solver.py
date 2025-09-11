import numpy as np
import time

# Node class for the Dancing Links structure
class Node:
    def __init__(self, row=None, column=None):
        self.row = row
        self.column = column
        self.up = self.down = self.left = self.right = self  # Circular links

# Dancing Links algorithm for solving exact cover problems
class DancingLinks:
    def __init__(self, matrix):
        self.header = Node()
        self.columns = []
        self.solution = []
        self.build(matrix)  # Build the linked structure from the matrix

    # Build the Dancing Links structure from the exact cover matrix
    def build(self, matrix):
        self.columns = [Node(column=i) for i in range(len(matrix[0]))]
        self.header.right = self.columns[0]
        self.columns[0].left = self.header
        self.columns[0].down = self.columns[0]
        self.columns[0].up = self.columns[0]
        for i in range(1, len(self.columns)):
            self.columns[i - 1].right = self.columns[i]
            self.columns[i].left = self.columns[i - 1]
            self.columns[i].down = self.columns[i]
            self.columns[i].up = self.columns[i]
        self.columns[-1].right = self.header
        self.header.left = self.columns[-1]

        # Build nodes for each row in the matrix
        for row_index, row in enumerate(matrix):
            prev = None
            first_node = None
            for col_index, cell in enumerate(row):
                if cell:
                    node = Node(row=row_index, column=col_index)
                    col_node = self.columns[col_index]

                    # Find the last node in the column
                    while col_node.down != self.columns[col_index]:
                        col_node = col_node.down
                    node.up = col_node
                    col_node.down = node

                    node.down = self.columns[col_index]

                    # Link nodes in the row
                    if prev:
                        prev.right = node
                        node.left = prev
                    else:
                        first_node = node
                    prev = node

            # Close the row circularly
            if prev:
                prev.right = first_node
                first_node.left = prev

    # Cover a column (remove it from the matrix)
    def cover(self, column):
        col = self.columns[column]
        col.right.left = col.left
        col.left.right = col.right

        node = col.down
        while node != col:
            row_node = node.right
            while row_node != node:
                row_node.down.up = row_node.up
                row_node.up.down = row_node.down
                row_node = row_node.right
            node = node.down

    # Uncover a column (restore it to the matrix)
    def uncover(self, column):
        col = self.columns[column]
        col.right.left = col
        col.left.right = col

        node = col.down
        while node != col:
            row_node = node.right
            while row_node != node:
                row_node.down.up = row_node
                row_node.up.down = row_node
                row_node = row_node.right
            node = node.down

    # Select the column with the fewest 1s (heuristic for efficiency)
    def select_column(self):
        min_ones = float('inf')
        selected_column = None
        col = self.header.right
        while col != self.header:
            count = 0
            node = col.down
            while node != col:
                count += 1
                node = node.down
            if count < min_ones:
                min_ones = count
                selected_column = col
            col = col.right
        return selected_column

    # Recursive DLX solver
    def solve(self, iteration_count=0, max_iterations=1000000000):
        # if iteration_count > max_iterations:
        #     return None
        if self.header.right == self.header:
            return self.solution  # Solution found

        column = self.select_column()
        if column is None:  # No column to select, stop
            return None
        self.cover(column.column)

        row_node = column.down
        while row_node != column:
            self.solution.append(row_node.row)
            next_node = row_node.right
            while next_node != row_node:
                self.cover(next_node.column)
                next_node = next_node.right

            result = self.solve(iteration_count + 1, max_iterations)
            if result:
                return result

            self.solution.pop()
            next_node = row_node.right
            while next_node != row_node:
                self.uncover(next_node.column)
                next_node = next_node.right

            row_node = row_node.down

        self.uncover(column.column)
        return None

# Helper to get the index for the exact cover matrix
def get_index(r, c, num, constraint_type, n=9):
    n2 = n * n
    if constraint_type == 0:
        return r * n + c  # Cell constraint
    elif constraint_type == 1:
        return n2 + r * n + (num - 1)  # Row constraint
    elif constraint_type == 2:
        return 2 * n2 + c * n + (num - 1)  # Column constraint
    elif constraint_type == 3:
        return 3 * n2 + (r // 3 * 3 + c // 3) * n + (num - 1)  # Box constraint

# Convert a Sudoku puzzle to an exact cover matrix
def sudoku_to_exact_cover(sudoku, mapping=[]):
    n = 9
    n2 = n * n
    matrix = []

    for r in range(n):
        for c in range(n):
            if sudoku[r, c] != 0:
                num = sudoku[r, c]
                row = [0] * (4 * n2)
                row[get_index(r, c, num, 0)] = 1
                row[get_index(r, c, num, 1)] = 1
                row[get_index(r, c, num, 2)] = 1
                row[get_index(r, c, num, 3)] = 1
                matrix.append(row)
                mapping.append((r, c, num))
            else:
                for num in range(1, 10):
                    row = [0] * (4 * n2)
                    row[get_index(r, c, num, 0)] = 1
                    row[get_index(r, c, num, 1)] = 1
                    row[get_index(r, c, num, 2)] = 1
                    row[get_index(r, c, num, 3)] = 1
                    matrix.append(row)
                    mapping.append((r, c, num))

    return matrix, mapping

# Reconstruct the Sudoku solution from the DLX result
def reconstruct_solution(solution, mapping, n=9):
    sudoku = np.zeros((n, n), dtype=int)
    for candidate_row in solution:
        r, c, num = mapping[candidate_row]
        sudoku[r, c] = num
    return sudoku

# Main function to solve Sudoku using DLX
def solve_sudoku_dlx(puzzle):
    mapping = []
    exact_cover_matrix, mapping = sudoku_to_exact_cover(puzzle, mapping)
    dlx = DancingLinks(exact_cover_matrix)
    solution = dlx.solve()
    if solution:
        solved_sudoku = reconstruct_solution(solution, mapping)
        return solved_sudoku
    else:
        print("No solution!")

# print(solve_sudoku_dlx(sudoku))