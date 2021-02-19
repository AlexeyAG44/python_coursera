# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка

numList = list(map(int, input().split()))
max_i = numList.index(max(numList))
min_i = numList.index(min(numList))
numList[max_i], numList[min_i] = numList[min_i], numList[max_i]
print(*numList)
