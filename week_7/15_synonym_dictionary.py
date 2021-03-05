# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.
#
# Формат ввода
#
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два слова-синонима.
# После этого следует одно слово.
#
# Формат вывода
#
# Программа должна вывести синоним к данному слову.
#
# Примечания
#
# Эту задачу можно решить и без словарей (сохранив все входные данные в списке),
# но решение со словарем будет более простым.

n = int(input())
SynDict = {}
for i in range(n):
    line = input()
    first_srt = line[:line.find(' ')].strip()
    second_str = line[line.find(' ') + 1:].strip()
    second = map(lambda s: s.strip(), second_str.split())
    for j in second:
        if j not in SynDict:
            SynDict[j] = []
        SynDict[j].append(first_srt)
word = input()
for keys, [value] in SynDict.items():
    if word == value:
        print(keys)
    elif word == keys:
        print(value)
