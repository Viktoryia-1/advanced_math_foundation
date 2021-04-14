import numpy as num
import matplotlib.pyplot as mat
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
fig = figure()
ax = Axes3D(fig)
x = num.arange(-10, 10, 0.5)
y = num.arange(-10, 10, 0.5)
x, y = num.meshgrid(x, y)
z = num.sqrt(x**2 + y**2 + 1)
# Хотела построить элиипсоид, вывела z по формуле. На выходе получила какую-то ерунду.
# Когда разделила ерунду на 100, она стала напоминать половину эллипсоида
#z = num.sqrt(1 - (x**2 + y**2)/100 )
ax.set_aspect("auto")
ax.plot_wireframe(x, y, z)
ax.scatter(0, 0, 0, "z", 50, "red")
show()