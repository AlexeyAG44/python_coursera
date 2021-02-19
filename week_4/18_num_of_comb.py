# По данным целым числам n и k  (0≤k≤n) вычислите C из n по k.
#
#  Решение оформите в виде функции C(n, k).
#
# Для решения используйте рекуррентное соотношение:
#
# Cnk = Cn-1k + Cn-1k-1
#
# И равенства:
#
# С(n, 1)=n
#
# C(n, n)=1

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
