a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
a2 = a // a1
b2 = b // b1
c2 = c // c1

if a2 == 0 or b2 == 0 or c2 == 0:
    n2 = a2 * b2 * c2
    print(n2)
else: #b <= a % a1 or a <= b % b1:
    n = (a2 // b) * (b2 // a) * c2
    print(n)

