import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 2, 201)
plt.plot(x, 10*x-14)
plt.plot(x, -0.3*x - 0.2)
plt.plot(x, 0.4*x - 0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
X = np.linalg.lstsq(A, B)
print(X)