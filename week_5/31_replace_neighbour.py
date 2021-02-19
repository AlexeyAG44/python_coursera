# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

numList = list(map(int, input().split()))
numListLen = len(numList)
resNumList = []
for index in range(len(numList) - 1):
    if index % 2 == 0:
        resNumList.append(numList[index + 1])
        resNumList.append(numList[index])
if len(numList) % 2 != 0:
    resNumList.append(numList[-1])
print(*resNumList)
