import json
import os
import statistics

import numpy as np

from backtracking import solve_sudoku_aux, solve_sudoku_backtracking
from bfs_solver import bfs_solver
from analyze_bed import sudoku_performance_all_methods
from hard_tests import puzzle_al_escargot, platinum_blonde_sudoku, golden_nugget_sudoku
from sat_solver import solve_sudoku_sat
from utils.statistics import bootstrap_resampling, analyze_metrics

metrics, times = sudoku_performance_all_methods(solve_sudoku_sat, [golden_nugget_sudoku], 6, 2)

analyze_metrics(times)