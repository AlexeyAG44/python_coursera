def sum(a1, b1):
    if a1 == 0:
        return b1
    if b1 == 0:
        return a1
    a2 = a1 + 1
    b2 = b1 - 1
    return sum(a2, b2)


a = int(input())
b = int(input())
print(sum(a, b))
