num = int(input())
a = "+___ "
c = "|__\ "
d = "|    "
i = 1
print(a * num)
while i <= num:
    b = "|" + str(i) + " / "
    print(b, end="")
    i += 1
print()
print(c * num)
print(d * num)
