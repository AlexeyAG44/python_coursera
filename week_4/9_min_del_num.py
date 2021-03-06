# Дано натуральное число n>1.
# Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.
#
# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n.
# А у всех составных чисел обязательно есть делители,
# отличные от единицы и не превосходящие корня из n.

import math


def MinDivisor(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > math.sqrt(n):
            return n
    return i


x = int(input())
print(MinDivisor(x))
