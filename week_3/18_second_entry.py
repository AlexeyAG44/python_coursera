# Дана строка.
# Найдите в этой строке второе вхождение буквы f и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2.
# При решении этой задачи нельзя использовать метод count.

string = str(input())
sub_string = "f"
first = string.find(sub_string)
string_1 = string[first+1:]
second = string_1.find(sub_string)
if second != -1:
    print(first + second + 1)
elif first == -1:
    print(-2)
else:
    print(-1)
