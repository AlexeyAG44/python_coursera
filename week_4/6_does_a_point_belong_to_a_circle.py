def IsPointInCircle(x1, y1, xc1, yc1, r1):
    return r1 ** 2 >= (y1 - yc1) ** 2 + (x1 - xc1) ** 2


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
