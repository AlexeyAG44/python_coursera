# Даны два списка, упорядоченных по возрастанию
# (каждый список состоит из различных элементов).
# Найдите пересечение множеств элементов этих списков,
# то есть те числа, которые являются элементами обоих списков.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Решение оформите в виде функции Intersection(A, B).
# Функция должна возвращать список пересечения данных списков в порядке возрастания элементов.
# Модифицировать исходные списки запрещается.

def Intersection(a, b):
    count_a = 0
    count_b = 0
    c = []
    while count_a < len(a) and count_b < len(b):
        if a[count_a] == b[count_b]:
            c.append(a[count_a])
            count_a += 1
            count_b += 1
        elif a[count_a] > b[count_b]:
            count_b += 1
        elif a[count_a] < b[count_b]:
            count_a += 1
    return c


numList1 = list(map(int, input().split()))
numList2 = list(map(int, input().split()))
print(*Intersection(numList1, numList2))
