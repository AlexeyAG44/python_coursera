import math
a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
if d >= 0:
    cor = math.sqrt(d)
    x1 = ((-b) + cor) / (2 * a)
    x2 = ((-b) - cor) / (2 * a)
    form1 = ('{0:.6f}'.format(x1).rstrip('0').rstrip('.'))
    form2 = ('{0:.6f}'.format(x2).rstrip('0').rstrip('.'))
    if form1 == form2:
        print(form1)
    elif x1 >= x2:
        print(form2, form1)
    elif x2 >= x1:
        print(form1, form2)
else:
    print()
