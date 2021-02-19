# Даны два натуральных числа n и m.
#
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
#
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
#
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).

def gcd(n, m):
    nm = n % m
    if m == 0:
        return n
    elif nm == 0:
        return m
    return gcd(m, nm)


def ReduceFraction(p, q):
    gcd_pq = gcd(p, q)
    if gcd_pq == 1:
        return p, q
    else:
        return ReduceFraction(p // gcd_pq, q // gcd_pq)


p1 = int(input())
q1 = int(input())
print(*ReduceFraction(p1, q1))
