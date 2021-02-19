# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности,
# которые равны ее наибольшему элементу.

arr = []
i = 0
inp = int(input())
while inp != 0:
    arr.append(inp)
    inp = int(input())
arr_sort = sorted(arr, reverse=True)
max_arr = max(arr_sort)
while i < len(arr_sort) and arr_sort[i] == max_arr:
    i = i + 1
print(i)


while i < len(arr) and arr[i] != arr[i + 1]:
    i = i + 1
count = i
while count < len(arr) - 1 and arr[count] == arr[count + 1]:
    count = count + 1
a = count - (i - 1)
print(a)
