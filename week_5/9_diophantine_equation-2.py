# Даны числа a, b, c, d, e.
# Подсчитайте количество таких целых чисел от 0 до 1000 (включительно),
# которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
for x in range(0, 1001):
    equation = (a * x ** 3 + b * x ** 2 + c * x + d)
    if equation == 0 and x != e:
        count += 1
print(count)
