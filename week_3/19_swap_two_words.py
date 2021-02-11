string = str(input())
sub_string = " "
first = string.find(sub_string)
string_1 = string[:first]
string_2 = string[first+1:]
print(string_2, string_1)
