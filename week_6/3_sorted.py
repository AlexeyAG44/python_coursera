# Отсортируйте данный массив, используя встроенную сортировку.
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10⁵.
# Далее идет N целых чисел, не превосходящих по абсолютной величине 10⁹.

n = int(input())
numList = list(map(int, input().split()[:n]))
newNumList = []
for i in range(n, 100):
    newNumList.append(numList)
print(newNumList)
