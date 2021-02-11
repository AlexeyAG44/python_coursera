a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif c * (-b / a) + d != 0 and (int(-b / a) == -b / a):
    print(int(-b / a))
else:
    print('NO')
