import numpy as np
from coord import Vector3D

a = Vector3D(48.1649296, 17.0605933, 242.3037578)
b = Vector3D(48.1819935, 17.0938382, 442.2726772)
c = Vector3D(48.1546859, 17.0876735, 274.7232364)
d = Vector3D(48.1585922, 17.0789262, 229.9943608)
e = Vector3D(48.1675208, 17.0911456, 228.6059778)
f = Vector3D(48.1730563, 17.0719448, 190.2051344)

x = (f - a) ^ (b - a)
y = (d - a) ^ (c - a)
z = (e - b) ^ (c - b)

A = np.array([x.np(), y.np(), z.np()])

k = np.dot(x.np(), a.np())
l = np.dot(y.np(), d.np())
m = np.dot(z.np(), b.np())

print(k, l, m)

B = np.array([k, l, m])
print(A, B)
f = np.linalg.solve(A, B)
print(f)

position = Vector3D.from_numpy_vector(f)
print(position)
