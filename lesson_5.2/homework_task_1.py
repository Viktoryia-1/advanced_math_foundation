import numpy as np
a = np.random.uniform(0, 37)
a = int(a)
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
if a in black_numbers:
    print(f"We have a black number {a}!")
elif a in red_numbers:
    print(f"We have a red number {a}!")
else:
    print(f"It's a zero!")