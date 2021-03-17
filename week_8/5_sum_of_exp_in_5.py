# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.
# Для решения задачи используйте функцию reduce из модуля functools

import functools
print(
    functools.reduce(
        lambda x, y: x * y,
        list(
            map(
                lambda x: x ** 5,
                map(int, input().split())
            )
        )
    )
)
