import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[12, 2, 1]])
print(np.linalg.det(A))
C = np.concatenate((A, B.T), axis=1)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(C))



A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[4, 7, 10]])
print(np.linalg.det(A))
C = np.concatenate((A, B.T), axis=1)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(C))
print(C)

x = np.linspace(-20, 20, 201)
z_1 = -2 - x
z_2 =( - 8 - 4*x) / 4


plt.plot(x, z_1)
plt.plot(x, z_2)
plt.xlabel('z')
plt.ylabel('y, x')
plt.grid(True)
plt.show()
