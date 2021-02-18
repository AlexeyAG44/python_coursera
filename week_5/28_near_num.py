len_list = int(input())
numList = list(map(int, input().split()))
resNumList = []
num = int(input())
res = 0
for i in numList[:len_list]:
    m = abs(num - i)
    b = resNumList.append(m)
    i_min = min(resNumList)
    res = numList[resNumList.index(i_min)]
print(res)
