src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
nums_1 = set()
nums_2 = set()
for el in src:
    if el in nums_1:
        nums_2.add(el)
        nums_1.discard(el)
    elif el not in nums_2:
        nums_1.add(el)
print(*nums_1)