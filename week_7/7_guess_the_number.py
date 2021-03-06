# Август и Беатриса играют в игру.
# Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ею чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август.
#
# Формат ввода
#
# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.
#
# Формат вывода
#
# Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.

August_List = list(range(1, int(input()) + 1))
Beatrice_Answer = input()
Result_Set = set()
while Beatrice_Answer != "HELP":
    Answer = str(input())
    if Answer == "YES":
        Beatrice_List = list(map(int, Beatrice_Answer.split()))
        August_List = list(set(August_List) & set(Beatrice_List))
    elif Answer == "NO":
        Beatrice_List = list(map(int, Beatrice_Answer.split()))
        Result_Set |= set(Beatrice_List)
    Beatrice_Answer = input()
August_List = set(August_List)
print(*sorted(list(August_List - Result_Set)))
