numList = list(map(int, input().split()))
resNumList = []
current = numList[0]
previous = current
for current in numList:
    if current > previous:
        resNumList.append(current)
        previous = current
    else:
        previous = current
print(*resNumList)
