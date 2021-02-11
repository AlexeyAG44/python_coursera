arr = []
inp = int(input())
while inp != 0:
    arr.append(inp)
    inp = int(input())
prev = -1
max_l = 0
cur_l = 1
for val in arr:
    if val == prev:
        cur_l = cur_l + 1
        if cur_l > max_l:
            max_l = cur_l
    else:
        if cur_l > max_l:
            max_l = cur_l
        cur_l = 1
    prev = val
print(max_l)
