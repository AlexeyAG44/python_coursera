def Cnk(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return Cnk(n - 1, k) + Cnk(n - 1, k - 1)
    else:
        return n


n1 = int(input())
k1 = int(input())
print(Cnk(n1, k1))
