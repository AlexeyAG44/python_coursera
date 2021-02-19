# Даны координаты двух точек на плоскости, требуется определить,
# лежат ли они в одной координатной четверти или нет
# (все координаты отличны от нуля).

x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
k = (x > 0 and y > 0) and (x1 > 0 and y1 > 0)
k1 = (x < 0 and y < 0) and (x1 < 0 and y1 < 0)
k2 = (x < 0 and y > 0) and (x1 < 0 and y1 > 0)
k3 = (x > 0 and y < 0) and (x1 > 0 and y1 < 0)
if (k or k1) or (k2 or k3):
    print("YES")
else:
    print("NO")
