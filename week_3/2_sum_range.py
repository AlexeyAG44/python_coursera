# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).

a = int(input())
count_sum = 1
sum_range1 = 0
while count_sum <= a:
    sum_range = (1 / (count_sum ** 2))
    sum_range1 = sum_range1 + sum_range
    count_sum = count_sum + 1
print('{0:.5f}'.format(sum_range1).rstrip('0').rstrip('.'))
