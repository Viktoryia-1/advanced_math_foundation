# Постройте на одном графике две кривые y(x) для функции двух переменных y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1.
import matplotlib.pyplot as mat
import numpy as num

x = num.linspace(0, 10, 400)


def cos(k):
    return num.cos(x * k)


mat.plot(x,  cos(1))
mat.plot(x,  cos(3))
mat.show()