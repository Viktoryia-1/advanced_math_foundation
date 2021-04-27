import numpy as np
from math import factorial
k, n = 0, 4
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + g + d
for el in x:
    if el == 2:
        k += 1

c = factorial(n) / factorial(2)*factorial(n-2)
print(c)
# Не уверена здесь в рассчетах. Как мы должны рассчитывать? При 0,5 выпадения орла и решки
# вероятность получается 1,5. Считала исходя из восьми результатов для 4 испытаний.
# Вероятность выпадения орла и решки в одинаковом количестве 1/8,
# это и поставила в формулу. Для небольших значений работает.
# Для 20 испытаний выдает уже какие-то дикие числа.
# При 100 испытаниях не рассчитывает с, выдает ошибку
result = c * 0.125**2 * 0.875**(n-2)
print(f"Oрел и решка в одинаковых количествах выпали по {k} раз,\
 количество испытаний {n}, результат {k/n}")
print(result)

# Повторите расчеты биномиальных коэффициентов и вероятностей k успехов
# в последовательности из n независимых испытаний, взяв другие значения n и k.

k, n = 0, 4
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + g + d
for el in x:
    if el == 2:
        k += 1

c = factorial(n) / factorial(3)*factorial(n-3)
print(c)
result = c * 0.125**3 * 0.875**(n-3)


print(f"Oрел и решка в одинаковых количествах выпали по {k} раз,\
 количество испытаний {n}, результат {k/n}")
print(result)
# Здесь изменила значение n до десяти и получила вероятность 500
# Пожалуйста поясните, где мой код свернул не туда.
k, n = 0, 10
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + g + d
for el in x:
    if el == 2:
        k += 1

c = factorial(n) / factorial(4)*factorial(n-4)
print(c)
result = c * 0.05**4 * 0.95**(n-4)


print(f"Oрел и решка в одинаковых количествах выпали по {k} раз,\
 количество испытаний {n}, результат {k/n}")
print(result)




