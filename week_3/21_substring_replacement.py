# Дана строка. Замените в этой строке все цифры 1 на слово one.

string = str(input())
string = string.strip()
sub_string = "1"
count = 0
for sub_string in string:
    if sub_string == "1":
        sub_string = "one"
    print(sub_string, sep="", end="")
