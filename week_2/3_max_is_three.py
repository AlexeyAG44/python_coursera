# Даны три целых числа.
# Найдите наибольшее из них (программа должна вывести ровно одно целое число).
#
# Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

a = int(input())
b = int(input())
c = int(input())
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= c >= b:
    print(c)
