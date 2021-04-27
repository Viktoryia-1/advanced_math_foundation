from itertools import permutations, combinations
count = 0
for p in permutations("012345", 2):
    print("".join(str(x) for x in p))
    count += 1

print(f"всего размещений {count}")

count_2 = 0
for p in permutations("01234567", 3):
    print("".join(str(x) for x in p))
    count_2 += 1

print(f"всего размещений {count_2}")

count_3 = 0
for x in combinations("012345", 2):
    print("".join(x))
    count_3 += 1

print(f"всего сочетаний {count_3}")

count_4 = 0
for x in combinations("01234567", 4):
    print("".join(x))
    count_4 += 1

print(f"всего сочетаний {count_4}")
