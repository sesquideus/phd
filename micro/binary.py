import numpy as np
from matplotlib import pyplot as plt

RES = 1000
x = np.linspace(-2, 2, 2 * RES)
y = np.linspace(-2, 2, 2 * RES)

mx, my = np.meshgrid(x, y)

q = 6

def g1(x, y):
    return 2 * q * np.sqrt(1 / np.sqrt(x**2 + y**2))

def g2(x, y):
    return 2 * np.sqrt(1 / np.sqrt((x - 1)**2 + y**2))

def rotation(x, y):
    return np.sqrt((x - 1 / (1+q))**2 + y**2)


phi = (g1(mx, my) + g2(mx, my) + 50*rotation(mx, my))
phi[phi > 300] = np.nan
phi = phi.reshape(2*RES, 2*RES)

plt.imshow(np.log(phi))
plt.show()
