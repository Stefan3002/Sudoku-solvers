import statistics

import numpy as np

from analyze_bed import sudoku_performance_all_methods
from hard_tests import puzzle_al_escargot
from sat_solver import solve_sudoku_sat
from test_importer import prepare_tests
from utils.plots import plot_times
from utils.statistics import bootstrap_resampling, analyze_metrics

sudoku_puzzles = prepare_tests(0.0, 1.0)
metrics, times = sudoku_performance_all_methods(solve_sudoku_sat, sudoku_puzzles, 10, 2)

analyze_metrics(times)

plot_times(times)