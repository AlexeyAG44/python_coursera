# Даны произвольные действительные коэффициенты a, b, c.
# Решите уравнение ax²+bx+c=0.

import math
a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
if a == b == 0 and c != 0 or d < 0:
    print(0)
elif a == b == c == 0:
    print(3)
elif d >= 0 and a != 0:
    cor = math.sqrt(d)
    x1 = ((-b) + cor) / (2 * a)
    x2 = ((-b) - cor) / (2 * a)
    form1 = ('{0:.6f}'.format(x1).rstrip('0').rstrip('.'))
    form2 = ('{0:.6f}'.format(x2).rstrip('0').rstrip('.'))
    if form1 == form2:
        print(1, form1)
    elif form1 >= form2:
        print(2, form2, form1)
    elif form2 >= form1:
        print(2, form1, form2)
elif a == 0:
    print(1, -c / b)
