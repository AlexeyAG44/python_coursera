# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.

string = str(input())
sub_string = "h"
first = string.find(sub_string)
last = string.rfind(sub_string)
res = str(string[:first] + string[last+1:])
print(res)
