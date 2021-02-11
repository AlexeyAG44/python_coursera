import math
n = float(input())
n1 = n // 1
f_p = (n - n1) * 10
if f_p >= 5:
    print(math.ceil(n))
else:
    print(math.floor(n))
