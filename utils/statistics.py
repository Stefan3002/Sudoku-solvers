import statistics

import numpy as np


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


def analyze_metrics(times):
    print('Mean: ', np.mean(times))
    print('Median: ', statistics.median(times))
    print('Std Dev: ', statistics.stdev(times))

    with open('test_times.txt', 'w') as f:
        for time in times:
            f.write(f'{time}\n')

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