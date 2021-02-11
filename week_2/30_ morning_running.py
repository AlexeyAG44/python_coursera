x = int(input())
y = int(input())
i = 1
g = x * 0.1
while x < y:
    x = x + g
    i = i + 1
    g = x * 0.1
print(i)
