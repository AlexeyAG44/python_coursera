def min4num(a1, b1, c1, d1):
    return min(min(a1, b1), min(c1, d1))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4num(a, b, c, d))
