num = int(input())
i = 1
while i <= num:
    a = 0
    for i in range(1, num + 1):
        a = a + (i ** 2)
    i += 1
    print(a)
