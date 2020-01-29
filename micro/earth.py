import math

G = 6.674e-11
M = 5.97e24
R = 6371000

layers = [0, 1.2215e6, 3.48e6, 3.63e6, 5.701e6, 5.771e6, 5.971e6, 6.151e6, 6.3466e6, 6.356e6, 6.368e6, 6.371e6]

def gravity_linear(r):
    return -G*M*r / (R**3)

def integral(i, a, b, c, r):
    if r < layers[i - 1]:
        return 0
    d = layers[i - 1]
    u = min(r, layers[i])
    return math.pi * (4/5 * a * (u**5 - d**5) + b * (u**4 - d**4) + 4/3 * c * (u**3 - d**3))

def mass_PREM(r):
    mass = 0
    mass += integral(1, -2.1773e-10, 1.911e-8, 1.3088e4, r)
    mass += integral(2, -2.4123e-10, 1.3976e-4, 1.2346e4, r)
    mass += integral(3, 0, -5.0007e-4, 7.3067e3, r)
    mass += integral(4, -3.0922e-11, -2.4441e-4, 6.7823e3, r)
    mass += integral(5, 0, -2.3286e-4, 5.3197e3, r)
    mass += integral(6, 0, -1.2603e-3, 1.1249e4, r)
    mass += integral(7, 0, -5.9706e-4, 7.1083e3, r)
    mass += integral(8, 0, 1.0869e-4, 2.691e3, r)
    mass += integral(9, 0, 0, 2.9e3, r)
    mass += integral(10, 0, 0, 2.6e3, r)
    mass += integral(11, 0, 0, 1.02e3, r)
    return mass

def gravity_PREM(r):
    s = -1 if r > 0 else 1
    return s * G * mass_PREM(abs(r)) / r**2

r = 6371000
dr = 0
dt = 0.001
t = 0
step = 0
gravity = gravity_PREM

while True:
    ddr = gravity(r)
    dr += ddr * dt
    r += dr * dt
    t += dt
    step += 1

    if step % 1000 == 0:
        print(f"t = {t:10.3f} s | {r:14.3f} m, {dr:10.3f} m/s, {ddr:10.6f} m/s²")

