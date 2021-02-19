# Дана строка.
# Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз,
# выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.
# При решении этой задачи нельзя использовать метод count и циклы.

string = str(input())
sub_string = "f"
first = string.find(sub_string)
last = string.rfind(sub_string)
if first != -1 and last != -1:
    if first == last:
        print(first)
    else:
        print(first, last)
else:
    print()
