#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
import scipy.integrate

SIZE = 1000000
M = 5.97e24
G = 6.674e-11
R = 6475000

def impact(v_inf, b):
    try:
        a = - G * M / v_inf**2
        #print(f"a = {a}")
        q = (np.sqrt(G**2 * M**2 + b**2 * v_inf**4) - G * M) / v_inf**2
        #print(f"q = {q}")
        p = b**2 * v_inf**2 / (G * M)
        #print(f"p = {p}")
        e = np.sqrt(1 + p**2 / b**2)
        #print(f"e = {e}")
        t = np.arccos(-1 / e)
        #print(f"t = {t}")

        f = np.arccos((p - R) / (R * e))
        #print(f"f = {f}")

        v_R = np.sqrt(v_inf**2 + 2 * G * M / R)

        rdot = b * v_inf * e * np.sin(f) / p
    except RuntimeWarning:
        pass

    return a, q, p, e, t, f, rdot, v_R

def b_crit(v_inf):
    return np.sqrt(R**2 * v_inf**2 + 2 * G * M * R) / v_inf

def prob():

    v_inf = 1e3

    xs = np.linspace(1, b_crit(v_inf), 100000)
    for v in [1000, 2000, 4000, 6000, 8000, 10000, 15000, 20000, 35000, 50000, 70000, 100000]:
        a, q, p, e, t, f, rdot, v_R = impact(float(v), xs)
        #plt.plot(xs, np.degrees(t - f), color=((np.log10(v) - 3) / 2, 0, 0))
        ys = np.arcsin(rdot / v_R)

        an = np.degrees(ys)[~np.isnan(ys)]
        xs = xs[~np.isnan(ys)]
        ys = ys[~np.isnan(ys)]

        # plt.plot(xs, ys * 2 * np.pi * xs, color=((np.log10(v) - 3) / 2, 1 - (np.log10(v) - 3) / 2, 0))
        plt.plot(an, xs)#, marker='.', s=1)
#    plt.plot(xs, np.arccos(v / v_R * xs / R) - ys)
#    plt.plot(xs, ys, color=((np.log10(v) - 3) / 2, 1 - (np.log10(v) - 3) / 2, 0))

        print(an[np.argmax(ys * 2 * np.pi * xs)])

        #print(np.degrees(
        #    scipy.integrate.trapz(ys * 2 * np.pi * xs, xs) /
        #    scipy.integrate.trapz(2 * np.pi * xs, xs)
        #))
        #print(np.nanmean(y))
    plt.show()

def sim(v):
    cr = b_crit(v)
    print(cr)
    x = np.random.uniform(-cr, cr, size=1000000)
    y = np.random.uniform(-cr, cr, size=1000000)
    b = np.sqrt(x**2 + y**2)
    b = b[b <= cr]
    print(b)
    a, q, p, e, t, f, rdot, v_R = impact(v, b)
    theta = np.degrees(np.arcsin(rdot / v_R))
    print(theta)
    plt.hist(theta, bins=np.linspace(0, 180, 361))

def isim():
    x = np.random.uniform(-1, 1, size=1000000)
    y = np.random.uniform(-1, 1, size=1000000)
    b = np.sqrt(x**2 + y**2)
    b = b[b <= 1]
    x = np.degrees(np.arccos(b))
    plt.hist(x, bins=np.linspace(0, 90, 361), density=True)
    xs = np.linspace(0, 90, 3601)
    plt.plot(xs, np.sin(np.radians(xs * 2)) * np.pi / 180)
    plt.show()


isim()


#x = np.random.uniform(-R*10, R*10, size=SIZE)
#y = np.random.uniform(-R*10, R*10, size=SIZE)
#
#r = np.sqrt(x**2 + y**2)
#r = np.ma.array(r, mask=r > R)
#
#print(r)
#
#c = np.arccos(r)
#
#print(np.degrees(np.mean(c)))
