import numpy as np
from scipy import integrate
from pprint import pprint as pp
from matplotlib import pyplot as plt


R = 6371000

def density(h):
    return np.where(
        h >= 0,
        np.where(h <= 1e5, 1.28 * np.exp(-(29 * 1.667e-27 * 9.80665 * h) / (1.38e-23 * 273)), 0),
        np.nan
    )

def sample_line(height=0, angle=np.pi / 2, line=np.linspace(0, 1e6, 100001)):
    x = np.cos(angle) * line
    y = np.sin(angle) * line
    h = np.sqrt((R + height + y)**2 + x**2) - R

    return h

def kapparho(height=0, angle=np.pi / 2, line=np.linspace(0, 1e6, 100001)):
    heights = sample_line(height, angle, line)

    return density(heights)

def taux(height=0, angle=np.pi / 2, distance=1e6):
    taus = np.sum(kapparho(height, angle, np.linspace(0, distance, 1000001))) / 1000001 * distance
    return np.sum(taus)


def plotto(height=0, angle=np.pi / 2, max_distance=1e6):
    line = np.linspace(0, 1e6, 1000001)

    print(taux(2634, -np.pi/ 2, 2634) / taux(0, np.radians(90), 1e6))

    return
    plt.plot(line, sample_line(0, np.radians(0), line))
    plt.show()

    for angle in np.linspace(np.radians(-2), np.radians(0), 21):
        plt.plot(line, kapparho(2634, angle, line=line))
    plt.show()

    norm = np.sum(kapparho(0, np.pi / 2, line))
    for angle in np.linspace(np.radians(-2), np.radians(0), 21):
        plt.plot(line, np.cumsum(kapparho(2634, angle, line=line)) / norm)
    plt.show()


def main():
    plotto(0)


main()
