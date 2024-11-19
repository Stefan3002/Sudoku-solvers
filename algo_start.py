import os

from analyze_bed import sudoku_performance_all_methods, sudoku_methods, sudoku_puzzles

pid = os.getpid()
print(pid)
sudoku_performance_all_methods(sudoku_methods, sudoku_puzzles, 2000)