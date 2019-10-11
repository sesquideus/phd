#!/usr/bin/env python

import argparse

import numpy as np
import pandas
from scipy.stats import norm
from matplotlib import pyplot
from matplotlib.ticker          import ScalarFormatter

def lightCurve(x):
    raw = np.zeros(len(x))
    for u in range(0, 20):
        a = np.random.uniform(1, 10) * norm(loc = np.random.uniform(1.5, 2.5), scale = np.random.uniform(0.01, 0.2)).pdf(x)
        raw += a

    noise = 20 * np.random.normal(0, 0.3, size = 5000)
    return np.maximum(0, raw + noise + 1)

def kernel(x, a):
    return np.exp(-a * x) * a

def eye(data, kernel):
    return (np.convolve(data, kernel, mode = 'full') / 1000)[:5000]

def plotLightCurve():
    figure, axes = emptyPlot()

    x = np.arange(0, 5, 0.001)
    data = lightCurve(x)
    human = eye(data, kernel(x, 20))
    humanLazy = eye(data, kernel(x, 10))
    humanHelboj = eye(data, kernel(x, 5))

    axes.bar(x, data, width = 0.001, color = 'gray')
    axes.plot(x, human)
    axes.plot(x, humanLazy)
    axes.plot(x, humanHelboj)

    figure.savefig('out.png', dpi = 300)
    
def emptyPlot():
    pyplot.rcParams['font.family'] = "Minion Pro"
    pyplot.rcParams['mathtext.fontset'] = "dejavuserif"
    pyplot.rcParams["axes.formatter.useoffset"] = False
    figure, axes = pyplot.subplots()
    figure.tight_layout(rect = (0.07, 0.05, 1, 0.97))
    figure.set_size_inches(8, 5)
    axes.grid(linewidth = 0.2, linestyle = ':')
    axes.xaxis.set_major_formatter(ScalarFormatter(useOffset = False))
    axes.yaxis.set_major_formatter(ScalarFormatter(useOffset = False))

    return figure, axes


def main():
    plotLightCurve()

main()
