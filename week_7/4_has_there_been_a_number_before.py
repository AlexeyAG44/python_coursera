n = list(map(int, input().split()))
mySet = set()
for i in n:
    if i in mySet:
        print('YES')
    else:
        print('NO')
    mySet.add(i)
