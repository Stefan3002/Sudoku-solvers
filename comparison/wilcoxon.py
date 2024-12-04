from scipy.stats import wilcoxon

from utils.load_times import load_times


def wilcoxon_2_files(path1, path2):
    times1 = load_times(path1)
    times2 = load_times(path2)

    stat, p_value = wilcoxon(times1, times2)
    significance_level = .005
    bonferroni_p_value = significance_level / len(times1)

    print(stat, p_value, bonferroni_p_value)

wilcoxon_2_files('/home/stefan/PycharmProjects/sudoku_bfs/data/test_times.txt',
                 '/home/stefan/PycharmProjects/sudoku_bfs/data/test_times2.txt'
                 )