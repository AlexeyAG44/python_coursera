string = input()
for i in range(len(string)):
    if i % 3 != 0:
        print(string[i], end="")
