import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-2, 2, 201)
x1 = 1.4 + 0.1*z
x2 = z
x3 = 0.4 + 2.1*x2
x = x1**2 + x2**2 + x3**2
plt.plot(z, x1**2 + x2**2 + x3**2)
plt.xlabel('z')
plt.ylabel('x')
plt.grid(True)
z_min = min(z)
print(z_min)
plt.show()