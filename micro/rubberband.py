import numpy as np
from matplotlib import pyplot as plt

s = 16
n = 2**s + 1
x = np.linspace(0, 1, n)

def cauliflower(u):
    y = np.zeros(n, dtype=float)
    y[-1] = 1
    compute(u, y, 0, n - 1)
    return y

def compute(x, y, low, up):
    if low + 1 == up:
        return
    else:
        mid = (low + up) // 2
        y[mid] = y[low] + x * (y[up] - y[low])
        compute(x, y, low, mid)
        compute(x, y, mid, up)

xx = np.linspace(0, 0.5, 51)

for u in xx:
    plt.plot(x, x - cauliflower(u))
plt.show()
