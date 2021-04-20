import numpy as np
from matplotlib import pyplot as plt


def morrison(reynolds):
    a = reynolds / 5
    b = reynolds / 263000
    c = reynolds / 1000000

    return 24 / reynolds \
        + 2.6 * a / (1 + a**1.52) \
        + 0.411 * b**-7.94 / (1 + b**-8) \
        + 0.25 * c / (1 + c)

def morrison_mod(re):
    a = re / 5
    b = re / 263000

    return 24 / re \
        + 2.6 * a / (1 + a**1.52) \
        + 0.411 * b**-7.94 / (1 + b**-8) \
        + re**0.8 / 461000

def kelessidis(re):
    return 24 / re * (1 + 0.1466 * re**0.378) + 0.44 / (1 + 0.2635 / re)

def reynolds_number(length, speed, density):
    return length * speed * density / constants.AIR_VISCOSITY


xs = 10**np.linspace(-5, 7, 1201)

plt.plot(xs, kelessidis(xs))
plt.plot(xs, morrison(xs))
plt.plot(xs, morrison_mod(xs))
plt.loglog()
plt.show()
