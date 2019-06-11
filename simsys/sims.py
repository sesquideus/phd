import argparse
import os
import scipy.stats
import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as pp

def initialize():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

def load(filename):
    return np.loadtxt(filename, dtype = float, skiprows = 3, usecols = (1, 2))

def gauss(x, m, s, c):
    return c * np.exp(-(x - m)**2 / (2*s**2)) / (np.sqrt(2 * np.pi) * s)

def gaussH(x, m, s, h):
    return h * np.exp(-(x - m)**2 / (2*s**2))

def bigauss(x, m1, m2, s1, s2, c1, c2):
    return gauss(x, m1, s1, c1) + gauss(x, m2, s2, c2)

def maxwell(x, m, s, c):
    return c * x**3 * np.exp(-(x - m)**2 / (2*s**2)) / (np.sqrt(2 * np.pi) * s)

def moyal(x, l, s, c):
    return c * scipy.stats.moyal.pdf(x, l, s)

def height(s, c):
    return c / (np.sqrt(2 * np.pi) * s)

def moyal(x, c, mu, sigma):
    return c * np.exp(-0.5 * np.exp(-(x - mu) / sigma) - (x - mu) / (2 * sigma)) / (np.sqrt(2 * np.pi) * sigma)

def bimoyal(x, c1, c2, mu1, mu2, sigma1, sigma2):
    return moyal(x, c1, mu1, sigma1) + moyal(x, c2, mu2, sigma2)

def generate(p1, p2):
    mu1, sigma1, count1 = p1
    mu2, sigma2, count2 = p2

    a1 = np.random.normal(*p1)
    a2 = np.random.normal(*p2)
    low = (mu1 + mu2) / 2 - 5 * (sigma1 + sigma2) / 2
    high = (mu1 + mu2) / 2 + 5 * (sigma1 + sigma2) / 2

    a = np.concatenate([a1, a2])

    h, e = np.histogram(a + 0.25, 100, (2600, 2700))

    popt, pcov = so.curve_fit(bigauss, e[:-1], h, p0 = (2640, 2650, 1, 1, 5000, 5000), xtol = 1e-18)

    m1, m2, s1, s2, c1, c2 = popt

    def bg(x):
        return bigauss(x, m1, m2, s1, s2, c1, c2)

    def g2(x):
        return gauss(x, m2, s2, c2)
    
    def g(x):
        return gauss(x, 2650, 1, 500)
   
    print("Parameters:")
    print("c1 = {:.6f}".format(c1))
    print("m1 = {:.6f}".format(m1))
    print("s1 = {:.6f}".format(s1))
    print("h1 = {:.6f}".format(height(s1, c1)))
    print("-" * 50)
    print("c2 = {:.6f}".format(c2))
    print("m2 = {:.6f}".format(m2))
    print("s2 = {:.6f}".format(s2))
    print("h2 = {:.6f}".format(height(s2, c2)))
    
    pp.hist(a, bins = 100, range = (2600, 2700), align = 'mid')
    pp.plot(e[:-1], bg(e[:-1] - 0.5))
    pp.plot(e[:-1], g1(e[:-1] - 0.5))
    pp.plot(e[:-1], g2(e[:-1] - 0.5))
    #pp.plot(e[:-1], g(e[:-1]))
    pp.show()

def mainA():
    # generate((2633.9, 10, 20000), (2654.4, 10, 20000))
    data = load('mini.dat')
    x, y = np.transpose(data)
    x = x - 106

    popt, pcov = so.curve_fit(bimoyal, x, y,
        bounds = (
            (28.95, 28.95, 0, 0, 0.01, 0.01),
            (29.05, 29.05, 0.5, 0.5, 50, 50)
        ),
        xtol = 1e-9,
        maxfev = 100000
    )

    popt, pcov = fitMoyal(x, y)

    c, mu, sigma = popt

    def f(x):
        return moyal(x, c, mu, sigma)

    #print("Parameters:")
    #print("c1 = {:.6f}".format(c1))
    #print("m1 = {:.6f}".format(m1))
    #print("s1 = {:.6f}".format(s1))
    #print("h1 = {:.6f}".format(height(s1, c1)))
    #print("-" * 50)
    #print("c2 = {:.6f}".format(c2))
    #print("m2 = {:.6f}".format(m2))
    #print("s2 = {:.6f}".format(s2))
    #print("h2 = {:.6f}".format(height(s2, c2)))

    pp.bar(x, y, width = x / 60000)
    #pp.plot(x, g1(x), color = 'yellow')
    #pp.plot(x, g2(x), color = 'orange')
    pp.plot(x, f(x), color = 'red')
    pp.show()

def loadMulti(filename):
    with open(filename, 'r') as f:
        result = []

        for i, line in enumerate(f):
            if i < 3:
                continue
            data = line.rstrip('\n').split('\t')
            result += [float(data[1])] * int(data[2])

    return np.array(result)


def main():
    data = load(os.path.join('data', 'mg.txt'))
    x, y = np.transpose(data)

    data = loadMulti(os.path.join('data', 'mg.txt'))

    popt, pcov = so.curve_fit(moyal, x, y,
        bounds = (
            (0.8, 1e-4, 0.1),
            (1.0, 100, 1000),
        ),
        xtol = 1e-9,
        maxfev = 100000
    )

    l, s, c = popt

    def m(x):
        return moyal(x, l, s, c)
        
    kernel = scipy.stats.gaussian_kde(data)
    space = np.linspace(23.97, 24.01, 1000)

    pp.bar(x, y, width = 0.0005)
    pp.plot(x, m(x), color = 'red')
    pp.plot(space, kernel.evaluate(space) * 7, color = 'cyan')
    pp.show()

main()
