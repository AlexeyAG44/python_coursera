def power(a1, n1):
    if a1 >= 0:
        if n1 == 0:
            return 1
        return a1 * a1 ** (n - 1)


a = float(input())
n = int(input())
print('{0:.6f}'.format(power(a, n)).rstrip('0').rstrip('.'))
