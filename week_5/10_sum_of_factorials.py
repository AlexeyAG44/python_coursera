# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.

import math
n = int(input())
print(sum(map(math.factorial, list(range(1, n + 1)))))
