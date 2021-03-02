# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').
#
# Входные данные
#
# Строки вида "Фамилия Имя НомерШколы Балл".
#
# Выходные данные
#
# Строки вида "Фамилия Имя Балл", отсортированные по фамилии.

input_file = open('input.txt', 'r', encoding='utf8')
output_file = open('output.txt', 'w', encoding='utf8')
List = []
for i in input_file:
    List.append(i.split())
List.sort()
for now in List:
    now.pop(2)
    print(*now, file=output_file)
input_file.close()
output_file.close()
