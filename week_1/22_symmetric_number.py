x = int(input())
x1 = x // 1000
x2 = x // 100 % 10
x3 = x // 10 - x1 * 100 - x2 * 10
x4 = x % 10
y1 = (x1 - x4) ** 2
y2 = (x2 - x3) ** 2
print(y1 + y2 + 1)
