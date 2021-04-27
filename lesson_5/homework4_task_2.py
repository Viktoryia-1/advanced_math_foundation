import numpy as np
import matplotlib.pyplot as plt
n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]

x_ = np.sum(x) / len(x)
y_ = np.sum(y) / len(y)


c = np.sum((x[0]-x_)*(y[0]-y_))/np.sqrt((np.sum(x[0]-x_)**2) * (np.sum(y[0]-y_)**2))
c_ = np.corrcoef(x, y)

print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])
print(c)
print(c_)
plt.show()