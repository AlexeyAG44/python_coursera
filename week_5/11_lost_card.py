# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.

n = int(input())
count_1 = 0
count_2 = 0
for i in range(1, n + 1):
    count_1 += i
for j in range(1, n):
    k = int(input())
    count_2 += k
print(count_1 - count_2)
