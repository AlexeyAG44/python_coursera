a = int(input())
count_sum = 1
sum_range1 = 0
while count_sum <= a:
    sum_range = (1 / (count_sum ** 2))
    sum_range1 = sum_range1 + sum_range
    count_sum = count_sum + 1
print('{0:.5f}'.format(sum_range1).rstrip('0').rstrip('.'))
