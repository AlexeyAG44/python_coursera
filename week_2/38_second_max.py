arr = []
inp = int(input())
while inp != 0:
    arr.append(inp)
    inp = int(input())
arr_sort = sorted(arr, reverse=True)
print(arr_sort[1])
