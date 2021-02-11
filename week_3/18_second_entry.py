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
