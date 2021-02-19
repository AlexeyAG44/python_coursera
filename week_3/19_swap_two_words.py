# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.

string = str(input())
sub_string = " "
first = string.find(sub_string)
string_1 = string[:first]
string_2 = string[first+1:]
print(string_2, string_1)
