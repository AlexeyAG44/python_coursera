a = int(input())
a1 = a % 4
a2 = a % 400
a3 = a % 100
if (a1 == 0 and a3 != 0) or a2 == 0:
    print("YES")
else:
    print("NO")
