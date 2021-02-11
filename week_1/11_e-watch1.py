source = int(input())
hours = source // 60
minutes = source % 60
print((24 + int(hours)) % 24, int(minutes) % 60)
