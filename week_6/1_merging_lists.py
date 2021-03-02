# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.

def merge(a, b):
    count_a = 0
    count_b = 0
    c = []
    for i in range(0, len(a) + len(b)):
        if len(a) > count_a and len(b) > count_b:
            if a[i - count_b] > b[i - count_a]:
                c.append(b[i - count_a])
                count_b += 1
            else:
                c.append(a[i - count_b])
                count_a += 1
        else:
            if len(a) > count_a:
                c.extend(a[count_a:])
                break
            else:
                c.extend(b[count_b:])
                break
    return c


a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
print(*merge(a1, b1))

# Решение без пизд*страданий в 3 строчки

a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
print(*sorted(a1 + b1))
