n = int(input())
res = (int(n) % 10)
p = str("korov")
p1 = str("korovy")
p2 = str("korova")
if (5 <= n <= 20) or (5 <= res <= 9) or (res == 0):
    print(str(n), " ", str(p))
elif (2 <= n <= 4) or (2 <= res <= 4):
    print(str(n), " ", str(p1))
elif (n == 1) or (res == 1):
    print(str(n), str(p2))
