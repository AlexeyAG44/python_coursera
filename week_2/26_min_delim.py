n = int(input())
i = 2
x = n % i
if x == 0:
    print(i)
else:
    while x != 0:
        x = n % i
        i = i + 1
    print(i - 1)
