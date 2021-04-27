# Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы  +х1+ …+ х9.
import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.randint(1, 10, 5)
x2 = np.random.randint(1, 10, 5)
x3 = np.random.randint(1, 10, 5)
x4 = np.random.randint(1, 10, 5)
x5 = np.random.randint(1, 10, 5)
x6 = np.random.randint(1, 10, 5)
x7 = np.random.randint(1, 10, 5)
x8 = np.random.randint(1, 10, 5)
x9 = np.random.randint(1, 10, 5)
x10 = np.random.randint(1, 10, 5)

result = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10
print(result)
bins = 10
result, bins, patches = plt.hist(result, bins)
plt.xlabel('max = 100')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

