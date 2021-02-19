# Определите сумму всех элементов последовательности, завершающейся числом 0.

now = int(input())
count_sum = now
while now != 0:
    now = int(input())
    count_sum = count_sum + now
print(count_sum)
