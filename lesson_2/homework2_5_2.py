import numpy as num
import matplotlib.pyplot as mat
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
fig = figure()
ax = Axes3D(fig)
x = num.arange(-5, 5, 0.5)
y = num.arange(-5, 5, 0.5)
x, y = num.meshgrid(x, y)
z = x ** 2 - y ** 2
ax.plot_surface(x, y, z)
ax.scatter(0, 0, 0, "z", 50, "red")
show()