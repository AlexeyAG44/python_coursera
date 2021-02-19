# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.

rub = int(input())
penny = int(input())
n = int(input())
penny1 = (penny * n) // 100
penny2 = (penny * n) % 100
rub2 = rub * n + penny1
print(rub2, penny2)
