# Даны длины сторон треугольника. Вычислите площадь треугольника.

import math
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('{0:.6f}'.format(s).rstrip('0').rstrip('.'))
