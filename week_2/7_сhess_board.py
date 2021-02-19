# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES,
# а если в разные цвета – то NO.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a + b) % 2) == ((c + d) % 2):
    print("YES")
else:
    print("NO")
