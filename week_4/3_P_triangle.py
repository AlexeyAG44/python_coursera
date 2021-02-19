# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу,
# вычисляющую периметр треугольника по координатам трех его вершин.

import math


def distance(x1, y1, x2, y2):
    xy = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if xy < 0:
        xy = xy * -1
        dis = math.sqrt(xy)
        dis = dis * -1
    else:
        dis = math.sqrt(xy)
    return dis


x11 = int(input())
y11 = int(input())
x22 = int(input())
y22 = int(input())
x33 = int(input())
y33 = int(input())
a = float(distance(x11, y11, x22, y22))
b = float(distance(x22, y22, x33, y33))
c = float(distance(x11, y11, x33, y33))
p = a + b + c
print('{0:.6f}'.format(p).rstrip('0').rstrip('.'))
