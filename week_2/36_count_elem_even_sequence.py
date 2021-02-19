# Определите количество четных элементов в последовательности, завершающейся числом 0

n = int(input())
count = 0
while n != 0:
    if n % 2 == 0 and n != 0:
        n = int(input())
        count = count + 1
    else:
        n = int(input())
print(count)
