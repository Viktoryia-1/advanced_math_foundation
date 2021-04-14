from math import sqrt
vector_1 = [10, 10, 10]
vector_2 = [0, 0, -10]
vector_3 = [a + b for a, b in zip(vector_1, vector_2)]
print(vector_3)

sqrt_result = [el**2 for el in vector_3]
print(sqrt_result)
final_length = sqrt(sum(sqrt_result))
print(final_length)

