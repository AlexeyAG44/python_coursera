# Даны два четырёхзначных числа A и B.
# Выведите все четырёхзначные числа на отрезке от A до B, запись которых является палиндромом.

a, b = int(input()), int(input())
i2 = 0
for i in range(a, b + 1):
    i2 = str(i)
    if int(i2) == int(i2[::-1]):
        print(i)