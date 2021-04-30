import numpy as np
A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([2, 5, 1])
X = np.linalg.solve(A, B)
print(X)