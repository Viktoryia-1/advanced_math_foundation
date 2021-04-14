import matplotlib.pyplot as mat
import numpy as num

x = num.linspace(-2 * num.pi, 2 * num.pi, 400)

def cos(x, k, a, b):
    return k * num.cos(x - a) + b


mat.plot(x, cos(x, 3, 4, 1))
mat.plot(x, cos(x, 1, 1, 0.4))
mat.plot(x, cos(x, 2, 1, 3))
mat.show()



