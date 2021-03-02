# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
# каждый из них оценивается целым числом от 0 до 100 баллов.
# При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку)
# по любому экзамену из конкурса выбывают.
# Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
#
# В конкурсе участвует N человек, при этом количество мест равно K.
# Определите проходной балл, то есть такое количество баллов, что количество участников,
# набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов,
# набравших наибольшее количество баллов среди непринятых абитуриентов,
# общее число принятых абитуриентов станет больше K.
#
# Формат ввода
#
# Программа получает на вход количество мест K.
# Далее идут строки с информацией об абитуриентах, каждая из которых состоит из имени
# (текстовая строка содержащая произвольное число пробелов) и трех чисел от 0 до 100, разделенных пробелами.
#
# Используйте для ввода файл input.txt с указанием кодировки utf8
# (для создания такого файла на своем компьютере в программе Notepad++ следует использовать кодировку UTF-8 без BOM).
#
# Формат вывода
#
# Программа должна вывести проходной балл в конкурсе.
# Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
#
# Также возможны две ситуации, когда проходной балл не определен.
#
# Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
#
# Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.
#
# Используйте для вывода файл output.txt с указанием кодировки utf8.
#
# Предупреждение
#
# Пожалуйста, тестируйте файловый ввод и вывод на своем компьютере.
# В этой задаче слушатели часто получают ошибки вроде RE на первом тесте,
# протестировав у себя с помощью консоли и просто заменив input() на чтение из файла перед сдачей.
# К сожалению, такую замену не всегда удается сделать без ошибок,
# и решение слушателей действительно перестает правильно работать даже на первом тесте.

import sys

read = sys.stdin
n = int(read.readline())
marks = []
for line in sys.stdin:
    mark = list(map(int, line.split()[-3:]))
    if min(mark) > 39:
        marks.append(sum(mark))
if len(marks) <= n:
    print(0)
elif marks.count(max(marks)) > n:
    print(1)
else:
    marks.sort(reverse=True)
    nums = marks[:n]
    if nums[-1] == marks[n]:
        while marks[n] in nums:
            nums.remove(marks[n])
    print(min(nums))