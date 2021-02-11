string = str(input())
sub_string = "h"
first = string.find(sub_string)
last = string.rfind(sub_string)
res = str(string[:first] + string[last+1:])
print(res)
