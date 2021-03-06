# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
# Реализуйте алгоритм быстрого возведения в степень.
# Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).

def exp(a1, n1):
    if n1 == 0:
        return 1
    if n1 == 1:
        return a1
    elif n1 % 2 == 0:
        return (a1 ** 2) ** (n1 / 2)
    elif n1 % 2 != 0:
        return a1 * (a1 ** (n1 - 1))


a = float(input())
n = int(input())
print(exp(a, n))
