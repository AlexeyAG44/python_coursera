import math


def distance(x1, y1, x2, y2):
    xy = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if xy < 0:
        xy = xy * -1
        dis = '{0:.5f}'.format(math.sqrt(xy)).rstrip('0').rstrip('.')
        dis = dis * -1
    else:
        dis = '{0:.5f}'.format(math.sqrt(xy)).rstrip('0').rstrip('.')
    return dis


xa = float(input())
ya = float(input())
xb = float(input())
yb = float(input())
print(distance(xa, ya, xb, yb))
