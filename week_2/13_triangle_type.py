a, b, c = int(input()), int(input()), int(input())
if a + b <= c or a + c <= b or b + c <= a or a == b == c == 0:
    print("impossible")
elif a ** 2 + b ** 2 == c ** 2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("rectangular")
elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
    print("obtuse")
elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
    print("acute")
