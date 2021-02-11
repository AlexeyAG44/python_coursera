import math


def IsPointInSquare(x1, y1):
    return 1 < (math.sqrt(x1 ** 2) + math.sqrt(y1 ** 2))


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("NO")
else:
    print("YES")
