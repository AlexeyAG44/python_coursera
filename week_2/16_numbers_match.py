a, b, c = int(input()), int(input()), int(input())
if a != b and a != c and b != c:
    print(0)
elif a == b and a == c and b == c:
    print(3)
else:
    print(2)
