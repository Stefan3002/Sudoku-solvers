import pandas as pd
import numpy as np
from numpy.f2py.auxfuncs import throw_error
from numpy.ma.core import count


def select_data_difficulty(dataframe, min_difficulty, max_difficulty):
    return dataframe[(dataframe.difficulty >= min_difficulty) & (dataframe.difficulty <= max_difficulty)]

def import_tests(min_difficulty, max_difficulty):
    dataframe = pd.read_csv("data/sudoku-3m.csv", nrows=None)
    # print(dataframe[:10])
    # Max is 8.5
    # print(np.max(dataframe.difficulty))
    # Min is 0.0
    # print(np.min(dataframe.difficulty))
    tests = select_data_difficulty(dataframe, min_difficulty, max_difficulty)
    return tests

def prepare_tests(min_difficulty = 0.0, max_difficulty = 1.1, no_rows = 100):
    tests = import_tests(min_difficulty, max_difficulty)

    if len(tests) < no_rows:
        raise Exception(f"Number of tests is {len(tests)} and is less than {no_rows}")
    tests = tests[:no_rows]

    tests.puzzle = tests.puzzle.apply(lambda puzzle: puzzle.replace('.', '0'))
    tests.puzzle = tests.puzzle.apply(lambda puzzle: np.array([int(char) for char in puzzle]).reshape(9, 9))
    return np.array(tests.puzzle)


