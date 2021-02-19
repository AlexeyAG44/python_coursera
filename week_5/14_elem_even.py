# Вводится список чисел. Все числа списка находятся на одной строке.

numList = list(map(int, input().split()))
for i in numList:
    if i % 2 == 0:
        print(i, end=' ')
