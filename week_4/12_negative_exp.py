def power(a1, n1):
    an = 1
    for i in range(abs(n1)):
        an *= a1
    if n1 >= 0:
        return an
    else:
        return 1 / an


a = float(input())
n = int(input())
print('{0:.6f}'.format(power(a, n)).rstrip('0').rstrip('.'))
