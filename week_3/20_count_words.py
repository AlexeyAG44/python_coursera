# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.

string = str(input())
string = string.strip()
sub_string = " "
count = 1
if string != sub_string:
    for sub_string in string:
        if sub_string == " ":
            count = count + 1
    print(count)
print()
