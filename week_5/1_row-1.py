# 1 способ
a = int(input())
b = int(input())
while a <= b:
    print(a, end=" ")
    a += 1

# 2 способ
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i, end=" ")
