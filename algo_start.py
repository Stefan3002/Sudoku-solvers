import json
import os
import statistics

import numpy as np

from backtracking import solve_sudoku_aux
from bfs_solver import bfs_solver
from analyze_bed import sudoku_performance_all_methods
from hard_tests import puzzle_al_escargot
from sat_solver import solve_sudoku_sat

metrics, times = sudoku_performance_all_methods(bfs_solver, [puzzle_al_escargot], 6, 2)

print(metrics)
print('Mean: ', np.mean(times))
print('Median: ', statistics.median(times))
print('Std Dev: ', statistics.stdev(times))

with open('test_times.txt', 'w') as f:
    for time in times:
        f.write(f'{time}\n')


def bootstrap_resampling(data, iterations = 1000):
    means = []
    medians = []
    std_devs = []

    for _ in range(iterations):
        sample = np.random.choice(data, size=len(data), replace=True)
        means.append(np.mean(sample))
        medians.append(statistics.median(sample))
        std_devs.append(statistics.stdev(sample))
    return means, medians, std_devs

means, medians, std_devs = bootstrap_resampling(times)

confidence_mean = np.percentile(means, [2.5, 97.5])
confidence_medians = np.percentile(medians, [2.5, 97.5])
confidence_std_devs = np.percentile(std_devs, [2.5, 97.5])

print('Mean lies between: ', confidence_mean)
print('Median lies between: ', confidence_medians)
print('Std Dev lies between: ', confidence_std_devs)

with open('test_metrics.txt', 'w') as f:
    f.write(f'{confidence_mean}\n')
    f.write(f'{confidence_medians}\n')
    f.write(f'{confidence_std_devs}\n')