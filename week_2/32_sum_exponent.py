# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
i = 0
sum_1 = 0
while i + 1 <= n:
    i = i + 1
    i2 = i ** 2
    sum_1 = sum_1 + i2
print(sum_1)
