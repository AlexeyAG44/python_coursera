# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

s = str(input())
first_h = s.find('h')
start = s[:first_h + 1]
last_h = len(s) - 1 - s[::-1].find('h')
end = s[last_h:]
middle = s[first_h + 1:last_h:]
sub_string = "h"
print(start, sep="", end="")
for sub_string in middle:
    if sub_string == "h":
        sub_string = "H"
    print(sub_string, sep="", end="")
print(end, sep="", end="")
