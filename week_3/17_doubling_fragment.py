s = str(input())
first_h = s.find('h')
start = s[:first_h + 1]
last_h = len(s) - 1 - s[::-1].find('h')
end = s[last_h:]
middle = s[first_h + 1:last_h:]
middle *= 2
print(start, middle, end, sep="")
