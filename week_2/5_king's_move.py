a = int(input())
b = int(input())
c = int(input())
d = int(input())
e1 = (c == a + 1) or (c == a - 1) or a == c
e2 = (d == b + 1) or (d == b - 1) or b == d
if e1 and e2:
    print("YES")
else:
    print("NO")
