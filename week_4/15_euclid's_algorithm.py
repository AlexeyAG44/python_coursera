def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a1 = int(input())
b1 = int(input())
print(gcd(a1, b1))

# Рекурсия:
#def gcd(a, b):
#    if b == 0:
#        return a
#    a = a % b
#    elif a == 0:
#        return b
#    return gcd(b, a)