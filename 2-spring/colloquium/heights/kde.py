import numpy as np
import scipy
import shutil
import os
from sklearn.neighbors import KernelDensity

import matplotlib
from matplotlib import pyplot as plt

COUNT = 10000
XMIN = 1e-3
S = 2

matplotlib.rc('font', **{
    'family': 'Minion Pro',
    'size': 22,
})


def generate():
    prng = np.random.RandomState(12348)
    return XMIN * (prng.pareto(S - 1, size=COUNT) + 1)

def histogram(data):
    return np.histogram(data, bins=np.linspace(1300, 2100, 80))

def gauss(data, c, mean, stddev):
    return c / (np.sqrt(2 * np.pi) * stddev) * np.exp(-(data - mean)**2 / (2 * stddev**2))

def double_gauss(data, c1, mean1, stddev1, c2, mean2, stddev2):
    return gauss(data, c1, mean1, stddev1) + gauss(data, c2, mean2, stddev2)

def pareto(x):
    return np.where(x <= XMIN, 0, (S - 1) * (XMIN**(S-1)) / x**S)

data = generate()
x = np.linspace(1.000, 2.500, 1500)
bw = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30, 50, 100, 200, 300, 500, 1000, 1500, 3000, 5000, 10000]
bandwidths = 10 ** np.linspace(-3.75, -0.5, 50)

def kde_frames(data):
    shutil.rmtree('kde', ignore_errors=True)
    os.makedirs('kde')
    i = 0
    mises = []

    for h in bandwidths:
        kde = KernelDensity(kernel='gaussian', bandwidth=h).fit(data[:, np.newaxis])
        y = (FEMALE_COUNT + MALE_COUNT) * np.exp(kde.score_samples(x[:, np.newaxis]))

        result = scipy.integrate.trapz((yo - y)**2, x)
        mises.append(result)

        plt.figure(figsize=(16, 10))
        plt.fill_between(x, y, 0, color=(0, 0, 0.7, 0.5))
        plt.fill_between(x, (y-yo)**2 / 1e3, 0, color=(0.7, 0.3, 0, 0.2))
        plt.plot(x, yo)
        plt.xlim(1, 2.5)
        plt.ylim(0, 80000)
        plt.xlabel('height / m')
        plt.tight_layout(rect=(0, 0, 1, 1))
        plt.title(f'Bandwidth {h:.6f}, MISE {result:.0f}')
        plt.savefig(f'kde/{i:03d}.png')
        plt.close()
        print(f"{i}")
        i = i + 1

    return mises

def plot_mises(mises):
    plt.figure(figsize=(16, 10))
    plt.xlim(0, 0.2)
    plt.xlabel('bandwidth')
    plt.ylabel('MISE')
    plt.yscale('log')
    plt.plot(bandwidths, mises)
    plt.tight_layout(rect=(0, 0, 1, 1))
    plt.savefig('kde/mise.png')
    plt.close()


def show_histogram(data):
    plt.figure(figsize=(16, 10))
    bins, edges = np.histogram(data, bins=np.linspace(0, 1, 101), density=True)
    plt.bar(edges[:-1], bins, width=1e-2, align='edge', color=(0.7, 0, 0.5, 0.5))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig('histogram.png')
    plt.close()


def show_kde(data):
    plt.figure(figsize=(16, 10))
    x = np.linspace(-3.5, 1.5, 1000)
    kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(data[:, np.newaxis])
    y = kde.score_samples(x[:, np.newaxis])

    plt.fill_between(x, y, 0, color=(0, 0, 0.7, 0.5))
    plt.plot(x, np.log(pareto(np.exp(x))))
    plt.xlim(-10, 3)
    plt.savefig('kde.png')
    plt.close()



def hist_frames(data):
    shutil.rmtree('hist', ignore_errors=True)
    os.makedirs('hist')
    i = 0
    mises = []

    for h in bw:
        plt.figure(figsize=(16, 10))
        bins, edges = np.histogram(data, bins=np.linspace(1, 2.5, h + 1), density=True)

        plt.bar(edges[:-1], (MALE_COUNT + FEMALE_COUNT) * bins, width=1.5 / h, align='edge', color=(0.7, 0, 0.5, 0.5))

        plt.plot(x, yo)
        plt.xlabel('height / m')
        plt.xlim(1, 2.5)
        plt.ylim(0, 80000)
        plt.tight_layout(rect=(0, 0, 1, 1))
        plt.title(f'Bin width {1.5 / h:.6f}')
        plt.savefig(f'hist/{i:03d}.png')
        plt.close()
        print(f"{i}")
        i = i + 1

    return mises


def hist_shift(data):
    i = 1000
    mises = []

    for h in [300]:
        for s in np.linspace(0, 0.01, 101):
            plt.figure(figsize=(16, 10))
            bins, edges = np.histogram(data, bins=np.linspace(1 + s, 2.5 + s, h + 1), density=True)
            print(edges)

            plt.bar(edges[:-1], COUNT * bins, width=1.5 / h, align='edge', color=(0.7, 0, 0.5, 0.5))

            plt.xlabel('height / m')
            plt.xlim(1, 2.5)
            plt.ylim(0, 80000)
            plt.tight_layout(rect=(0, 0, 1, 1))
            plt.title(f'Bin width {1.5 / h:.6f}')
            plt.savefig(f'hist/{i:03d}.png')
            plt.close()
            print(f"{i} {s}")
            i = i + 1

    return mises


def fit(data):
    xh = np.linspace(0, 1, 1001)
    bins, edges = np.histogram(data, bins=xh, density=True)
    popt, pcov = scipy.optimize.curve_fit(double_gauss, xh[:-1], bins, ftol=1e-12)
    males = popt[0] * (MALE_COUNT + FEMALE_COUNT)
    females = popt[3] * (MALE_COUNT + FEMALE_COUNT)
    male_mean = popt[1]
    female_mean = popt[4]
    male_sigma = popt[2]
    female_sigma = popt[5]

    plt.figure(figsize=(16, 10))
    plt.xlabel('height / m')
    plt.xlim(1, 2.5)
    plt.ylim(0, 60000)
    plt.bar(edges[:-1], (MALE_COUNT + FEMALE_COUNT) * bins, width=1.5 / 150, align='edge', color=(0.7, 0, 0.5, 0.5))
    plt.tight_layout(rect=(0, 0, 1, 1))
    plt.savefig('hist/hist.png')
    plt.close()

    plt.figure(figsize=(16, 10))
    plt.xlabel('height / m')
    plt.xlim(1, 2.5)
    plt.ylim(0, 60000)
    plt.bar(edges[:-1], (MALE_COUNT + FEMALE_COUNT) * bins, width=1.5 / 150, align='edge', color=(0.7, 0, 0.5, 0.3))
    plt.plot(x, gauss(x, males, male_mean, male_sigma), color=(0.0, 0.0, 0.8, 1))
    plt.plot(x, gauss(x, females, female_mean, female_sigma), color=(1, 0.0, 0.8, 1))
    plt.plot(x, double_gauss(x, males, male_mean, male_sigma, females, female_mean, female_sigma), color=(1, 0.5, 0, 1))
    plt.tight_layout(rect=(0, 0, 1, 1))
    plt.savefig('hist/fit.png')
    plt.close()

    plt.figure(figsize=(16, 10))
    plt.xlabel('height / m')
    plt.xlim(1, 2.5)
    plt.ylim(0, 60000)
    plt.bar(edges[:-1], (MALE_COUNT + FEMALE_COUNT) * bins, width=1.5 / 150, align='edge', color=(0.7, 0, 0.5, 0.3))
    plt.plot(x, yo)
    plt.plot(x, gauss(x, males, male_mean, male_sigma), color=(0.0, 0.0, 0.8, 1))
    plt.plot(x, gauss(x, females, female_mean, female_sigma), color=(1, 0.0, 0.8, 1))
    plt.plot(x, double_gauss(x, males, male_mean, male_sigma, females, female_mean, female_sigma), color=(1, 0.5, 0, 1))
    plt.tight_layout(rect=(0, 0, 1, 1))
    plt.title(f'Males: {males:.0f}, {male_mean:.3f} m, females: {females:.0f}, {female_mean:.3f} m')
    plt.savefig('hist/full.png')
    plt.close()



def main():
    data = np.log(generate())
    print(data)

    show_histogram(data)
    show_kde(data)

  #  mises = kde_frames(stacked)
  #  plot_mises(mises)

   ## mises = hist_frames(stacked)
    #plot_mises(mises)


main()

