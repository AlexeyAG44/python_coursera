import math


def isPointInArea(x, y):
    xy1 = (y - 0) - (x + 1) * 2
    xy2 = (y - 1) - (x + 1) * (-1)
    c = math.sqrt((((-1) - x) ** 2 + (1 - y) ** 2))
    if xy1 >= 0 and xy2 >= 0 and c <= 2 or xy1 <= 0 and xy2 <= 0 and c >= 2:
        return x, y


xx, yy = float(input()), float(input())
if isPointInArea(xx, yy):
    print("YES")
else:
    print("NO")
