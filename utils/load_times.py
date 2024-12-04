import numpy as np


def load_times(path):
    with open(path, 'r') as f:
        times = f.readlines()
        times = [float(time[:-1]) for time in times]
        return np.array(times)


times = load_times('/home/stefan/PycharmProjects/sudoku_bfs/test_times.txt')
print(times)