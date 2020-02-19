import numpy as np
import scipy
from sklearn.neighbors import KernelDensity

import matplotlib
from matplotlib import pyplot as plt

def generate():
    return np.random.normal(1.625, 0.060, 6000), np.random.normal(1.770, 0.090, 8000)

def histogram(data):
    return np.histogram(data, bins=np.linspace(1300, 2100, 80))

def gauss(data, c, mean, stddev):
    return c / (np.sqrt(2 * np.pi) * stddev) * np.exp(-(data - mean)**2 / (2 * stddev**2))

def double_gauss(data, c1, mean1, stddev1, c2, mean2, stddev2):
    return gauss(data, c1, mean1, stddev1) + gauss(data, c2, mean2, stddev2)


def main():
    female, male = generate()
    stacked = np.hstack((female, male))
#    plt.hist(stacked, bins=80)
#    plt.show()
#    plt.hist(female, stacked=False, bins=80, color=(1, 0.4, 0, 0.6))
#    plt.hist(male, stacked=False, bins=80, color=(0, 0, 0.7, 0.6))
    x = np.linspace(0.500, 2.500, 1600)

    matplotlib.rc('font', **{
        'family': 'Minion Pro',
        'size': 22,
    })

    i = 0
    bandwidths = 10**np.linspace(-3.75, -0.75, 100)
    mises = []
    for h in bandwidths:
        kde = KernelDensity(kernel='gaussian', bandwidth=h).fit(stacked[:, np.newaxis])
        y = 14000 * np.exp(kde.score_samples(x[:, np.newaxis]))
        yo = double_gauss(x, 6000, 1.625, 0.060, 8000, 1.770, 0.090)
        result = scipy.integrate.trapz((yo - y)**2, x)
        mises.append(result)

        plt.figure(figsize=(16, 10))
        plt.fill_between(x, y, 0, color=(0, 0, 0.7, 0.5))
        plt.plot(x, yo)
        plt.xlim(1, 2.5)
        plt.ylim(0, 80000)
        plt.tight_layout(rect=(0, 0, 1, 1))
        plt.title(f'Bandwidth {h:.6f}, MISE {result:.0f}')
        plt.savefig(f'{i:03d}.png')
        plt.close()
        print(f"{i}")
        i = i + 1

    plt.figure(figsize=(16, 10))
    plt.xlim(0, 0.2)
    plt.yscale('log')
    plt.plot(bandwidths, mises)
    plt.tight_layout(rect=(0, 0, 1, 1))
    plt.savefig('mise.png')
    plt.close()

main()

