scr = list(map(int, input('Введите числа: ').split()))
ans = [scr[i] for i in range(1, len(scr)) if scr[i] > scr[i - 1]]
print(*ans)
