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
