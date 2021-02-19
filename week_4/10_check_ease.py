# Дано натуральное число n>1.
# Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO,
# если число составное. Решение оформите в виде функции IsPrime(n),
# которая возвращает True для простых чисел и False для составных чисел.
# Программа должна иметь сложность O(корень из n):
# количество действий в программе должно быть пропорционально квадратному корню из n
# (иначе говоря, при увеличении входного числа в k раз,
# время выполнения программы должно увеличиваться примерно в корень из k раз).

import math


def IsPrime(n):
    if n >= 2:
        if n == 2:
            return n
        i = 2
        k = math.sqrt(n)
        if n % 2 != 0:
            while n % i != 0:
                if k >= i:
                    i += 1
                else:
                    return n


num = int(input())
if IsPrime(num):
    print("YES")
else:
    print("NO")
