numList = list(map(int, input().split()))
max_num = max(numList)
length = len(numList) - 1
length_rev = numList[::-1]
i_len_rev = length_rev.index(max_num)
print(max(numList), length - i_len_rev)
