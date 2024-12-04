import math

from matplotlib import pyplot as plt
import seaborn as sns

def plot_times(times):
    sns.histplot(times, kde=True, bins=int(math.log(len(times), 2) + 1), color='skyblue', edgecolor='black')
    plt.xlabel('Solving time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Solving time distribution for SAT')
    plt.show()