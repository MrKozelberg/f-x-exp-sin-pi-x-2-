import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

N = 10000
num_bins = 10

print('Start plotting...')

fig = plt.figure(figsize=(5, 4)) # width x height, in inches
ax = fig.add_subplot(111)

x = np.random.rand(N)
y = np.e * np.random.rand(N)
x = x[np.exp(np.sin(np.pi * x * x)) > y]

xx = np.linspace(0, 1, len(x))
yy = np.exp(np.sin(np.pi * xx * xx)) * N /(np.e * num_bins)

ax.plot(xx, yy, 'r--')
ax.hist(x, bins = num_bins)
ax.set_xlabel(r'$x$')
fig.savefig('graph.png')
print('...done!')
