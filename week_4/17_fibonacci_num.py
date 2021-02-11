def phib(n):
    if n == 1 or n == 2:
        return 1
    else:
        res = phib(n - 1) + phib(n - 2)
        return res


i = int(input())
print(phib(i))
