def exp(a1, n1):
    if n1 == 0:
        return 1
    if n1 == 1:
        return a1
    elif n1 % 2 == 0:
        return (a1 ** 2) ** (n1 / 2)
    elif n1 % 2 != 0:
        return a1 * (a1 ** (n1 - 1))


a = float(input())
n = int(input())
print(exp(a, n))
