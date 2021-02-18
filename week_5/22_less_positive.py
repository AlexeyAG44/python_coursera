numList = list(map(int, input().split()))
resNumList = []
current = numList[0]
for current in numList:
    if current > 0:
        resNumList.append(current)
print(min(resNumList))
