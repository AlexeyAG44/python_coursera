# Дано число N. С начала суток прошло N минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.

source = int(input())
hours = source // 60
minutes = source % 60
print((24 + int(hours)) % 24, int(minutes) % 60)
