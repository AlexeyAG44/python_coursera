a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
a1 = (a <= e and b <= d) or (b <= e and a <= d)
a2 = (a <= e and c <= d) or (c <= e and a <= d)
a3 = (c <= e and b <= d) or (b <= e and c <= d)
if a1 or a2 or a3:
    print("YES")
else:
    print("NO")
