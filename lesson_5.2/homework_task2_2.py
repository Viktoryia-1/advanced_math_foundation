import numpy as np
test_count = 0
sum_1 = 0
sum_2 = 0
while test_count != 100:
    a = int(np.random.uniform(0, 100))

    test_count += 1
    if a <= 50:
        sum_1 += 1
    elif a >= 50:
        sum_2 += 1


print(f"Выпадение решки: {sum_1}")
print(f"Выпадение орла: {sum_2}")
print(f"выероятность выпаденя орла и решки равна {sum_1 + sum_2}")