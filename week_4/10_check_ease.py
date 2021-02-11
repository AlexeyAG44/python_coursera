import math


def IsPrime(n):
    if n >= 2:
        if n == 2:
            return n
        i = 2
        k = math.sqrt(n)
        if n % 2 != 0:
            while n % i != 0:
                if k >= i:
                    i += 1
                else:
                    return n


num = int(input())
if IsPrime(num):
    print("YES")
else:
    print("NO")
