# Если точка принадлежит области (область включает границы),
# выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y),
# возвращающую True, если точка принадлежит области и False,
# если не принадлежит. Основная программа должна считать координаты точки,
# вызвать функцию IsPointInArea и в зависимости от возвращенного значения
# вывести на экран необходимое сообщение.
# Функция IsPointInArea не должна содержать инструкцию if.
# В задаче подразумевается, что нижняя область продолжается вниз  бесконечно
# (картинка может ввести в заблуждение,
# как будто область  заканчивается на y = -3.5).
# Т.е. например для ввода

import math


def isPointInArea(x, y):
    xy1 = (y - 0) - (x + 1) * 2
    xy2 = (y - 1) - (x + 1) * (-1)
    c = math.sqrt((((-1) - x) ** 2 + (1 - y) ** 2))
    if xy1 >= 0 and xy2 >= 0 and c <= 2 or xy1 <= 0 and xy2 <= 0 and c >= 2:
        return x, y


xx, yy = float(input()), float(input())
if isPointInArea(xx, yy):
    print("YES")
else:
    print("NO")
