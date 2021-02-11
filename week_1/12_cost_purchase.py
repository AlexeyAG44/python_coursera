rub = int(input())
penny = int(input())
n = int(input())
penny1 = (penny * n) // 100
penny2 = (penny * n) % 100
rub2 = rub * n + penny1
print(rub2, penny2)
