import random

import matplotlib.pyplot as plt


def test_samples(num_trials, sample_size):
    tight_mean, wide_mean = [], []
    for t in range(num_trials):
        sample_tight, sample_wide = [], []
        for i in range(sample_size):
            sample_tight.append(random.gauss(0, 1))
            sample_wide.append(random.gauss(0, 100))
        tight_mean.append(sum(sample_tight) / len(sample_tight))
        wide_mean.append(sum(sample_wide) / len(sample_wide))
    return tight_mean, wide_mean


tight_means, wide_means = test_samples(1000, 40)
plt.plot(wide_means, 'y*', label=' SD = 100')
plt.plot(tight_means, 'bo', label='SD = 1')
plt.xlabel('Sample Number')
plt.ylabel('Sample Mean')
plt.title('Means of Samples of Size ' + str(40))
plt.legend()
plt.show()

plt.figure()
plt.hist(wide_means, bins=20, label='SD = 100')
plt.title('Distribution of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency of Occurrence')
plt.legend()
