# Проверьте, есть ли среди данных N чисел нули.
# Вводится число N, а затем N чисел.
# Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.

# решение подглядел, не допер что ввод можно впихнуть в лямбду
print(any(map(lambda x: int(input()) == 0, range(int(input())))))

# мое решение
b = 0
for i in range(int(input())):
    b = any(map(lambda x: x == 0, map(int, input())))
print(b)
