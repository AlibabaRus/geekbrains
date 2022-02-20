n = int(input())
nums_gen = (el for el in range(1, n + 1, 2))
print(*nums_gen)
