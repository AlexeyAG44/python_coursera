# Даны три целых числа A, B, C.
# Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

a, b, c = int(input()), int(input()), int(input())
p1 = (a == b == c)
p2 = (a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
p3 = (a % 2 != 0 and b % 2 != 0 and c % 2 != 0)
if p1 or p2 or p3:
    print("NO")
else:
    print("YES")
