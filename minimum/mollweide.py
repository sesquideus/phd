import numpy as np

from sklearn.neighbors import KernelDensity

from matplotlib import pyplot as plt

fig = plt.figure()
plt.subplot(111, projection="mollweide")

BG_COUNT = 10000
COUNT1 = 100

phi = np.concatenate((
    np.array(np.radians(np.random.uniform(-180, 180, size=BG_COUNT))),
    np.array(np.radians(np.random.normal(70, 3, size=COUNT1))),
    np.array(np.radians(np.random.normal(-140, 4, size=300))),
    np.array(np.radians(np.random.normal(-40, 10, size=500))),
))
theta = np.concatenate((
    np.array(np.arcsin(np.random.uniform(-0.999, 0.999, size=BG_COUNT))),
    np.array(np.radians(np.random.normal(-50, 2, size=COUNT1))),
    np.array(np.radians(np.random.normal(38, 3, size=300))),
    np.array(np.radians(np.random.normal(5, 10, size=500))),
))
speed = np.concatenate((
    np.random.pareto(1.8, size=BG_COUNT) * 10000,
    np.random.normal(44400, 550, size=COUNT1),
    np.random.normal(24100, 230, size=300),
    np.random.normal(59000, 100, size=500),
))

xgrid = np.linspace(-np.pi, np.pi, 360)
ygrid = np.linspace(-np.pi / 2, np.pi / 2, 180)
X, Y = np.meshgrid(xgrid, ygrid)

xy = np.vstack([Y.ravel(), X.ravel()]).T

kde = KernelDensity(bandwidth=0.1, metric='haversine', kernel='gaussian', algorithm='ball_tree', rtol=1e-12)
coord = np.vstack([theta, phi]).T

print("Fitting...")
kde.fit(coord)

print("Evaluating...")
z = np.exp(kde.score_samples(xy))
z = z.reshape(X.shape)

print("Plotting...")
plt.contourf(X, Y, z, levels=np.linspace(0, z.max(), 100), cmap='Blues')
plt.scatter(phi, theta, (speed / 1000), np.log(speed), marker='.')
plt.grid()
plt.tight_layout()
plt.show()
fig.savefig('example.png')
