import numpy as num
import matplotlib.pyplot as mat
import math

x = num.linspace(-5, 5, 21)
y = 3*x + 1
y_2 = -1/3 * x + 1
mat.plot(x, y)
mat.plot(x, y_2)
# Приводим при помощи данной функции оси x и y к единой шкале?
# Прочитала в документации, но плохо понимаю, как это работает.
mat.axis('equal')
mat.show()
