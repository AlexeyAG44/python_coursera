# По российский правилам числа округляются до ближайшего целого числа,
# а если дробная часть числа равна 0.5,
# то число округляется вверх. Дано неотрицательное число x,
# округлите его по этим правилам.
# Обратите внимание, что функция round не годится для этой задачи!

import math
n = float(input())
n1 = n // 1
f_p = (n - n1) * 10
if f_p >= 5:
    print(math.ceil(n))
else:
    print(math.floor(n))
