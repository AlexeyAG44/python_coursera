a = int(input())
b = int(input())
c = a % b
print("YES" * (c == 0), "NO" * (c > 0), sep="")
