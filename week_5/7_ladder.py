# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.

num = int(input())
i = 1
if 0 <= num <= 9:
    while i <= num:
        for i in range(1, num + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()
        i += 1
