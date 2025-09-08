from analyze_bed import sudoku_performance_all_methods
from solvers.sat_solver import solve_sudoku_sat
from test_importer import prepare_tests
from utils.plots import plot_times
from utils.statistics import analyze_metrics

sudoku_puzzles = prepare_tests(2.1, 3.0, 30000)
# Change here the algorithm to test.
metrics, times = sudoku_performance_all_methods(solve_sudoku_sat, sudoku_puzzles, 10, 2)

analyze_metrics(times)

plot_times(times)