import numpy as np
from scipy import optimize

a = np.array([1890.37, 2857.45, 627])
b = np.array([0, 0, 278])
c = np.array([1519.34, 440.57, 206])

ab = 1442
ac = 1004.4
bc = 914.5

def length(v):
    return np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def angle(x, p, y):
    return np.arccos(np.dot(x - p, y - p) / (length(x - p) * length(y - p)))

def evaluate(p):
    p = np.array(p)
    return (ab / ac - angle(a, p, b) / angle(a, p, c))**2 + (bc / ac - angle(b, p, c) / angle(a, p, c))**2 + (bc / ab - angle(b, p, c) / angle(a, p, b))**2

r = optimize.minimize(evaluate, method='Nelder-Mead', x0=[120000, -350000, 400000])
print(r)
