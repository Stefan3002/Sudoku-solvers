from tests.analyze_bed import sudoku_performance_all_methods
from tests.hard_coded_puzzles import golden_nugget_sudoku
from solvers.sat_solver import solve_sudoku_sat
from utils.statistics import analyze_metrics

metrics, times = sudoku_performance_all_methods(solve_sudoku_sat, [golden_nugget_sudoku], 6, 2)

analyze_metrics(times)