# Дано положительное действительное число X. Выведите его дробную часть.

x = float(input())
d = x // 1
fp = x - d
print('{0:.6f}'.format(fp).rstrip('0').rstrip('.'))
