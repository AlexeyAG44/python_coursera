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
