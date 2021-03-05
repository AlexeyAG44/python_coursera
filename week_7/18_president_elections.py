# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
#
# Формат ввода
#
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
# Известно, что общее число кандидатов не превосходит 20,
# но в отличии от предыдущих задач список кандидатов явно не задан.
# Читайте данные из файла input.txt с указанием кодировки utf8.
#
# Формат вывода
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.

fileIn = open('input.txt', 'r', encoding='utf-8')
fileOut = open('output.txt', 'w', encoding='utf-8')
input_data = fileIn.readlines()
candidates = dict()
wins = list()
for l in input_data:
    candidates[l] = candidates.get(l, 0) + 1
for l in candidates:
    wins.append((candidates[l], l))
wins = sorted(wins)
if wins[-1][0] > len(input_data) / 2:
    fileOut.writelines(wins[-1][1])
else:
    fileOut.writelines(wins[-1][1])
    fileOut.writelines(wins[-2][1])