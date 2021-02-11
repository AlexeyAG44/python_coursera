string = str(input())
string = string.strip()
sub_string = "@"
count = 0
for sub_string in string:
    if sub_string == "@":
        sub_string = ""
    print(sub_string, sep="", end="")
