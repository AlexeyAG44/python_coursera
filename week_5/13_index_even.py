# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# Программа должна быть эффективной и не выполнять лишних действий!

numList = list(map(int, input().split()[::2]))
print(*numList)