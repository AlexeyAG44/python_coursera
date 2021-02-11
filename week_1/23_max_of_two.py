a = int(input())
b = int(input())
print(str(b) * (b > a), str(a) * (a > b), str(a) * (a == b), sep="")
