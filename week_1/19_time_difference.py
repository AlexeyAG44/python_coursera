# Даны два момента времени в пределах одних и тех же суток.
# Для каждого момента указан час, минута и секунда.
# Известно, что второй момент времени наступил не раньше первого.
#
# Определите сколько секунд прошло между двумя моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
h = h2 - h1
m = m2 - m1
s = s2 - s1
print(h * 3600 + m * 60 + s)
