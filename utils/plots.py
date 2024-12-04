import math

from matplotlib import pyplot as plt
import seaborn as sns

def plot_times(times):
    if len(times) <= 200:
        no_bins = int(math.log(len(times), 2) + 1)
    else:
        no_bins = int(2 * (len(times) ** (1/3)) )
    sns.histplot(times, kde=True, bins=no_bins, color='skyblue', edgecolor='black')
    plt.xlabel('Solving time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Solving time distribution for SAT')
    plt.show()