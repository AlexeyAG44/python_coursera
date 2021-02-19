# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.

numList = list(map(int, input().split()))
resNumList = []
current = numList[0]
for current in numList:
    if current > 0:
        resNumList.append(current)
print(min(resNumList))
